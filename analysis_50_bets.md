# Google Cannot Get Enough Memory — Kalshi Bet Analysis
**Date**: May 30, 2026 | **Platform**: Kalshi | **Markets fetched**: 51 live

---

## Core Thesis & Causal Chain

> **Base Assumption**: Google/Alphabet cannot procure sufficient HBM3/HBM3e and server-grade DRAM for its AI infrastructure throughout 2026–2027.

**Causal chain**: HBM supply shortage → Google panic-buys at premium → CapEx surge → model scaling constrained → competitive disadvantage → memory suppliers capture pricing power → packaging bottleneck → AI unicorns face compute cost crunch → AI valuation bubble stress.

**Note on numbers**: The thesis references "1800–1900亿" — this is RMB (Chinese yuan), not USD. 1,900亿 RMB ≈ $26B USD/quarter or ~$104B annually. Alphabet's actual 2026 CapEx guidance is ~$75–100B USD for the full year. Treat any thesis threshold citing "$195B USD" as a RMB/USD confusion.

**Platform note**: Kalshi's available markets don't cover Google CapEx, Micron gross margins, or HBM contract prices directly. The 51 live markets cluster around AI model competition, OpenAI/Anthropic corporate events, and Broadcom earnings — all **downstream consequences** of the thesis. This analysis maps those proxies to the thesis chain.

---

## ROI Formula

| Contract | Formula | Example |
|----------|---------|---------|
| Buy YES at $P | ROI = (1 − P) / P × 100% | YES at $0.54 → 85% ROI if win |
| Buy NO at P_yes | NO costs (1 − P_yes); ROI = P_yes / (1 − P_yes) × 100% | YES = 88¢ → NO costs 12¢ → 633% ROI if win |

---

## Section I: AI Coding Model Race

**Series**: `KXCODINGMODEL` | **Closes**: Dec 31, 2026 | **Question**: Which AI company will have the best coding model?

**Thesis link**: Memory constraints impair Google's ability to train and serve the largest models. If HBM shortage hits Google harder than its competitors, Google's coding model falls behind Anthropic, OpenAI, and xAI — all of which have more flexible compute procurement.

**Market data**:

| Ticker | Winner | YES | NO | ROI | Verdict |
|--------|--------|-----|----|-----|---------|
| KXCODINGMODEL-26DEC-ANTH | Anthropic | $0.56 | $0.46 | 79% | **Thesis supported — market leader** |
| KXCODINGMODEL-26DEC-OPEN | OpenAI | $0.27 | $0.74 | 270% | Strong #2 — good value |
| KXCODINGMODEL-26DEC-XAI | xAI | $0.10 | $0.94 | 900% | Speculative |
| KXCODINGMODEL-26DEC-GOOG | Google | $0.06 | $0.95 | 1567% | Thesis: Google loses — market agrees at 94% |
| KXCODINGMODEL-26DEC-MOON | Moonshot AI | $0.02 | $1.00 | 4900% | Lottery |
| KXCODINGMODEL-26DEC-DEEP | Deepseek | $0.01 | $1.00 | 9900% | Lottery |
| KXCODINGMODEL-26DEC-ALIB | Alibaba | $0.01 | $1.00 | 9900% | Lottery |
| KXCODINGMODEL-26DEC-ZAI | Z.ai | $0.01 | $1.00 | 9900% | Lottery |
| KXCODINGMODEL-26DEC-BAID | Baidu | $0.01 | $1.00 | 9900% | Lottery |

**Analysis**: The market already prices Google out of the coding race at 6% — thesis aligned but mostly priced in. The real opportunity is Anthropic (56%) vs OpenAI (27%). Anthropic's Claude models have led coding benchmarks since Claude 3.5 Sonnet; the memory thesis gives Anthropic an ongoing structural advantage over Google. OpenAI at 27% is the best value play if you believe they'll close the gap on Anthropic by year-end.

**Recommended bets**:
- **YES ANTH** at $0.56 — high conviction, 79% ROI, thesis strongly aligned
- **YES OPEN** at $0.27 — medium conviction, 270% ROI, good if OpenAI releases coding-focused model
- **Skip GOOG NO** — NO costs $0.94, ROI only 6%; already priced in

