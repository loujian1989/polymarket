"""
Kalshi API client with rate limiting, exponential backoff, and batch support.
Auth: RSA-PSS / SHA-256 signed headers.
Docs: https://docs.kalshi.com
"""
import os
import time
import random
import base64
import hashlib
import requests
from datetime import datetime, timezone
from typing import Optional
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://trading-api.kalshi.com/trade-api/v2"

# Token budget per tier (tokens/sec). Default cost per request = 10 tokens.
TIER_READ_BUDGET = {
    "basic":    200,
    "advanced": 300,
    "premier":  1000,
    "paragon":  2000,
    "prime":    4000,
}


class RateLimiter:
    """Token bucket rate limiter."""

    def __init__(self, tokens_per_sec: int = 200, cost_per_request: int = 10):
        self.capacity = tokens_per_sec
        self.tokens = float(tokens_per_sec)
        self.cost = cost_per_request
        self.last_refill = time.monotonic()

    def _refill(self):
        now = time.monotonic()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.capacity)
        self.last_refill = now

    def acquire(self):
        self._refill()
        if self.tokens >= self.cost:
            self.tokens -= self.cost
            return
        # Wait until enough tokens accumulate
        wait = (self.cost - self.tokens) / self.capacity
        time.sleep(wait)
        self._refill()
        self.tokens -= self.cost


class KalshiClient:
    def __init__(
        self,
        key_id: Optional[str] = None,
        private_key_path: Optional[str] = None,
        tier: str = "basic",
    ):
        self.key_id = key_id or os.environ.get("KALSHI_KEY_ID", "")
        pem_path = private_key_path or os.environ.get("KALSHI_PRIVATE_KEY_PATH", "")
        self.private_key = self._load_key(pem_path) if pem_path else None
        self.session = requests.Session()
        self.rate_limiter = RateLimiter(
            tokens_per_sec=TIER_READ_BUDGET.get(tier, 200)
        )

    def _load_key(self, path: str):
        with open(path, "rb") as f:
            return serialization.load_pem_private_key(f.read(), password=None)

    def _sign(self, timestamp_ms: int, method: str, path: str) -> str:
        """RSA-PSS SHA-256 signature over timestamp + method + path (no query string)."""
        msg = f"{timestamp_ms}{method}{path}".encode()
        sig = self.private_key.sign(msg, padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.DIGEST_LENGTH,
        ), hashes.SHA256())
        return base64.b64encode(sig).decode()

    def _headers(self, method: str, path: str) -> dict:
        ts = int(datetime.now(timezone.utc).timestamp() * 1000)
        headers = {"Content-Type": "application/json"}
        if self.private_key and self.key_id:
            headers["KALSHI-ACCESS-KEY"] = self.key_id
            headers["KALSHI-ACCESS-TIMESTAMP"] = str(ts)
            headers["KALSHI-ACCESS-SIGNATURE"] = self._sign(ts, method.upper(), path)
        return headers

    def _get(self, path: str, params: dict = None, max_retries: int = 6) -> dict:
        """GET with rate limiting and exponential backoff on 429."""
        self.rate_limiter.acquire()
        url = BASE_URL + path
        for attempt in range(max_retries):
            resp = self.session.get(url, headers=self._headers("GET", path), params=params)
            if resp.status_code == 200:
                return resp.json()
            if resp.status_code == 429:
                wait = min(2 ** attempt, 60) + random.uniform(0, 1)
                print(f"  [429] Rate limited — backing off {wait:.1f}s (attempt {attempt+1}/{max_retries})")
                time.sleep(wait)
                continue
            if resp.status_code == 401:
                raise PermissionError("401 Unauthorized — check KALSHI_KEY_ID and private key path")
            resp.raise_for_status()
        raise RuntimeError(f"Failed after {max_retries} retries on {path}")

    # ── Public API methods ──────────────────────────────────────────────────

    def get_series(self) -> list[dict]:
        """List all series (e.g. KXNVDA, KXGOOG). 10 tokens."""
        data = self._get("/series")
        return data.get("series", [])

    def get_markets(
        self,
        series_ticker: str = "",
        status: str = "open",
        limit: int = 200,
        cursor: str = "",
    ) -> dict:
        """
        List markets, optionally filtered by series_ticker.
        Returns {'markets': [...], 'cursor': '...'}.
        10 tokens per call.
        """
        params = {"status": status, "limit": limit}
        if series_ticker:
            params["series_ticker"] = series_ticker
        if cursor:
            params["cursor"] = cursor
        return self._get("/markets", params=params)

    def get_all_markets_for_series(self, series_ticker: str) -> list[dict]:
        """Paginate through all markets for a given series. ~10 tokens per page."""
        markets, cursor = [], ""
        while True:
            data = self.get_markets(series_ticker=series_ticker, cursor=cursor)
            markets.extend(data.get("markets", []))
            cursor = data.get("cursor", "")
            if not cursor:
                break
        return markets

    def get_orderbooks_batch(self, tickers: list[str], depth: int = 1) -> list[dict]:
        """
        Fetch orderbooks for up to 100 tickers in a SINGLE request (10 tokens flat).
        Returns list of orderbook dicts with yes_ask, no_ask prices.
        """
        if not tickers:
            return []
        # Batch in chunks of 100
        results = []
        for i in range(0, len(tickers), 100):
            chunk = tickers[i:i+100]
            params = {"tickers": ",".join(chunk), "depth": depth}
            data = self._get("/markets/orderbooks", params=params)
            results.extend(data.get("orderbooks", []))
        return results

    def search_series_by_keywords(self, keywords: list[str]) -> list[dict]:
        """
        Get all series and filter by keywords in ticker or title.
        Returns matching series with their tickers.
        10 tokens for the series list.
        """
        all_series = self.get_series()
        results = []
        for s in all_series:
            ticker = (s.get("ticker") or "").lower()
            title = (s.get("title") or "").lower()
            for kw in keywords:
                if kw.lower() in ticker or kw.lower() in title:
                    results.append(s)
                    break
        return results
