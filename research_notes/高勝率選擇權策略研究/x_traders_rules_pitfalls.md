# Systematic Option Sellers on X/Twitter: Accounts, Rules, Pitfalls, Blowups (as of Oct 2026)

Scope note: Educational only. X/Twitter is hard to search directly (no reliable nitter mirror was used). Most X content below was verified indirectly through Thread Reader mirrors, articles, podcasts, or the traders' own blogs. **Any handle not confirmed by a cited source is marked UNVERIFIED.** Several "rule" sources are tastylive episode pages or third-party digests (options-simply / options-force pages.dev sites, recapio.com) that look AI-generated or are secondary study guides. They are flagged where used.

## (a) Which X accounts / traders are frequently cited, and what do they share?

### Takeaway
The ecosystem splits into (1) **education/platform brands that publish rules and backtests** (tastytrade/tastylive, Option Alpha), (2) **individual practitioners who publish track records** (Karsten "Big ERN" Jeske's SPX put-writing; the cautionary "Captain Condor" community), and (3) **professional volatility traders who criticize retail premium selling** (Benn Eifert of QVR; Euan Sinclair). Flow/gamma services like SpotGamma are often cited by 0DTE traders but are analytics vendors, not systematic sellers. Search could not confirm the handles @darjohn25, @VolatilityWiz or @sinclaireuan. Treat them as UNVERIFIED.

### Cited Findings
**tastytrade / tastylive (Tom Sosnoff, Tony Battista, Dr. Jim Schultz). Brand X handle not confirmed in this search, so it is UNVERIFIED.**
- tastylive's published research is the main source of the "45 DTE / 16-delta strangle / manage at 50% or 21 DTE" rule set. A 2019 Best Practices episode reports that a 16Δ, 45 DTE strangle exited at 21 DTE performed better than managing at 50% or holding to expiration. — [tastylive Best Practices, Trade Entry & Exit 07-08-2019](https://www.tastylive.com/shows/best-practices/episodes/trade-entry-and-exit-07-08-2019)
- 2016 segment: "Why manage at 50% not 25% for short strangles" (16Δ strangles managed at 25%, 50%, or held to expiry). — [tastylive Options Jive 09-13-2016](https://tastylive.com/shows/options-jive/episodes/why-manage-at-50-not-25-for-short-strangles-09-13-2016)
- Duration/delta management study. — [tastylive Market Measures 03-17-2016](https://tastylive.com/shows/market-measures/episodes/duration-delta-management-03-17-2016)
- tastylive piece on capital allocation: exiting at 21 DTE gave the best containment of volatility, and managing at 50% gave a bigger profitability jump but more P/L volatility. Scaling up when IV Rank is high gave better results but a bigger largest loss. — [tastylive news-insights: How Capital Allocation Impacts Volatility](https://www.tastylive.com/news-insights/How-Capital-Allocation-Impacts-Volatility)
- Credibility: these are in-house backtests by a broker/media company that earns on transaction volume, mostly on SPY/IWM/TLT, over limited periods. One secondary summary notes the 50% figure is "a chosen heuristic, not a proven optimum". — [options-simply (secondary, possibly AI-generated)](https://options-simply.pages.dev/p/profit-targets-vs-holding)

**Option Alpha (Kirk Du Plessis). Handle @OptionAlpha is UNVERIFIED in this search, though the brand is real.**
- Option Alpha publishes 0DTE studies built from its users' automated-bot trades. Its first study (about 25,000 trades) reported **3,170 iron condors with a 63% win rate** and iron butterflies with a 72% win rate. Average hold time was 155 min for condors and 137 min for butterflies. — [Option Alpha: 0DTE options strategy performance](https://optionalpha.com/blog/0dte-options-strategy-performance)
- Follow-up study of about 230k 0DTE trades: **only 49.64% of Option Alpha traders using a 0DTE strategy were profitable.** — [Option Alpha 0DTE blog](https://optionalpha.com/blog/0dte)
- I could not confirm that Du Plessis personally authored those studies.

**Karsten Jeske, "Big ERN" (EarlyRetirementNow.com). He is active on X, but the handle is not confirmed here, so it is UNVERIFIED.**
- Rules he publishes: "Every trading day, I write (=short) very short-dated (1DTE) CBOE puts on the SPX index… my bread-and-butter strategy since 2011." He adds 0DTE puts near the open and occasionally 1DTE calls. He uses stop-losses. In 2025 he was stopped out by a sub-1% intraday drop when his OTM cushion "was a bit too tight." — [ERN Options Trading Series Part 14, 2025 Review](https://earlyretirementnow.com/2026/01/30/options-trading-series-part-14-year-2025-review)
- Track record he discloses: the 0DTE/1DTE put strategy returned "just under $100,000 in 2024", on top of his portfolio returns. In 2025 he traded just over 10,000 contracts with more than $6.5B notional. — [ERN Part 13, 2024 Review](https://earlyretirementnow.com/2025/01/14/options-trading-series-part-13-year-2024-review/); [Part 14](https://earlyretirementnow.com/2026/01/30/options-trading-series-part-14-year-2025-review)
- Older version of the strategy (2016–2020): about 5 delta or below, with leverage cut from 3–3.5x to 2–2.5x. — [ERN Part 4 (2020)](https://earlyretirementnow.com/2020/06/10/passive-income-through-option-writing-part-4/); [ERN Part 1 (2016)](https://earlyretirementnow.com/2016/09/28/passive-income-through-option-writing-part1/)
- Third-party analysis: the daily skew of ERN's option portfolio is about −5.1 (vs −0.5 for the S&P 500), and quarterly skew is about +0.1. — [the7circles.uk: ERN's Options Strategy](https://the7circles.uk/?p=27364)
- Credibility: among the more credible public retail track records, because he publishes multi-year reviews that include losing periods (e.g., 2018, 2020). It is still self-reported and not audited.

**Benn Eifert (CIO, QVR Advisors). Active on X, confirmed via Thread Reader mirrors of his threads. Exact handle not shown in results (commonly @bennpeifert), so the handle is UNVERIFIED.**
- His covered-call / option-selling mega-thread says "systematically, blindly selling options is a BAD IDEA. Underperforms owning equities by a lot". Influencers quote "income" as premium sold or theta collected, which he calls only half the story. — [Thread Reader: Benn Eifert thread 1955996656387940647](https://threadreaderapp.com/thread/1955996656387940647.html)
- His 2022 theta thread: theta is not alpha. Short premium pays only if the market overprices gamma/vanna/volga. The expected risk premium is "a tiny fraction of overall theta", possibly smaller than retail transaction costs. — [Thread Reader 1572019785797603328](https://threadreaderapp.com/thread/1572019785797603328.html)
- Nuance: "all volatility selling is not the same" (Jan 2025 thread). — [Thread Reader 1878126777383448915](https://threadreaderapp.com/thread/1878126777383448915)
- Related: a Risk.net piece, "The options experts who think vol selling is a broken trade". — [Risk.net](https://www.risk.net/node/7962573)

**Euan Sinclair (author of *Volatility Trading* and *Positional Option Trading*; Bluefin). X handle @sinclaireuan is UNVERIFIED.**
- Podcast: "0DTE The Trap? with Euan Sinclair" (Sharpe Two Podcast Ep. 1). A third-party summary says he treats edge as positive expected value and compares selling volatility to selling insurance, where occasional large losses are part of the model. The full transcript was not retrievable. — [recapio digest (third-party)](https://recapio.com/digest/0dte-the-trap-with-euan-sinclair-the-sharpe-two-podcast-ep-1-by-sharpe-two)
- Robot Wealth AMA with Sinclair (June 2025). — [Robot Wealth](https://robotwealth.com/ask-me-anything-with-euan-sinclair-19-june-2025/)

**SpotGamma (Brent Kochuba).** An options-positioning / gamma-exposure analytics vendor (paid tiers, e.g., Alpha at about $299/mo). 0DTE traders cite it for levels. It is not a systematic seller with a track record. — [SpotGamma products](https://spotgamma.com/products/)

**"Captain Condor" / David Chau (InsideOptions community, SPX Program Fund LP).** He ran a subscription community selling large 0DTE SPX iron condors, reportedly with martingale-style sizing. Details in section (d). — [Wikipedia: David Chau](https://en.wikipedia.org/wiki/David_Chau)

**Not verified:** @darjohn25 and @VolatilityWiz. Search returned no indexed profile or post. Tony Zhang (OptionsPlay, CNBC contributor) is a known options educator, but this search returned no X-specific material on him. All three are UNVERIFIED.

### Inferences
- The most widely shared "rules" on X trace back to tastylive and Option Alpha content. These are vendors whose revenue depends on trading activity, so the rules are marketed as much as they are researched.
- Credible public critiques mostly come from professional vol traders (Eifert, Sinclair). They do not say short vol has no premium. They say *blind, crowded, unhedged* selling has a small edge relative to costs and tail risk.

### Gaps
- Direct X post retrieval was not possible. Handles for tastylive, Option Alpha, ERN, Eifert, and Sinclair should be checked on x.com before being cited.
- I found no audited track record for any retail-facing X option seller.
- I found no Sinclair quote directly criticizing the "50% profit target" or "high win rate" framing. Do not attribute one to him.

## (b) The common rule set used in practice

### Takeaway
The standard retail "mechanical" rule set comes mainly from tastylive:
- **Entry:** around 45 DTE, short strikes at about 16Δ (1 SD) to 30Δ, preferably when IV Rank is high.
- **Exit:** take profit at 50% of credit, or close/roll at 21 DTE.
- **Defined risk:** close at about 2x credit, or when a short strike is touched.
- **Sizing:** 3–7% of buying power or net liq per undefined-risk position, with total buying power usage capped (often 30–50%).

0DTE SPX sellers use a separate rule family: intraday iron condors or credit spreads, tight stops, small size. All of these numbers are heuristics, not proven optima.

### Cited Findings
- **45 DTE entry, 16Δ, exit at 50% or 21 DTE.** tastylive's 2019 review found entering at 45 DTE and exiting at 50% profit or 21 DTE gave the largest daily P/L, and 21 DTE beat 50% management and holding to expiry for 16Δ strangles. — [tastylive Best Practices 2019](https://www.tastylive.com/shows/best-practices/episodes/trade-entry-and-exit-07-08-2019)
- Secondary claim: a 1 SD strangle opened at about 45 DTE reaches about 50% of max profit around 21 DTE on average. Not verified against raw data. — [options-simply (secondary)](https://options-simply.pages.dev/p/21-dte-management)
- **Gamma rationale for 21 DTE:** gamma risk rises sharply as expiration approaches. — [tastylive Options Jive 2016](https://tastylive.com/shows/options-jive/episodes/why-manage-at-50-not-25-for-short-strangles-09-13-2016)
- **Position sizing:** tastylive-linked summaries say 3–7% of buying power (or of net liquidating value) per undefined-risk position. Overall committed capital is about 30–50% when IV is low, and buying power usage scales up when IVR is high. Buying-power requirements drop about 35–40% moving from low-IV to high-IV environments, because prices are lower and the extra volatility shifts margin. — [recapio: How to Size Naked Options Without Blowing Up (third-party)](https://recapio.com/digest/how-to-size-naked-options-without-blowing-up-by-tastylive); [recapio: How Volatility Changes Your Capital Requirements (third-party)](https://recapio.com/digest/how-volatility-changes-your-capital-requirements-by-tastylive); [tastylive: Trading Too Big 2016](https://tastylive.com/shows/best-practices/episodes/trading-too-big-04-04-2016); [tastylive: Risk Capital Allocation 2014](https://www.tastylive.com/shows/market-measures/episodes/risk-capital-allocation-10-24-2014)
- **IV Rank filter:** I found no primary tastylive source fixing an "IVR > 30" cutoff. One study summary cites "High IVR (>40)" as giving fewer trades but higher premium returns, and says IVR thresholds should flex after vol spikes. — [pulse.bot video summary (third-party)](https://www.pulse.bot/options-derivatives/video/most-traders-wait-for-high-ivr-to-sell-premium-heres-why-thats-the-wrong-move-after-a-vix-spike-e67bb973-fc34-46c4-af2f-57c19eb9929c)
- **Non-tastylive buying-power guidance:** "never use more than 50% of portfolio margin buying power", and many cap it at 30–40%. — [optionsnest portfolio margin page (secondary)](https://optionsnest-com.pages.dev/courses/advanced/portfolio-margin/)
- **0DTE SPX:** Option Alpha user data shows iron condors at a 63% win rate and iron butterflies at 72%, yet about half of 0DTE users are unprofitable overall. — [Option Alpha](https://optionalpha.com/blog/0dte-options-strategy-performance); [Option Alpha 0DTE](https://optionalpha.com/blog/0dte)
- tastylive-related summaries cite about 90% win rates for 20Δ 0DTE SPX iron condors, with the caveat that the bull-market sample inflated results. — [recapio: 0DTE Profit Targets, Win Rate & Risk (third-party)](https://recapio.com/digest/0dte-options-trading-strategy-profit-targets-win-rate-risk-by-tastylive)
- **Stops for daily index put-writing (ERN):** stop-losses are used, and too tight an OTM cushion leads to frequent stop-outs. — [ERN Part 14](https://earlyretirementnow.com/2026/01/30/options-trading-series-part-14-year-2025-review)
- **Captain Condor's reported entry filter:** sell 0DTE condors when realized vol exceeded implied vol two days in a row. Secondary reporting; Option Strategist notes the exact strategy cannot be definitively confirmed. — [Option Strategist: A Tragic Tale of Too Much Risk](https://optionstrategist.com/node/19645)

### Inferences
- The stop rule of "close at 2x credit or on short-strike touch" is widely repeated on r/thetagang and r/options, but I did not retrieve a primary source that defines it. Treat it as community convention.
- The 50% / 21 DTE rules mainly reduce gamma exposure and P/L variance. They do not create edge. Edge, if any, comes from implied vol exceeding realized vol (the variance risk premium).

### Gaps
- I found no primary-source data for the wheel strategy's rules (e.g., 30Δ CSPs at 30–45 DTE). Reddit r/thetagang was not fetched.
- No independent (non-vendor) replication of the tastylive 45/21/50 results was retrieved, apart from a SteadyOptions critique of short strangles that was found but not read: [SteadyOptions](https://steadyoptions.com/articles/selling-short-strangles-and-straddles-does-it-work-r516).

## (c) Pitfalls and risk management (tail, gap, assignment, settlement, liquidity, tax, margin)

### Takeaway
The main structural pitfalls are:
- Negatively skewed payoffs: many small wins, rare huge losses.
- Gap and overnight risk, which stops cannot protect against.
- Early assignment and dividend risk on American-style ETF/equity options (SPY).
- Margin expansion during volatility spikes, leading to forced liquidation.
- Rolling or doubling down after losses, which turns defined risk into undefined cumulative risk.

SPX/XSP (European-style, cash-settled, Section 1256 60/40 tax) remove assignment and dividend issues but not tail risk.

### Cited Findings
- **Settlement and exercise style:** SPX and XSP are European-style and cash-settled, with no early exercise. SPY options are American-style and are often exercised early before quarterly ex-dividend dates. If an ITM call's remaining time value is less than the dividend, the holder has an incentive to exercise, and the short call holder may owe the dividend. — [Cboe XSP European-style](https://www.cboe.com/tradable_products/sp_500/mini_spx_options/european_style); [Cboe: Don't Get Stuck Paying the Dividend on Your Short Trade](https://www.cboe.com/insights/posts/dont-get-stuck-paying-the-dividend-on-your-short-trade); [tastylive: dividends risky to option traders](https://www.tastylive.com/news-insights/dividends-risky-to-option-traders)
- **Tax:** broad-based index options such as SPX are Section 1256 contracts. They get 60% long-term / 40% short-term treatment regardless of holding period, are marked to market at year-end, and are reported on Form 6781. SPY options are taxed like stock options. The benefit does not apply inside IRAs. — [Cboe index options tax treatment](https://www.cboe.com/tradable_products/index-options-benefits-tax-treatment/); [Cboe XSP tax benefit](https://www.cboe.com/tradable_products/sp_500/mini_spx_options/tax_benefit/). A worked example of about $10,200 saved on $100k at a 37% bracket comes from a secondary source. — [TradersPost blog](https://blog.traderspost.io/article/index-options-tax-treatment-the-6040-advantage)
- **Margin expansion / forced liquidation:** LJM, Cordier, and Malachite all ended in margin calls or forced liquidation (see section d). OptionSellers clients were left with negative balances owed to the FCM, INTL FCStone. — [ThinkAdvisor](https://thinkadvisor.com/2018/11/21/wiped-out-hedge-fund-manager-confesses-losses-on-youtube)
- **Defined risk is not truly capped once you roll:** Captain Condor's losses compounded by repeatedly closing losing spreads and reopening larger ones (martingale). — [Wikipedia: David Chau](https://en.wikipedia.org/wiki/David_Chau); [stockwirex: How a Zero-Day Options Roll Turns a Loss Into a Wipeout (secondary)](https://stockwirex.com/?p=46388)
- **Execution/pricing risk on 0DTE:** one reported April 2025 case had a realized loss of about $116k, more than 3x the spread's defined max risk, attributed to pricing/fill problems. Unverified secondary account. — [optionstradingiq](https://optionstradingiq.com/?p=37388)
- **Underestimated worst case:** the SEC alleged LJM derived its "20% worst-case daily loss" estimate by doubling its worst historical day (about 9%) and rounding up. — [Seward & Kissel 40 Act blog on SEC/CFTC complaints](https://40actblog.sewkis.com/sec-and-cftc-file-civil-complaints-against-fund-sponsor-and-its-portfolio-managers-and-enter-into-settlement-agreement-with-chief-risk-officer-on-related-alleg)
- **Costs vs edge:** Eifert argues the true risk premium is a small fraction of theta and may be below retail transaction costs. — [Thread Reader](https://threadreaderapp.com/thread/1572019785797603328.html)

### Inferences
- Pin risk mainly affects physically settled products (SPY, single stocks) at expiry. Cash-settled SPX avoids share delivery, though PM-settled SPX still carries close-price uncertainty.
- Bid-ask slippage matters most on wide-strike SPX spreads and in illiquid single-stock options. In stressed 0DTE markets, stop orders can fill far past the stop price.

### Gaps
- I did not retrieve OCC/Cboe primary text on pin risk, or broker data on SPX vs SPY bid-ask spreads.
- Commission impact was not quantified from a primary source.

## (d) Famous blowups

### Takeaway
Every famous blowup shares the same anatomy:
- A short-volatility or short-tail position.
- Leverage or size calibrated on calm history.
- A gap or vol spike: Feb 2018 Volmageddon, the Nov 2018 nat-gas squeeze, Mar 2020 COVID, and a Dec 24 2025 rally for 0DTE condors.
- Margin calls forcing liquidation at the worst prices.

### Cited Findings
- **OptionSellers.com / James Cordier (Nov 2018):**
  - The Tampa firm billed itself as "The Global Authority on Selling Options" and held naked short natural-gas calls.
  - Nat-gas futures spiked about 18% to a 4-year high on Nov 14, 2018, and accounts were liquidated by INTL FCStone.
  - Some clients ended with negative balances. Cordier posted a tearful YouTube apology blaming a "rogue wave".
  - AUM is commonly cited at about $150M, a blog estimate. Client count is about 280–290.
  - Sources: [ThinkAdvisor](https://thinkadvisor.com/2018/11/21/wiped-out-hedge-fund-manager-confesses-losses-on-youtube); [Bloomberg via BloombergQuint](https://www.bloombergquint.com/business/founder-of-stricken-hedge-fund-promoted-selling-of-naked-options); [SteadyOptions](https://steadyoptions.com/articles/james-cordier-another-options-selling-firm-goes-bust-r429); [The Short Bear Substack](https://theshortbear.substack.com/p/blowing-up-selling-options)
- **LJM Preservation & Growth Fund (Feb 2018):**
  - The fund sold OTM puts and calls on S&P futures on margin.
  - Its NAV fell from $9.67 to $4.27 (−55.8%) on Feb 5, 2018. LJM funds lost more than 80%, over $1B, in two trading days.
  - AUM had grown from about $450M (Feb 2016) to about $1.3B (Feb 2018).
  - In 2021 the SEC and CFTC charged managers Anthony Caine and Anish Parvataneni over risk disclosures.
  - Sources: [ai-CIO](https://www.ai-cio.com/news/risky-business-leads-to-1-billion-trading-loss-charges-for-fund-execs/); [Seward & Kissel](https://40actblog.sewkis.com/sec-and-cftc-file-civil-complaints-against-fund-sponsor-and-its-portfolio-managers-and-enter-into-settlement-agreement-with-chief-risk-officer-on-related-alleg); [RCM Alternatives: LJM – The Autopsy](https://www.rcmalternatives.com/?p=25637); [SLCG paper](https://www.slcg.com/files/research-papers/Investors%20Strangled%20by%20LJM%20Preservation%20and%20Growth%20Fund%20(LJMIX).pdf)
- **XIV (Feb 5, 2018):**
  - The inverse VIX ETN lost about 96% (indicative value) in one session.
  - Assets fell from $1.9B to $63M (Bloomberg).
  - Credit Suisse triggered an "acceleration event", because the intraday indicative value fell to 20% or less of the prior close. It redeemed the notes at the Feb 15, 2018 closing indicative value.
  - Sources: [ETF.com](https://www.etf.com/sections/news/inverse-vix-etn-shuts-down); [BloombergQuint: The Day the VIX Doubled](https://www.bloombergquint.com/markets/the-day-the-vix-doubled-tales-of-volmageddon); [CNBC](https://www.cnbc.com/2018/04/12/how-a-volatility-virus-infected-wall-street.html)
- **Malachite Capital (Mar 2020):**
  - A roughly $600M vol fund run by ex-Goldman traders Jacob Weinig and Joe Aiken. It sold downside protection to banks and used leverage.
  - It received margin calls (incl. BNP Paribas) and wound down around Mar 17, 2020.
  - Credit Suisse took a $214M loss. Institutional Investor says the hole left behind was about twice the fund's size.
  - Sources: [Bloomberg](https://www.bloomberg.com/news/articles/2020-03-17/malachite-capital-to-wind-down-funds-amid-market-volatility); [Institutional Investor](https://www.institutionalinvestor.com/article/2bsx55uaovbhxkwutx2io/portfolio/how-to-lose-a-billion-dollars-without-really-trying); [BloombergQuint: Credit Suisse ignored lesson](https://www.bloombergquint.com/markets/credit-suisse-ignored-lesson-from-hedge-fund-hit-before-archegos)
- **"Captain Condor" / David Chau (Dec 24, 2025), the 0DTE blowup widely discussed on X/Reddit:**
  - Large 0DTE SPX iron condors, with sizing increased after losses (martingale).
  - Reportedly lost about $21.6M over three days, then opened about 90,000 (some say 99,000) condors on Dec 24, 2025.
  - The S&P rallied about 2% to a record close through short strikes reported at 7,735/7,740. Total losses were reported at over $50M against about $13M in premium collected.
  - Subscribers reported losing their life savings.
  - Covered by Bloomberg (Jan 11, 2026), MarketWatch, and WSJ (April 2025 profile).
  - Sources: [Bloomberg](https://www.bloomberg.com/news/articles/2026-01-11/-captain-condor-wipeout-offers-harsh-lesson-in-managing-risk); [Wikipedia](https://en.wikipedia.org/wiki/David_Chau); [Option Strategist](https://optionstrategist.com/node/19645); [Yahoo Finance](https://finance.yahoo.com/news/experienced-catastrophic-financial-loss-options-152100134.html). Contract counts and strikes differ across sources.

### Inferences
- LJM's and Cordier's public pitches stressed "preservation" and "selling options like an insurance company". Both had high win rates for years before a single event erased them. This is the textbook "Taleb distribution" pattern.

### Gaps
- Other 0DTE blowups shared on X (individual screenshots) could not be verified. A "$47k lost in an afternoon" anecdote found on a low-quality site was excluded.
- Final investor recovery amounts for OptionSellers and Malachite were not found.

## Critics' view of "high win rate" option selling

### Takeaway
Critics agree that win rate is the wrong metric. What matters is expected value after costs and the size and timing of the loss tail.
- **Taleb's view:** short-tail strategies hide catastrophic risk ("picking up pennies in front of a steamroller").
- **Academic / AQR view:** a genuine risk premium exists, but losses arrive at the worst times.
- **Eifert's view:** blind retail selling underperforms owning equities, and the true premium is a small fraction of theta.

### Cited Findings
- "Taleb distribution": strategies earn steady small profits while hiding catastrophic-loss risk. The "pennies in front of a steamroller" phrase predates Taleb (print citations go back to 1998). — [Wikipedia: Taleb distribution](https://en.wikipedia.org/wiki/Taleb_distribution); [Barry Popik](https://barrypopik.com/blog/picking_up_nickels_in_front_of_a_steamroller)
- AQR-affiliated rebuttal (Ilmanen, 2013 exchange): selling volatility and catastrophe insurance earns higher average returns, consistent with a compensated risk. It concedes that the terrible timing of losses can make it unappealing. — [AQR author response](https://www.aqr.com/Insights/Research/Journal-Article/Do-Financial-Markets-Reward-Buying-or-Selling-Insurance-and-Lottery-Tickets-Author-Response)
- Academic framing: option selling is insurance with asymmetric tail risk. — [arXiv 1409.7720: Risk Premia: Asymmetric Tail Risks and Excess Returns](https://arxiv.org/pdf/1409.7720)
- Larry Swedroe called a short-vol approach "as bad a strategy as I can think of" (headline). — [ETF.com](https://www.etf.com/node/94319.md)
- Eifert's critique is in section (a). — [Thread Reader](https://threadreaderapp.com/thread/1955996656387940647.html)
- Data point against win-rate thinking: a 63% condor win rate in Option Alpha's data coexists with only about 50% of 0DTE users being profitable. — [Option Alpha](https://optionalpha.com/blog/0dte)

### Inferences
- Even the critics accept that a variance risk premium exists. The disagreement is about whether retail sizing, costs, crowding, and leverage leave any of it after a tail event.

### Gaps
- I found no verified Euan Sinclair quote specifically on "win rate". His books emphasize positive-EV trade selection (per a table-of-contents description), which is an inference, not a quote.