---

## Section II: OpenAI IPO Timeline

**Series**: `KXIPOOPENAI` | **Question**: When will OpenAI IPO?

**Thesis link**: Compute cost inflation from HBM scarcity tightens AI startup margins. OpenAI's IPO timing reflects both market appetite and internal pressure from investors to lock in valuation before compute cost crises compound. High YES prices on near-term dates = market expects IPO soon regardless of memory costs.

**Market data**:

| Ticker | Deadline | YES | NO | ROI (YES) | ROI (NO) |
|--------|---------|-----|----|-----------|---------|
| KXIPOOPENAI-26JUN01 | Jun 1, 2026 | $0.01 | $1.00 | 9900% | 1% |
| KXIPOOPENAI-26JUL01 | Jul 1, 2026 | $0.01 | $1.00 | 9900% | 1% |
| KXIPOOPENAI-26AUG01 | Aug 1, 2026 | $0.04 | $0.97 | 2400% | 4% |
| KXIPOOPENAI-26SEP01 | Sep 1, 2026 | $0.09 | $0.92 | 1011% | 10% |
| KXIPOOPENAI-26OCT01 | Oct 1, 2026 | $0.59 | $0.42 | 69% | 140% |
| KXIPOOPENAI-26NOV01 | Nov 1, 2026 | $0.76 | $0.27 | 32% | 281% |
| KXIPOOPENAI-26DEC01 | Dec 1, 2026 | $0.82 | $0.21 | 22% | 390% |
| KXIPOOPENAI-27JAN01 | Jan 1, 2027 | $0.87 | $0.15 | 15% | 580% |
| KXIPOOPENAI-27FEB01 | Feb 1, 2027 | $0.91 | $0.16 | 10% | 569% |
| KXIPOOPENAI-27MAR01 | Mar 1, 2027 | $0.94 | $0.14 | 6% | 671% |
| KXIPOOPENAI-27APR01 | Apr 1, 2027 | $0.95 | $0.09 | 5% | 1056% |
| KXIPOOPENAI-27MAY01 | May 1, 2027 | $0.95 | $0.10 | 5% | 950% |
| KXIPOOPENAI-27JUN01 | Jun 1, 2027 | $0.95 | $0.08 | 5% | 1188% |

**Analysis**: The implied probability distribution peaks around Oct–Dec 2026. The market prices ~87% chance of IPO by Jan 1, 2027. This series is a probability ladder — each earlier date prices in a compressed window.

The thesis suggests compute cost pressure COULD delay IPO (investors nervous about unit economics) OR accelerate it (OpenAI needs public capital to fund compute). Market data leans heavily toward near-term IPO. The most interesting trade is **NO on the Oct 1 deadline** (NO at $0.41, ROI 140%) if you believe OpenAI's IPO is more likely in Q4 2026 than Q3.

**Recommended bets**:
- **NO on KXIPOOPENAI-26OCT01** at $0.41 — 140% ROI if IPO slips past Oct 1. Medium conviction given Sep 1 is only 9%, suggesting Oct is the first realistic window.
- **YES on KXIPOOPENAI-27JAN01** at $0.87 — low ROI (15%) but highest-probability "IPO happens" anchor. Suitable for capital preservation bets.

---

## Section III: Top-Ranked AI Model Before 2027

**Series**: `KXTOPAI-27-JAN01` | **Closes**: Jan 1, 2027 | **Question**: Which company will have the top-ranked AI model?

**Thesis link**: Google's memory constraints limit frontier model quality. Competitors not facing the same HBM bottleneck (OpenAI via Azure, Anthropic via AWS/Google TPU) will hold the top AI ranking through end of 2026.

**Market data**:

