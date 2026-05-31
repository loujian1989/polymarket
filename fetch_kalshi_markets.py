"""
Fetch Kalshi markets relevant to the "Google memory shortage" thesis
and update the KALSHI MARKET SEARCH GUIDE section in analysis_50_bets.md.

Usage:
  python fetch_kalshi_markets.py           # fetch + update + push
  python fetch_kalshi_markets.py --dry-run # print table only, no file changes
"""
import sys
import re
import subprocess
from kalshi_client import KalshiClient

ANALYSIS_FILE = "analysis_50_bets.md"

# Keywords to search for in Kalshi series tickers/titles
SEARCH_KEYWORDS = [
    "micron", "nvidia", "alphabet", "google",
    "openai", "anthropic", "broadcom", "semiconductor",
    "ai", "hbm", "memory", "chip", "capex",
]

# Known series tickers to try directly (Kalshi naming convention)
KNOWN_SERIES = [
    "KXNVDA", "KXGOOG", "KXGOOGL", "KXMIC", "KXMICRON",
    "KXAVGO", "KXOPENAI", "KXOPAI", "KXANTHOPIC",
    "KXSOX", "KXSMH", "KXAMD", "KXTSM",
]


def cents_to_prob(price_cents) -> float:
    """Kalshi prices are in cents (0–100). Convert to probability 0.0–1.0."""
    if price_cents is None:
        return None
    return price_cents / 100.0


def roi(yes_prob: float) -> str:
    if yes_prob is None or yes_prob <= 0 or yes_prob >= 1:
        return "N/A"
    return f"{(1 - yes_prob) / yes_prob * 100:.0f}%"


def format_market_row(m: dict) -> dict:
    ticker = m.get("ticker", "")
    title = m.get("title", ticker)
    yes_ask = cents_to_prob(m.get("yes_ask"))
    no_ask = cents_to_prob(m.get("no_ask"))
    close_time = (m.get("close_time") or "")[:10]  # YYYY-MM-DD
    volume = m.get("volume", 0)
    return {
        "ticker": ticker,
        "title": title,
        "yes_ask": f"{yes_ask:.0%}" if yes_ask is not None else "N/A",
        "no_ask": f"{no_ask:.0%}" if no_ask is not None else "N/A",
        "roi_yes": roi(yes_ask),
        "roi_no": roi(1 - yes_ask) if yes_ask is not None else "N/A",
        "close": close_time,
        "volume": f"${volume:,}" if volume else "—",
    }


def build_markdown_table(rows: list[dict]) -> str:
    if not rows:
        return "_No markets found on Kalshi for these keywords._\n"

    header = "| Ticker | Title | YES | NO | ROI(YES) | ROI(NO) | Closes | Volume |\n"
    sep    = "|--------|-------|-----|-----|----------|---------|--------|--------|\n"
    lines  = [header, sep]
    for r in rows:
        lines.append(
            f"| `{r['ticker']}` | {r['title']} | {r['yes_ask']} | {r['no_ask']} "
            f"| {r['roi_yes']} | {r['roi_no']} | {r['close']} | {r['volume']} |\n"
        )
    return "".join(lines)


def update_analysis_file(table_md: str):
    with open(ANALYSIS_FILE, "r") as f:
        content = f.read()

    # Replace everything between the KALSHI section header and the next ## heading
    section_header = "## KALSHI MARKET SEARCH GUIDE"
    pattern = rf"({re.escape(section_header)}.*?)(\n## |\Z)"

    replacement_body = f"""{section_header}

*Data fetched via authenticated Kalshi REST API — `GET /trade-api/v2/markets` + batch orderbooks.*

### Live Kalshi Markets (relevant to thesis)

{table_md}

### How to Upgrade Your Kalshi API Tier

| Tier | Read tokens/sec | Effective reads/sec | How to Get |
|------|----------------|--------------------|-----------|
| Basic | 200 | 20/sec | Free signup |
| **Advanced** | 300 | 30/sec | **Apply free at kalshi.com/account/profile** |
| Premier | 1,000 | 100/sec | Email support@kalshi.com with use case |
| Paragon | 2,000 | 200/sec | Contact account manager |
| Prime | 4,000 | 400/sec | Institutional/volume-based |

**Key**: For reading 50 markets, even Basic (200 tokens/sec) is sufficient — one batch call = 10 tokens.
Trading fees are ~$0.07/contract. There is no paid API subscription.

"""
    new_content = re.sub(pattern, lambda m: replacement_body + (m.group(2) if m.group(2).startswith("\n##") else ""), content, flags=re.DOTALL)

    # Fallback: if section not found, append
    if section_header not in new_content:
        new_content = content + "\n" + replacement_body

    with open(ANALYSIS_FILE, "w") as f:
        f.write(new_content)

    print(f"Updated {ANALYSIS_FILE}")


def git_commit_push():
    subprocess.run(["git", "add", ANALYSIS_FILE], check=True)
    subprocess.run(["git", "commit", "-m", "Add live Kalshi market data"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Pushed to GitHub.")


def main():
    dry_run = "--dry-run" in sys.argv
    client = KalshiClient()  # reads KALSHI_KEY_ID + KALSHI_PRIVATE_KEY_PATH from .env

    print("Searching Kalshi series...")
    matched_series = client.search_series_by_keywords(SEARCH_KEYWORDS)
    series_tickers = list({s["ticker"] for s in matched_series} | set(KNOWN_SERIES))
    print(f"Found {len(matched_series)} matching series. Fetching markets...")

    # Fetch markets for each series
    all_markets = []
    for ticker in series_tickers:
        try:
            markets = client.get_all_markets_for_series(ticker)
            all_markets.extend(markets)
        except Exception as e:
            print(f"  Skipping {ticker}: {e}")

    # Deduplicate by ticker
    seen = set()
    unique_markets = []
    for m in all_markets:
        t = m.get("ticker", "")
        if t not in seen:
            seen.add(t)
            unique_markets.append(m)

    print(f"Total unique markets found: {len(unique_markets)}")

    # Sort by volume descending
    unique_markets.sort(key=lambda m: m.get("volume", 0), reverse=True)

    # Format rows
    rows = [format_market_row(m) for m in unique_markets]

    # Print table
    print("\n" + "="*80)
    print("KALSHI MARKETS FOUND:")
    print("="*80)
    for r in rows:
        print(f"  {r['ticker']:30s} YES={r['yes_ask']:6s}  ROI={r['roi_yes']:8s}  Closes={r['close']}")

    if dry_run:
        print("\n[dry-run] No files written.")
        return

    table_md = build_markdown_table(rows)
    update_analysis_file(table_md)
    git_commit_push()


if __name__ == "__main__":
    main()
