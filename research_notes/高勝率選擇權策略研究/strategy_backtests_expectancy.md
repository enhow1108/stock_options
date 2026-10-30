# Win Rate vs. Expectancy of High-Win-Rate Options Selling Strategies (Backtests + Academic Evidence)

_Research notes compiled 2026-10-31. Educational only, not investment advice. Each figure carries its source's data period. Quality warning: many search results were AI-generated mirror sites (options-force.pages.dev, options-simply.pages.dev, apexvol.com, lambdafin.com, stockwirex.com). The notes flag these and do not treat their numbers as evidence._

---

## Q1. Win rates and P&L statistics from published backtests (tastylive, Option Alpha, Spintwig, CBOE indices, others)

### Takeaway
Published short-premium backtests consistently show win rates of 65–98%, and the win rate depends mainly on short-strike delta. Per-trade expectancy is small, though: a few cents to tens of cents per share on a $5-wide spread. Long-run index-level results are equity-like returns at about 60–65% of S&P 500 volatility (PUT), or low single-digit CAGR for managed SPX strangles. A high win rate alone does not mean high returns.

### Cited Findings

**Vertical credit spreads (bull put spread): FlashAlpha SPY matrix (published 2026-04-22; data about 2017/2018-04 to 2026-04; 18,307,256 spreads; all held to expiry; mid prices; no costs)**
- Win rate / max-loss rate / mean realized P&L per share, by short delta (22–45 DTE, $5 wide): 0.40Δ 76.5% / 19.7% / +$0.202; 0.30Δ 82.1% / 14.2% / +$0.132; 0.25Δ 85.7% / 10.9% / +$0.123; 0.20Δ 89.2% / 8.0% / +$0.110; 0.15Δ 93.0% / 4.9% / +$0.118; 0.10Δ 96.5% / 2.5% / +$0.110; 0.05Δ 98.4% / 1.3% / +$0.083 — [FlashAlpha](https://flashalpha.com/articles/spy-put-credit-spread-matrix-8-year-backtest-theoretical-vs-realized)
- By DTE (20–30Δ, $5 wide), win rate / realized P&L / annualized ROC: 0–7 DTE 83.1% / +$0.042 / 75.3%; 8–21 DTE 84.2% / +$0.069 / 41.0%; 22–45 DTE 85.9% / +$0.121 / 32.1%; 46–90 DTE 88.5% / +$0.255 / 32.7%; 91+ DTE 93.6% / +$0.752 / 17.7% — [FlashAlpha](https://flashalpha.com/articles/spy-put-credit-spread-matrix-8-year-backtest-theoretical-vs-realized)
- Selected 45 DTE profiles: 40Δ $5 wide, +$0.33 per trade, 78.2% win rate, 17.3% max-loss rate, IID Sharpe 0.48. 30Δ $5 wide, +$0.28 per trade, 85.2% win rate, 12.1% max-loss rate, Sharpe 0.47. Average credit was about $0.68–$1.06 against an average max loss of about $3.94–$4.32 on $5-wide spreads — [FlashAlpha](https://flashalpha.com/articles/spy-put-credit-spread-matrix-8-year-backtest-theoretical-vs-realized)
- Across all 18.3M rows, the average theoretical EV was −$0.48 per share and the average realized P&L was +$0.58, a realized edge of about +$1.06. The author attributes this to SPY's upward drift and the VRP. The author also warns that $0.10–0.20 per share in transaction costs can erase most of the short-DTE edge, and that the IID Sharpe is an upper bound because losses cluster — [FlashAlpha](https://flashalpha.com/articles/spy-put-credit-spread-matrix-8-year-backtest-theoretical-vs-realized)

**Short strangles: tastylive studies**
- The "Selling Premium Works" study (Oct 23, 2014) sold 262 SPY strangles, one every 5 days. About 83% won, against about 70% POP at entry, for a total profit of $20,333. Buying the same strangles would have lost $20,333 — [tastylive: Our 3 Favorite Strangle Studies (2015-03-23)](https://tastylive.com/news-insights/our-3-favorite-strangle-studies)
- "Premium: Losses before Profits" (Dec 18, 2014): of 1 SD (about 16Δ) strangles, 79% showed an unrealized loss at some point before expiration, yet 83% were winners at expiration. All delta variants tested (15/25/45) had realized win rates above their initial POP — [tastylive](https://tastylive.com/news-insights/our-3-favorite-strangle-studies)
- "Mega Strangle Study" (May 12, 2014): more than 300 1 SD strangles on SPY, GLD, EWW, TLT and IWM, opened at 45 DTE. It compared managing at 50% of max profit with holding to expiry, and IVR ≥50 with IVR <50. The article describes the result only qualitatively, as "strong support" for managing winners and selling in high IV, with no numbers — [tastylive](https://tastylive.com/news-insights/our-3-favorite-strangle-studies)
- A 1 SD SPY strangle opened at 45 DTE took an average of about 22 days to reach 50% of max profit. That timing is the origin of the "manage at 21 DTE" rule — [tastylive search-result summary; episode page](https://www.tastylive.com/shows/market-measures/episodes/duration-to-reach-50-winners-01-17-2017) (episode table not directly verified)
- Unverified secondary claim: a tastylive study of 45 DTE strangles managed at 21 DTE (about 1,600 cycles per delta, 2020–2026) reportedly found about 78% wins at 16Δ and about 67% at 30Δ. The source is stockwirex.com, a low-quality aggregator, so treat it as unverified — [stockwirex](https://stockwirex.com/?p=51173)

**Short strangles: independent SPX backtest (Jesse Blom, SteadyOptions, ORATS data, 2001 to May 2020, EOD, no slippage or commissions)**
- 16Δ strangle, opened at 45 DTE, closed at 50% profit or 21 DTE: CAGR 4.44%, volatility 8.62%, Sharpe 0.52 — [SteadyOptions](https://steadyoptions.com/articles/does-“managing-winners”-add-value-to-short-strangles-r618/)
- 16Δ strangle, opened at 30 DTE, closed at 5 DTE with no profit management: CAGR 5.46%, volatility 8.19%, Sharpe 0.67, beating the managed version — [SteadyOptions](https://steadyoptions.com/articles/does-“managing-winners”-add-value-to-short-strangles-r618/)
- 25Δ put / 16Δ call, 30 DTE to 5 DTE: CAGR 6.30%, volatility 9.93%, Sharpe 0.63 — [SteadyOptions](https://steadyoptions.com/articles/does-“managing-winners”-add-value-to-short-strangles-r618/)

**Cash-secured put / put-writing: Spintwig via Early Retirement Now**
- 5Δ SPY puts, 2018–2020, closed at 50% max profit or expiry: 330 trades with 11 losers, about a 96.7% win rate. Max drawdown was "a fraction" of 100% SPY, 80/20 and 60/40 benchmarks, but more leverage meant bigger drawdowns — [ERN Part 5 (2020-06-17), via search snippets](https://earlyretirementnow.com/2020/06/17/passive-income-through-option-writing-part-5) (the page returned 404 at fetch time, so figures come from search snippets)
- SPX 2016–2021, 2–3 DTE puts held to expiry: 10Δ puts had higher CAGR than 5Δ puts, but larger max drawdown and a lower Sharpe — [ERN Part 9 (spintwig guest post, 2021-11-10)](https://earlyretirementnow.com/2021/11/10/passive-income-through-option-writing-part-9-2016-2021-backtest-guest-post-by-spintwig) (page returned 404 at fetch time; numbers from search snippets only)

**CBOE benchmark indices**
- PUT (monthly ATM cash-secured SPX put), July 1986 to Oct 2008 (Ennis Knupp, 2009): 10.32% annualized vs 8.77% for the S&P 500, with standard deviation of 9.91% vs 15.39%. PUT's skew was more negative. In sharply up months PUT averaged +2.11% vs +4.14% for the S&P, and in sharply down months −2.93% vs −5.38%. Gross ATM premium was about 1.65% of notional per month — [Wikipedia: CBOE S&P 500 PutWrite Index](https://en.wikipedia.org/wiki/CBOE_S%26P_500_PutWrite_Index)
- PUT, June 1988 to May 2007: 12.65% annualized, vs 12.30% for SPTR, 11.86% for BXM and 4.67% for T-bills — [Cboe PUT material, via search snippet](https://en.wikipedia.org/wiki/CBOE_S%26P_500_PutWrite_Index)
- 2016 Wilshire-type study of Cboe options-selling indices: the lowest annualized standard deviations were CNDR at 7.23% and PUT at 10.16% — [Cboe IR (2016-02-23)](https://ir.cboe.com/news/news-details/2016/Study-Analyzes-Performance-of-CBOE-SP-500-SPX-Options-Selling-Indexes-02-23-2016/default.aspx)
- CNDR (sells ~20Δ SPX put and call, buys ~5Δ wings, monthly) and BFLY (sells ATM put and call, buys 5% OTM wings): over about 35 years, the worst peak-to-trough drawdown was 19% for CNDR and 47.1% for BFLY, vs 51% for the S&P 500. 59% of CNDR months returned between 0% and 2%. Neither index had a month beyond ±10%, while the S&P 500 had 11 such months — [Cboe (2021)](https://www.cboe.com/insights/posts/benchmark-indices-series-volatility-management-with-cboes-bfly-and-cndr-indices/)
- BXM, BXMD, PUT and CMBO: betas of 0.57–0.82. Average BXM (ATM covered call) monthly gross premium since May 2006 was about 1.7%. All four had lower returns than the S&P 500 but lower standard deviation and drawdowns. BXMD, PUT and CMBO had higher Sharpe and Sortino ratios — [Cboe (2021-07-20)](https://www.cboe.com/insights/posts/benchmark-indices-series-income-generation-and-smoother-returns-with-cboes-bxm-bxmd-put-and-cmbo-indices)
- Peak-to-trough in 2000–2002: S&P −44.7%, BXM −30.2%, PUT −27.6%. In 2007–2009: S&P −51.0%, BXM −35.8%, PUT −31.6% — [ACG whitepaper (2018)](https://acgnet.com/getattachment/845363f3-97c7-4ac9-be31-762e60b9143d/BXM-PUT-Update;.aspx)

**SPX/SPY 0DTE: Option Alpha platform data (230,000 0DTE trades, Sept 2021 onward; last updated 2025-02-08)**
- Iron butterfly win rate 66.76%, iron condor 70.19%. Together they made up 78% of 0DTE positions. 81% of trades were on SPY — [Option Alpha](https://optionalpha.com/blog/0dte-options-strategy-performance)
- Only 49.64% of Option Alpha 0DTE traders were net profitable, close to a coin flip at the trader level despite trade-level win rates of about 70% — [Option Alpha](https://optionalpha.com/blog/0dte-options-strategy-performance)
- Profitable traders typically opened around 10:15 ET and closed shortly after 12:00 ET, holding about 2 hours. A sample iron butterfly used a 15% profit target, a −25% stop and a 12:00 time exit. Monday was the most profitable day; Tuesday, Thursday and Friday had negative aggregate P&L — [Option Alpha](https://optionalpha.com/blog/0dte-options-strategy-performance)
- An earlier, smaller Option Alpha 0DTE study had 4,959 iron butterflies at a 72% win rate and 3,170 iron condors at 63% — [Option Alpha search snippet](https://optionalpha.com/blog/0dte)
- All-DTE live iron condors on Option Alpha: 65.06% average win rate over 144,976 trades, with an average of 17 DTE at entry and a 10-day hold — [Option Alpha stats](https://optionalpha.com/stats)

### Inferences
- In the FlashAlpha data, mean P&L per trade is roughly flat at about $0.08–$0.20 per share between 5Δ and 40Δ, even though the win rate ranges from 98.4% down to 76.5%. Win rate is mostly a matter of choosing the strike, not of finding edge. A tool should show EV and the max-loss rate next to win rate.
- The trade-level win rate for 0DTE iron condors and butterflies (about 67–70%) does not carry over to trader-level profitability (about 50%). The loss size and costs dominate.

### Gaps
- No primary tastylive table was retrieved with avg win, avg loss and P&L per day for 16Δ vs 30Δ at 45 DTE managed at 21 DTE. Episode pages carry the numbers only in video or slides.
- spintwig.com was not fetched, and its per-strategy tables (win rate, avg win/loss, max DD, Sharpe for SPY/SPX puts, strangles, iron condors, covered calls and the wheel) are not in these notes. ERN pages returned 404.
- No ProjectOption/projectfinance primary data. A lambdafin.com claim that "50% profit and 100% stop was most consistent" for 16Δ SPY strangles was not verified.
- No calendar/diagonal spread backtest with win rate and expectancy was found.
- No current (2025–2026) factsheet values for PUT, BXM, CNDR or BFLY were obtained. The Cboe PDF factsheet could not be parsed. Use the Cboe dashboards (e.g. https://www.cboe.com/us/indices/dashboard/PUT/) for current stats.
- No wheel-strategy backtest numbers were found.

---

## Q2. Academic evidence on the volatility risk premium (VRP) and 0DTE returns

### Takeaway
There is a well-documented negative market volatility risk premium, so S&P index options are on average overpriced and option sellers are paid for bearing crash and volatility risk. The premium is largest when volatility is high, and evidence outside the S&P 500 is mixed. On 0DTE, the evidence says retail buyers lose (mostly to transaction costs), sellers profit modestly before costs, and simple static hold-to-expiry 0DTE rules show no robust edge.

### Cited Findings
- Bakshi & Kapadia (2003, *Review of Financial Studies* 16(2):527–566): delta-hedged S&P 500 index option portfolios underperform zero, consistent with a negative market volatility risk premium. The underperformance is smaller for options away from the money, larger in high-volatility periods, and survives controls for jump fears — [RePEc/IDEAS](https://ideas.repec.org/a/oup/rfinst/v16y2003i2p527-566.html)
- A KOSPI200 replication found no volatility risk premium in that market, so the VRP is not universal — [Emerald JDQS](https://www.emerald.com/jdqs/article/17/2/67/205260/The-Volatility-Risk-Premium-in-the-KOSPI200-Index)
- Israelov, "Pathetic Protection" (2017), on put-buying, the mirror image of put-selling. In simulations with no VRP, a put-protection portfolio has 0.0% annualized alpha and 0.83 beta, and a 78% SPTR / 22% cash mix matches its compound return. With a VRP added, alpha falls to −1.9% per year (beta 0.82, volatility 16.9%) — [CXO Advisory summary](https://www.cxoadvisory.com/equity-options/do-protective-equity-index-puts-work-well/)
- Over Jul 1986 to May 2016, Cboe's PPUT (5% put-protection) index matched an equal-return stock/cash mix at about 2.5% CAGR excess but had a deeper drawdown, −32.1% vs −20.9% — [CXO Advisory](https://www.cxoadvisory.com/equity-options/do-protective-equity-index-puts-work-well/) (as summarized; the link to Israelov's paper was not confirmed)
- Israelov & Klein (AQR collar study): collars lost about 1.3% a year to the VRP, because the long put carries a higher volatility premium than the short call — [CXO Advisory: equity index collar performance](https://www.cxoadvisory.com/equity-options/equity-index-collar-performance); [AQR supplement](https://aqr.com/Insights/Research/Journal-Article/Risk-and-Return-of-Equity-Index-Collar-Strategies-Supplement)
- Beckmeyer, Branger & Gayda, "Retail Traders Love 0DTE Options… But Should They?" (SSRN 4404704, March 2023): retail 0DTE traders lost more than $70M over about 2 years, more than $50M of it transaction costs. Daily retail losses averaged $184k over the full sample and $358k after daily expiries began on May 16, 2022. Long positions lost on average, and short positions were profitable even after fees — [Medium summary](https://medium.com/@y125789/retail-traders-love-0dte-options-paper-summary-6da4a7ff7d72); [BNN Bloomberg (2023-04-21)](https://www.bnnbloomberg.ca/day-traders-lose-358-000-per-day-gambling-on-zero-day-options-1.1910634)
- Vilkov, "0DTE Trading Rules" (Nov 2023): tests unhedged daily SPX 0DTE positions (straddles, condors, spreads, butterflies, risk reversals) opened at 10:00, 13:00 or 15:00 and held to 16:00. Secondary summaries say static rules show no consistent profitability (Sharpe "near zero"), and the paper argues that conditional rules need forecasts of realized skewness — [CXO Advisory](https://cxoadvisory.com/equity-options/0dte-strategy-outcomes); [blog summary](https://breakingnasdaq.beehiiv.com/p/the-0dte-illusion) (paper tables not verified)
- Hull Tactical (2026-07-08) frames 0DTE as a "tiny edge, huge distribution" problem — [Hull Tactical](https://hulltactical.com/2026/07/08/0dte-options-tiny-edge-huge-distribution/) (headline only; content not fetched)

### Inferences
- Bakshi & Kapadia's finding that the VRP is larger in high-volatility periods supports IV-rank or VIX-level entry filters in theory. Gross mark-to-market losses are also largest in those regimes, so a filter changes the payoff distribution more than it removes tail risk.
- 0DTE evidence suggests that any seller edge is thin relative to bid-ask and commission costs. A tool should model fills at the bid/ask, not the mid.

### Gaps
- Carr & Wu (2009, "Variance Risk Premiums") figures were not retrieved; from memory, they document large negative variance risk premia on SPX. Verify before citing.
- AQR's "Understanding the Volatility Risk Premium" (Israelov & Nielsen, about 2018) was not retrieved.
- No 2024–2026 peer-reviewed 0DTE seller-return paper with confirmed numbers was found. Vilkov's exact Sharpe values were not verified.

---

## Q3. How win rate trades off with expectancy (90% win rate, but a loss is 5–10× the average win)

### Takeaway
For defined-risk credit spreads, win rate and the payoff ratio are close mirror images. At 10–20Δ, the max loss is about 4–10× the credit, so the strategy breaks even only if the win rate stays above roughly 80–90%. Measured edges are a few percentage points of win rate above breakeven.

### Cited Findings
- On $5-wide SPY spreads at 22–45 DTE, average credit was about $0.68–$1.06 against an average max loss of about $3.94–$4.32, a loss-to-credit ratio of roughly 4:1 to 6:1. Even so, realized EV was only +$0.08 to +$0.20 per share across deltas — [FlashAlpha](https://flashalpha.com/articles/spy-put-credit-spread-matrix-8-year-backtest-theoretical-vs-realized)
- 98.4% win rate at 5Δ (1.3% max-loss rate), +$0.083 per share; 76.5% win rate at 40Δ (19.7% max-loss rate), +$0.202 per share. The lower win rate produced more than twice the EV per trade — [FlashAlpha](https://flashalpha.com/articles/spy-put-credit-spread-matrix-8-year-backtest-theoretical-vs-realized)
- Theoretical (risk-neutral) EV averaged −$0.48 per share. Realized profits came from the drift and VRP of a mostly bullish 2018–2026 sample with one bear year (2022) — [FlashAlpha](https://flashalpha.com/articles/spy-put-credit-spread-matrix-8-year-backtest-theoretical-vs-realized)
- A 1 SD strangle has roughly 68% probability of expiring between the strikes and about 70%+ POP including credit, yet realized win rates were around 83% — [tastylive](https://tastylive.com/news-insights/our-3-favorite-strangle-studies)
- The LJM Preservation & Growth Fund, a short S&P futures options seller similar to a short strangle, saw NAV fall from $9.82 (Feb 2, 2018) to $1.94 (Feb 7, 2018), about −80% in a week, wiping out years of small gains. One estimate put leverage at about 60:1 short — [SEC complaint](https://www.sec.gov/file/sec-complaint-2095); [SteadyOptions](https://steadyoptions.com/articles/the-spectacular-fall-of-ljm-preservation-and-growth-r336); [Business Standard/Reuters](https://www.business-standard.com/amp/article/reuters/u-s-fund-that-lost-most-of-its-value-shuts-doors-to-new-investment-118020900219_1.html)

### Inferences
- Breakeven win rate for a defined-risk credit spread held to expiry (ignoring partial losses) = max loss ÷ (credit + max loss). A $0.70 credit on a $5 spread (max loss $4.30) needs about 86%, close to the observed 86–89% at 20–25Δ. The tool should display breakeven win rate vs. historical win rate, plus a confidence interval.
- Formula for the tool: EV = p_win × avg_win − p_loss × avg_loss − costs. Also report the profit factor, the CVaR of the worst 1–5% of trades, and the max-loss rate, not just the win rate.

### Gaps
- No primary source gave explicit avg-win/avg-loss ratios for managed 45 DTE strangles or iron condors. tastylive numbers live in videos.

---

## Q4. Performance in crash events (Feb 2018 Volmageddon, Mar 2020, Aug 2024, Apr 2025)

### Takeaway
Crash outcomes depend mostly on leverage and on undefined vs. defined risk. Defined-risk monthly indices (CNDR) have had max drawdowns under 20%, while leveraged naked short-vol funds (LJM, Feb 2018) lost about 80% in days. Index-level numbers for Aug 2024 and Apr 2025 were not found.

### Cited Findings
- Feb 2018: LJM Preservation & Growth, short S&P futures options, fell about 80% between Feb 2 and Feb 7, 2018. It closed to new investment on Feb 8 and was liquidated in March 2018. The SEC later alleged its stress tests showed potential losses greater than the worst-case figures disclosed to investors — [SEC complaint](https://www.sec.gov/file/sec-complaint-2095); [AI-CIO](https://www.ai-cio.com/news/risky-business-leads-to-1-billion-trading-loss-charges-for-fund-execs/)
- Aug 2024: on Aug 5, 2024 the VIX recorded its largest-ever one-day spike. The BIS attributes part of the move to dealer quote-setting and widening bid-ask spreads, especially in puts, which means mark-to-market losses for option sellers were amplified by illiquidity — [BIS Bulletin 95](https://www.bis.org/publ/bisbull95.htm). Cboe reported that broad averages fell nearly 6% in a few days as implied vol reached levels not seen since 2021 — [Cboe Index Insights Aug 2024](https://www.cboe.com/insights/posts/index-insights-august-2024)
- Apr 2025: Cboe described April 2025 (tariff announcement after the close on Apr 2) as one of the most volatile periods in recent history. Indices with long optionality did best, and the VIX Tail Hedge Index ended the month up more than 3% — [Cboe Index Insights April](https://www.cboe.com/insights/posts/index-insights-april)
- 2008 and 2000–02: PUT drew down −31.6% vs −51.0% for the S&P (2007–09), and BXM −35.8%. In 2000–02, PUT was −27.6% and BXM −30.2% vs −44.7% for the S&P — [ACG](https://acgnet.com/getattachment/845363f3-97c7-4ac9-be31-762e60b9143d/BXM-PUT-Update;.aspx)
- 2022 bear year, SPY put spreads at 20–30Δ, $5 wide: win rate 78.5%, max-loss rate 18.2%, average P&L only +$0.02 per share. The author estimates a 2022-style stress on a full-size $100k ladder would lose about $20–30k — [FlashAlpha](https://flashalpha.com/articles/spy-put-credit-spread-matrix-8-year-backtest-theoretical-vs-realized)
- CNDR's worst drawdown in about 35 years was 19%, BFLY's 47.1%, the S&P 500's 51% — [Cboe](https://www.cboe.com/insights/posts/benchmark-indices-series-volatility-management-with-cboes-bfly-and-cndr-indices/)

### Inferences
- Defined-risk wings (CNDR vs a naked strangle) cap the per-cycle loss. The tool should stress-test positions against historical shock days (2018-02-05, 2020-03-16, 2024-08-05, 2025-04-03/04) using gap moves plus IV expansion and wider spreads, not just delta.

### Gaps
- No source gave monthly PUT, BXM or CNDR returns for Feb 2018, Mar 2020, Aug 2024 or Apr 2025. Pull them from the Cboe dashboards.
- The OptionSellers.com November 2018 natural-gas strangle blowup could not be verified in this search.
- No Spintwig or tastylive March 2020 strangle or iron condor drawdown figures were retrieved.

---

## Q5. Which rule variants (delta, DTE, profit target, stop loss, IV filter) improve risk-adjusted returns

### Takeaway
The evidence is mixed and often contradicts popular rules. Lower delta raises win rate and Sharpe but lowers CAGR. Longer DTE raises per-trade P&L but lowers annualized ROC. The "50% profit / 21 DTE" rule did not beat simpler time-based exits in one independent 2001–2020 SPX test. Short-hold 0DTE structures with tight profit targets and stops appear among profitable traders, but evidence of a robust edge is weak.

### Cited Findings
- Profit-taking: on SPX 2001–2020, a 16Δ strangle with a 50% profit target or 21 DTE exit returned Sharpe 0.52 (CAGR 4.44%). An unmanaged 30→5 DTE version returned Sharpe 0.67 (CAGR 5.46%), so "managing winners" did not improve risk-adjusted returns there — [SteadyOptions](https://steadyoptions.com/articles/does-“managing-winners”-add-value-to-short-strangles-r618/)
- tastylive's position: close at 50% for discipline and to avoid gamma risk near expiration. Its Mega Strangle Study found qualitative support for managing at 50% and for selling at IVR ≥50 — [tastylive](https://tastylive.com/news-insights/our-3-favorite-strangle-studies)
- Delta: on SPY spreads, lower delta raised the win rate (98.4% at 5Δ) but not EV per trade (highest at 40Δ, +$0.20) — [FlashAlpha](https://flashalpha.com/articles/spy-put-credit-spread-matrix-8-year-backtest-theoretical-vs-realized). For spintwig SPX short puts, 10Δ had higher CAGR than 5Δ but larger drawdown and lower Sharpe — [ERN Part 9 snippet](https://earlyretirementnow.com/2021/11/10/passive-income-through-option-writing-part-9-2016-2021-backtest-guest-post-by-spintwig)
- Skewing the strangle (25Δ put / 16Δ call) raised CAGR to 6.30% at Sharpe 0.63 — [SteadyOptions](https://steadyoptions.com/articles/does-“managing-winners”-add-value-to-short-strangles-r618/)
- DTE: per-trade P&L rises with DTE (+$0.04 at 0–7 DTE vs +$0.75 at 91+ DTE), while annualized ROC falls (75.3% vs 17.7%). Short-DTE edge is most exposed to costs — [FlashAlpha](https://flashalpha.com/articles/spy-put-credit-spread-matrix-8-year-backtest-theoretical-vs-realized)
- 0DTE: profitable Option Alpha traders used about 2-hour holds with tight targets and stops (e.g. 15% profit target, −25% stop). Short call spreads on an SMA5 buy signal and short put spreads on an SMA5 sell signal (mean-reversion fades) had a profit factor above 2.0 and a win rate above 75%, covering about 17% of trades. This is in-sample data-mining from platform trades — [Option Alpha](https://optionalpha.com/blog/0dte-options-strategy-performance)
- Static hold-to-expiry 0DTE rules show no robust edge. Conditioning on forecasts of realized skewness is proposed instead — [CXO Advisory on Vilkov](https://cxoadvisory.com/equity-options/0dte-strategy-outcomes)
- Wider, defined-risk wings: CNDR (20Δ short, 5Δ long) had a 19% max drawdown and 7.23% volatility, vs 10.16% for PUT — [Cboe 2021](https://www.cboe.com/insights/posts/benchmark-indices-series-volatility-management-with-cboes-bfly-and-cndr-indices/); [Cboe IR 2016](https://ir.cboe.com/news/news-details/2016/Study-Analyzes-Performance-of-CBOE-SP-500-SPX-Options-Selling-Indexes-02-23-2016/default.aspx)
- Stop losses: a tastylive episode compared 16Δ SPY strangles from 2005 to 2018 held to expiry, managed at 21 DTE, and with loss stops at various multiples. Its results were not retrievable — [tastylive (2019-03-07)](https://www.tastylive.com/shows/market-measures/episodes/stop-losses-in-strangles-03-07-2019)

### Inferences
- Popular rules ("16Δ, 45 DTE, 50%/21 DTE, IVR > 50") are supported mostly by tastylive's own studies with few published numbers. Independent tests (SteadyOptions/ORATS) don't show clear Sharpe gains from profit-taking. The tool should let users backtest variants rather than hard-code these rules as optimal.
- The highest-Sharpe variants in this evidence are defined-risk or lower-delta structures. The highest-CAGR variants are higher delta or leveraged, with deeper drawdowns.

### Gaps
- No primary quantitative evidence on whether IV rank filters improve Sharpe; only qualitative tastylive claims.
- No verified stop-loss study numbers (tastylive 2019 and projectfinance were not retrieved).
- No evidence retrieved on calendar/diagonal rule variants, the wheel, or covered call delta choice beyond BXM vs BXMD (BXMD uses 30Δ calls and had a higher Sharpe than BXM per Cboe 2021, qualitatively) — [Cboe 2021](https://www.cboe.com/insights/posts/benchmark-indices-series-income-generation-and-smoother-returns-with-cboes-bxm-bxmd-put-and-cmbo-indices)