| Ticker | Company | YES | NO | ROI |
|--------|---------|-----|----|-----|
| KXTOPAI-27-JAN01-OPEN | OpenAI | $0.51 | $0.50 | 96% |
| KXTOPAI-27-JAN01-XAI | xAI | $0.24 | $0.81 | 317% |
| KXTOPAI-27-JAN01-META | Meta | $0.23 | $0.80 | 335% |
| KXTOPAI-27-JAN01-ALIB | Alibaba | $0.16 | $0.88 | 525% |
| KXTOPAI-27-JAN01-DEPP | Deepseek | $0.14 | $0.90 | 614% |
| KXTOPAI-27-JAN01-BYTE | ByteDance | $0.13 | $0.96 | 669% |
| KXTOPAI-27-JAN01-BAID | Baidu | $0.11 | $0.93 | 809% |
| KXTOPAI-27-JAN01-NVID | Nvidia | $0.09 | $0.93 | 1011% |
| KXTOPAI-27-JAN01-MIST | Mistral | $0.09 | $0.93 | 1011% |
| KXTOPAI-27-JAN01-MOON | Moonshot AI | $0.09 | $0.96 | 1011% |
| KXTOPAI-27-JAN01-ZAI | Z.ai | $0.09 | $0.95 | 1011% |
| KXTOPAI-27-JAN01-01A1 | 01A1 | $0.09 | $0.95 | 1011% |

**Note**: Google is not listed as a market option — implying Kalshi already removed Google as a contender for top AI ranking by 2027. This is a direct thesis validation in market structure.

**Analysis**: OpenAI holds the plurality at 51%. The remaining 49% is split across 11 competitors. This is essentially a winner-take-all market where the individual probabilities sum to ~100% across all outcomes. The thesis is most consistent with OpenAI maintaining top rank (memory constraints suppress Google; OpenAI benefits from NVIDIA compute access via Microsoft Azure).

xAI (Grok), Meta (Llama), and Alibaba (Qwen) are all viable at 14–24% — each represents a plausible scenario where an open-source or Chinese lab disrupts the leaderboard.

**Recommended bets**:
- **YES OPEN** at $0.51 — 96% ROI, thesis aligned, OpenAI most likely to hold top rank
- **YES XAI** at $0.24 — speculative 317% ROI if Elon's Grok surges on compute investment
- **Skip Google** — Google not even on the market. Thesis fully reflected in market structure.

---

## Section IV: OpenAI vs Anthropic IPO Race

**Series**: `KXOAIANTH` | **Closes**: Jan 1, 2040 (long-dated)

**Thesis link**: Compute cost inflation and memory shortages put pressure on AI unicorn fundraising timelines. The IPO order between OpenAI and Anthropic reflects which company has more capital runway and investor confidence despite rising infrastructure costs.

**Market data**:

| Ticker | Outcome | YES | NO | ROI |
|--------|---------|-----|----|-----|
| KXOAIANTH-40-OAI | OpenAI IPOs before Anthropic | $0.79 | $0.26 | 27% |
| KXOAIANTH-40-ANTH | Anthropic IPOs before OpenAI | $0.29 | $0.74 | 245% |

**Analysis**: The market gives a 79% chance OpenAI IPOs first. This aligns with OpenAI's larger scale and near-term IPO timeline (see Section II). Anthropic at 29% is the underdog — but a well-funded one with Amazon backing ($4B+ committed). If memory cost inflation accelerates and hurts OpenAI's margin story more than Anthropic's (Anthropic runs on AWS TPUs, bypassing some HBM supply chain), Anthropic's IPO story could improve.

The 2040 close date makes this a very long-dated bet. Capital is locked up. ROI should be heavily discounted for time value.

**Recommended bets**:
- **Skip** — 2040 horizon ties up capital for too long at thin ROI (27% for OAI, 245% for ANTH but with 14-year duration)
- If you have long-horizon capital: **YES ANTH** at $0.29 is the thesis-aligned contrarian play (245% ROI, Anthropic as compute-efficient underdog)

---

## Section V: Anthropic DoD Lawsuit

**Series**: `KXANTHROPICDOD` | **Closes**: Jan 1, 2028

| Ticker | Outcome | YES | NO | ROI |
|--------|---------|-----|----|-----|
| KXANTHROPICDOD-28 | Anthropic wins the lawsuit | $0.52 | $0.51 | 92% |

**Thesis link**: The Department of War (DoD) lawsuit against Anthropic relates to Anthropic PBC's corporate structure and its obligations to the government. If Anthropic loses, it faces potential restructuring or revenue restrictions — reducing its ability to fund compute at current rates. A win preserves Anthropic's independent capital structure and continued AI model investment.

**Analysis**: At $0.52, this is essentially a coin flip. The market has no strong view. The legal merits depend on specific PBC charter language and DoD contract terms — not directly linked to the memory thesis.

**Recommended bet**: **YES** at $0.52 — 92% ROI if Anthropic wins, essentially even-money with potentially favorable legal setup. Small position only given uncertainty. Not a thesis-core bet.

---

## Section VI: NVIDIA H200 to China

**Series**: `KXH200CHINA` | **Closes**: Jan 1, 2027

| Ticker | Outcome | YES | NO | ROI |
|--------|---------|-----|----|-----|
| KXH200CHINA-27-BEF | NVIDIA H200 confirmed delivered to mainland China | $0.86 | $0.20 | 16% |

**Thesis link**: If NVIDIA H200 chips (which use HBM3e stacked via CoWoS) reach China, it significantly amplifies global HBM demand. Chinese hyperscalers (Alibaba, Baidu, ByteDance, Tencent) would compete for HBM-equipped GPUs, tightening the already-constrained supply chain and strengthening the memory pricing thesis.

**Analysis**: At 86%, the market considers H200 delivery to China near-certain — likely reflecting confirmed reports of export license workarounds or prior shipments before updated restrictions. ROI is only 16%.

**Recommended bet**: **Skip** — ROI too thin at 16% for a near-certain outcome. Better to use this as thesis validation (if H200 is going to China → HBM demand exceeds even bullish forecasts → Micron/Hynix positions, not Kalshi bets).

---

## Section VII: Broadcom Earnings Mentions

**Series**: `KXEARNINGSMENTIONAVGO-26JUN03` | **Closes**: Sep 30, 2026
**Question**: What will Broadcom Inc. mention during their Q2 2026 earnings call?

**Thesis link**: Broadcom is a direct HBM/AI infrastructure beneficiary — their custom ASICs (XPUs) for Google TPUs use CoWoS packaging. What Broadcom emphasizes on earnings calls reveals the real state of AI infrastructure demand, memory appetite, and hyperscaler spending.

**Market data** (sorted by YES price, descending):

| Ticker | Keyword | YES | ROI | Signal |
|--------|---------|-----|-----|--------|
| KXEARNINGSMENTIONAVGO-26JUN03-HYPE | "Hyperscaler" | $0.93 | 8% | Near-certain — baseline demand confirmation |
| KXEARNINGSMENTIONAVGO-26JUN03-TOMA | "TomasBravo" | $0.83 | 20% | High — PE firm connection |
| KXEARNINGSMENTIONAVGO-26JUN03-ANTH | "Anthropic" | $0.80 | 25% | High — Broadcom supplies Anthropic infra |
| KXEARNINGSMENTIONAVGO-26JUN03-OPENA | "OpenAI" | $0.77 | 30% | High — major Broadcom customer |
| KXEARNINGSMENTIONAVGO-26JUN03-META | "Meta" | $0.77 | 30% | High — Meta uses Broadcom network chips |
| KXEARNINGSMENTIONAVGO-26JUN03-COMP | "Competition/competitive" | $0.51 | 96% | Medium — earnings calls vary |
| KXEARNINGSMENTIONAVGO-26JUN03-ACQU | "Acquisition" | $0.37 | 170% | Medium — Broadcom is acquisitive |
| KXEARNINGSMENTIONAVGO-26JUN03-OPTI | "Optical" | $0.34 | 194% | Medium — optical interconnects are a 2026 theme |
| KXEARNINGSMENTIONAVGO-26JUN03-ORGA | "Organic growth" | $0.34 | 194% | Medium |
| KXEARNINGSMENTIONAVGO-26JUN03-NVLI | "NVLink" | $0.30 | 233% | Medium — competitor tech but often mentioned |
| KXEARNINGSMENTIONAVGO-26JUN03-OPEN | "Open source" | $0.28 | 257% | Medium |
| KXEARNINGSMENTIONAVGO-26JUN03-DEPA | "DOGE/Department" | $0.27 | 270% | Low-medium — gov context varies |
| KXEARNINGSMENTIONAVGO-26JUN03-QUAN | "Quantum" | $0.26 | 285% | Low — not Broadcom's focus |

**Analysis**:

The high-probability mentions (Hyperscaler 93%, Anthropic 80%, OpenAI 77%) are near-certainties but offer thin ROI. The thesis-interesting plays are in the middle tier:

- **"Optical" (34%)**: Optical interconnects are increasingly cited as the solution to bandwidth bottlenecks between HBM and AI accelerators. If Broadcom mentions optical, it signals the memory/bandwidth constraint is becoming an engineering priority — direct thesis validation.
- **"NVLink" (30%)**: Broadcom mentioning a competitor's interconnect standard signals how pervasive the AI infrastructure conversation is — they'd only mention NVLink to contrast it with their own solutions.
- **"Quantum" (26%)**: Lowest credibility mention — Broadcom doesn't have a quantum compute product. Would signal a kitchen-sink earnings call.

**Recommended bets**:
- **YES HYPE** at $0.93 — 8% ROI but near-certain thesis validator. Good for anchoring position.
- **YES OPTI** at $0.34 — 194% ROI, high thesis relevance if optical interconnects are a bottleneck solution Broadcom discusses.
- **YES NVLI** at $0.30 — 233% ROI, interesting as a competitive signal.
- **YES COMP** at $0.51 — 96% ROI, essentially a coinflip on whether Broadcom discusses competitive dynamics.

---

## Thesis Gap Analysis

The following thesis bets have **no current Kalshi market**. These require either waiting for new markets or trading the underlying securities directly.

| Thesis Bet | Why No Kalshi Market | Alternative Action |
|------------|---------------------|-------------------|
| Alphabet Q2/Q3/Q4 CapEx beat | Kalshi doesn't cover Google CapEx thresholds | Monitor Kalshi post-earnings; check Polymarket |
| Micron Q3 gross margin >85% | No Kalshi market for Micron earnings | Stock (MU) or Polymarket if listed |
| SK Hynix H2 operating profit record | Korean company, rarely on US prediction markets | Stock: KRX 000660 / OTC HXSCL |
| Samsung HBM qualification | No market for supply-side events | Monitor NVIDIA/Samsung press releases |
| ASML net bookings beat | No market | Stock: ASML on NASDAQ |
| DDR5 contract prices +40% YoY | No market | Track DRAMeXchange/TrendForce monthly |
| TSMC CoWoS ahead of guidance | No market | Monitor TSMC quarterly earnings |
| Lam/KLA beats estimates | No market | Stocks: LRCX, KLAC |

**Bottom line**: Kalshi's available markets address the **downstream consequences** of the thesis (AI model race outcomes, unicorn corporate events) but not the **upstream causes** (memory pricing, CapEx data, equipment orders). For the core thesis validation trades, the relevant instruments are equities and futures, not Kalshi contracts.

---

## Portfolio Construction (Kalshi Only)

### Tier 1 — High Conviction (Execute Now)

| Market | Direction | Price | ROI | Allocation | Rationale |
|--------|-----------|-------|-----|-----------|-----------|
| KXCODINGMODEL-26DEC-ANTH | YES | $0.56 | 79% | 25% | Anthropic leads coding; memory thesis supports Anthropic advantage over Google |
| KXTOPAI-27-JAN01-OPEN | YES | $0.51 | 96% | 20% | OpenAI most likely to hold top AI rank; Google not even listed as option |
| KXEARNINGSMENTIONAVGO-26JUN03-OPTI | YES | $0.34 | 194% | 10% | Optical interconnects = bandwidth bottleneck solution; thesis-aligned signal |
| KXEARNINGSMENTIONAVGO-26JUN03-HYPE | YES | $0.93 | 8% | 5% | Near-certain thesis validation at each Broadcom earnings call |

### Tier 2 — Speculative (Small Size)

| Market | Direction | Price | ROI | Allocation | Rationale |
|--------|-----------|-------|-----|-----------|-----------|
| KXCODINGMODEL-26DEC-OPEN | YES | $0.27 | 270% | 8% | OpenAI as runner-up or winner if they release coding-focused flagship |
| KXEARNINGSMENTIONAVGO-26JUN03-NVLI | YES | $0.30 | 233% | 5% | NVLink mention = advanced packaging in the spotlight |
| KXANTHROPICDOD-28 | YES | $0.52 | 92% | 5% | Coin-flip, but Anthropic win = continued independent compute investment |
| KXIPOOPENAI-26OCT01 | NO | $0.41 | 140% | 5% | IPO more likely Q4 than Q3; NO pays if IPO slips past Oct 1 |
| KXTOPAI-27-JAN01-XAI | YES | $0.24 | 317% | 3% | xAI dark horse; Grok 3 could challenge OpenAI if training compute is unlocked |

### Cash Reserve

| Allocation | Purpose |
|-----------|---------|
| 14% | New Kalshi markets post-Alphabet Q2 earnings (late July 2026) |
| — | New Kalshi markets post-Broadcom Q2 earnings (Sep 2026) |

### Allocation Summary

| Tier | Markets | Bankroll % |
|------|---------|-----------|
| Tier 1 | 4 positions | 60% |
| Tier 2 | 5 positions | 26% |
| Cash reserve | — | 14% |

---

## Key Risks to the Thesis

1. **Samsung HBM qualification**: If Samsung passes NVIDIA/Google's HBM3e qualification, supply increases sharply → prices soften → memory thesis collapses. Monitor Samsung quarterly results.

2. **Distilled/small models reduce HBM demand**: The trend toward small distilled models (Gemini Flash, GPT-4o mini) requires far less HBM per query. If this accelerates, per-unit memory demand drops even as AI queries grow.

3. **Google self-supply via TPUs**: Google's TPU v6+ uses custom memory configurations that partially bypass third-party HBM supply chains. Shortage may hit GPU-based workloads (OpenAI, xAI) more than Google's own infrastructure.

4. **OpenAI/Anthropic success despite thesis**: Both companies are growing in market share. If they succeed despite compute costs, Section V (unicorn stress) is wrong — which is consistent with Section III and IV being right (memory demand stays elevated, Micron wins).

5. **Export control reversal**: If US-China chip restrictions ease, NVIDIA H200/B200 flows to China → HBM demand spikes globally → actually strengthens thesis, but Kalshi's KXH200CHINA-27-BEF (already 86%) has low remaining upside.

---

## Quick Reference Scorecard

| Thesis Area | Kalshi Markets Exist? | Market Agrees With Thesis? | Best Kalshi Play |
|------------|----------------------|--------------------------|-----------------|
| Google CapEx surge | No | N/A — no market | Wait for post-earnings markets |
| Google model quality lags | Yes (KXCODINGMODEL) | Yes — Google at 6% | YES ANTH ($0.56, 79% ROI) |
| Memory suppliers win | No | N/A | Trade MU/HXSCL stocks |
| Advanced packaging bottleneck | No | N/A | Trade AMAT/LRCX stocks |
| AI unicorn stress | Partial (IPO markets) | Mostly no — both are rising | NO on KXIPOOPENAI-26OCT01 |
| HBM demand amplification (China) | Yes (KXH200CHINA) | Yes — 86% priced in | Skip (too thin) |
| Broadcom AI demand signal | Yes (KXEARNINGSMENTIONAVGO) | Yes — hyperscalers 93% | YES OPTI ($0.34, 194% ROI) |

---

*Data sourced from live Kalshi markets (May 30, 2026) via authenticated API at api.elections.kalshi.com. 51 markets fetched. This is analysis only, not financial advice.*
