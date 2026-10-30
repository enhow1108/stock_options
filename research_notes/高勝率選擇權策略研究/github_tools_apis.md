# Open-source GitHub projects and data/broker APIs for building an options trading and analysis tool

Method note: GitHub metadata (stars, primary language, `pushed_at` = last push date, license, archived flag) was pulled from the public GitHub REST API (`api.github.com/repos/...` and `/search/repositories`) on 2026-10-31. PyPI latest version and upload date came from `pypi.org/pypi/<pkg>/json` on the same day. "Last push" is the last push to any branch, which is close to but not the same as the last commit on the default branch. The search API hit its unauthenticated rate limit partway through, so some keyword searches ("options screener", "0dte bot", Fubon and Yuanta repos) did not run. Those are listed under Gaps.

## Q1. Options backtesting libraries

### Takeaway
Three projects are active and options-native: **optopsy** (~1.5k stars, AGPL, multi-leg strategy research), **QuantConnect LEAN** (22k stars, Apache-2.0, full event-driven engine with options and broker integrations), and **Lumibot** (2.2k stars, GPL, backtest plus live trading). Several smaller options-only backtesters are also active, including lambdaclass/options_portfolio_backtester, cutebacktests and optionlab. backtrader has stalled since 2024. vectorbt and backtesting.py are fast but have no native options model, so options support would have to be built on top of them.

### Cited Findings
| Project | Stars | Lang | Last push | License | Notes |
|---|---|---|---|---|---|
| goldspanlabs/optopsy (formerly michaelchu/optopsy, now redirects) | 1,508 | Python | 2026-06-30 | AGPL-3.0 | Describes itself as "A nimble options research and backtesting library". PyPI `optopsy` 2.3.0 was uploaded 2026-03-04 |
| QuantConnect/Lean | 22,309 | C# (Python API) | 2026-10-30 | Apache-2.0 | "Lean Algorithmic Trading Engine by QuantConnect (Python, C#)" |
| Lumiwealth/lumibot | 2,187 | Python | 2026-10-30 | GPL-3.0 | "Backtest, paper and live" trading framework, tagged options-trading |
| sirnfs/OptionSuite | 303 | Python | 2026-06-01 | MIT | "Option and stock backtester / live trader" |
| lambdaclass/options_portfolio_backtester | 283 | Python | 2026-10-22 | MIT | "Backtester for evaluating options and equity portfolio strategies over historical data" |
| cutemarkets/cutebacktests | 166 | Python | 2026-05-30 | MIT | "Backtesting framework for modern option strategies" |
| rgaveiga/optionlab | 582 | Python | 2026-09-09 | GPL-3.0 | "A Python library for evaluating option trading strategies" (P/L and probability of profit for a strategy, not a time-series backtester). PyPI 1.9.1 was uploaded 2026-09-09 |
| mementum/backtrader | 23,618 | Python | 2024-08-19 | GPL-3.0 | General backtester. Last push was more than two years ago, and it has no native options/greeks model |
| polakowo/vectorbt | 9,597 | Python | 2026-10-28 | NOASSERTION (Apache-2.0 + Commons Clause per repo) | Vectorized research engine with no options chain model |
| kernc/backtesting.py | 9,164 | Python | 2026-08-05 | AGPL-3.0 | Single-asset OHLC backtester, not options-aware |
| nautechsystems/nautilus_trader | 31,078 | Rust/Python | 2026-10-30 | LGPL-3.0 | Production-grade event-driven engine. It is tagged options-trading |
| philipodonnell/paperbroker | 281 | Python | 2018-04-08 | MIT | Simulated options brokerage. Abandoned |
| m12t/bsm-time-machine | 65 | Jupyter | 2023-10-07 | GPL-3.0 | Black-Scholes-based options backtest simulator. Stale |
| FlashAlpha-lab/flashalpha-fill-simulator | 5 | Python | 2026-08-26 | MIT | "Realistic limit-order fill simulator for options credit/debit spreads". Useful for modeling slippage |
| DuFanYin/optra | 26 | C++ | 2026-10-20 | Apache-2.0 | C++23 options engine for backtest and live (young project) |

Sources: [optopsy](https://github.com/goldspanlabs/optopsy), [LEAN](https://github.com/QuantConnect/Lean), [lumibot](https://github.com/Lumiwealth/lumibot), [OptionSuite](https://github.com/sirnfs/OptionSuite), [options_portfolio_backtester](https://github.com/lambdaclass/options_portfolio_backtester), [cutebacktests](https://github.com/cutemarkets/cutebacktests), [optionlab](https://github.com/rgaveiga/optionlab), [backtrader](https://github.com/mementum/backtrader), [vectorbt](https://github.com/polakowo/vectorbt), [backtesting.py](https://github.com/kernc/backtesting.py), [nautilus_trader](https://github.com/nautechsystems/nautilus_trader), [paperbroker](https://github.com/philipodonnell/paperbroker), [bsm-time-machine](https://github.com/m12t/bsm-time-machine), [fill-simulator](https://github.com/FlashAlpha-lab/flashalpha-fill-simulator), [optra](https://github.com/DuFanYin/optra), [PyPI optopsy](https://pypi.org/project/optopsy/), [PyPI optionlab](https://pypi.org/project/optionlab/)

- The GitHub topic `options-backtesting` is nearly empty: only three repos, all with 0–1 stars. Most real projects tag `options-trading` instead — [GitHub search topic:options-backtesting](https://github.com/topics/options-backtesting)
- The `topic:options-trading` leaders by stars are nautilus_trader (31k), je-suis-tm/quant-trading (11.2k, strategy collection), lumibot (2.2k), robin_stocks (2.1k, Robinhood wrapper, last push 2026-02-11), jasonstrimpel/volatility-trading (2.0k, volatility estimators, last push 2024-10-21) and optopsy (1.5k) — [GitHub topic options-trading](https://github.com/topics/options-trading)

### Inferences
- For iron condor and credit spread research on historical chains, optopsy is the most direct fit. Its AGPL license matters if the tool is ever offered as a network service. LEAN is the strongest choice if the same code must also run live, but it brings a heavy C# runtime and is built around QuantConnect's data formats.
- None of these libraries ships options data. Every serious backtest still needs a historical chain source (see Q4: ThetaData, ORATS, Massive).
- Fill and slippage modeling for multi-leg orders is a weak spot almost everywhere. The small fill-simulator project shows a gap that remains open.

### Gaps
- I did not verify whether vectorbt PRO (the paid version) has options features. The open-source repo has no options support.
- I did not verify the depth of options support inside LEAN (e.g. `OptionStrategies.IronCondor` helpers, index options, 0DTE data) from docs in this pass.
- "backtrader option extensions": no well-maintained public extension surfaced in searches.

## Q2. Pricing and greeks libraries

### Takeaway
QuantLib (C++ with SWIG Python bindings, PyPI 1.44 from Oct 2026) is the actively maintained heavyweight. py_vollib was revived (PyPI 1.0.12 in June 2026) and is the standard lightweight Black-Scholes/IV library. py_vollib_vectorized, mibian and opstrat work but are stale.

### Cited Findings
| Project | Stars | Lang | Last push | License | PyPI latest | Notes |
|---|---|---|---|---|---|---|
| lballabio/QuantLib | 7,724 | C++ | 2026-10-30 | BSD-style (NOASSERTION on GitHub; PyPI says BSD-3-Clause) | QuantLib 1.44 (2026-10-13) | Full derivatives library (American options, vol surfaces) |
| lballabio/QuantLib-SWIG | 402 | SWIG | 2026-10-28 | same | — | Python wrappers. Steep learning curve |
| vollib/py_vollib | 444 | Python | 2026-05-29 | MIT | 1.0.12 (2026-06-01) | Black, Black-Scholes, BSM pricing, IV and greeks |
| marcdemers/py_vollib_vectorized | 162 | Python | 2024-12-02 | MIT | 0.1.1 (2021-02-28) | numpy/pandas vectorized wrapper of py_vollib. No PyPI release since 2021 |
| yassinemaaroufi/MibianLib | 290 | Python | 2021-06-14 | none on GitHub (PyPI says GPL) | 0.1.3 (2016) | Simple BS/Garman-Kohlhagen. Abandoned |
| hashABCD/opstrat | 169 | Python | 2024-01-11 | MIT | 0.1.7 (2021) | Payoff diagram plotting only |
| rgaveiga/optionlab | 582 | Python | 2026-09-09 | GPL-3.0 | 1.9.1 (2026-09-09) | Strategy P/L, probability of profit, greeks for multi-leg |
| jkirkby3/fypy | 149 | Python | 2025-02-27 | MIT | — | Vanilla/exotic pricing for quant R&D |
| Open-Lemma/options-implied-probability | 354 | Python | 2026-04-29 | Apache-2.0 | — | Implied probability distribution from option prices |
| mcdallas/wallstreet | 1,718 | Python | 2024-07-06 | MIT | — | Real-time stock and option data with BS greeks (scrapes free sources). Stale |

Sources: [QuantLib](https://github.com/lballabio/QuantLib), [QuantLib-SWIG](https://github.com/lballabio/QuantLib-SWIG), [PyPI QuantLib](https://pypi.org/project/QuantLib/), [py_vollib](https://github.com/vollib/py_vollib), [PyPI py_vollib](https://pypi.org/project/py_vollib/), [py_vollib_vectorized](https://github.com/marcdemers/py_vollib_vectorized), [MibianLib](https://github.com/yassinemaaroufi/MibianLib), [PyPI mibian](https://pypi.org/project/mibian/), [opstrat](https://github.com/hashABCD/opstrat), [optionlab](https://github.com/rgaveiga/optionlab), [fypy](https://github.com/jkirkby3/fypy), [OIPD](https://github.com/Open-Lemma/options-implied-probability), [wallstreet](https://github.com/mcdallas/wallstreet)

- The repo `vollib/py_vollib_vectorized` does not exist (404). The vectorized fork lives at `marcdemers/py_vollib_vectorized` — [GitHub API](https://api.github.com/repos/marcdemers/py_vollib_vectorized)

### Inferences
- A practical stack is py_vollib (or a small numpy Black-Scholes) for fast greeks and IV on screening, QuantLib only where American exercise or a vol surface is needed, and optionlab for probability of profit on spreads and iron condors.
- European-style index options (SPX, TAIFEX TXO) price fine with plain Black-Scholes/Black-76, so QuantLib is optional for the user's main use cases.

### Gaps
- I did not benchmark speed or accuracy across the libraries.

## Q3. Screeners and bots (credit spreads, wheel, 0DTE)

### Takeaway
This category is fragmented. Almost every credit spread, wheel or 0DTE bot on GitHub has under 100 stars, and many are 2025–2026 "AI agent" projects with little track record. The higher-signal active ones are GEX dashboards (EzOptions-Schwab, gex-terminal), MEICAgent for 0DTE iron condors on tastytrade, and income-desk. Expect to write your own screener on top of a broker or data API.

### Cited Findings
| Project | Stars | Lang | Last push | License | Focus |
|---|---|---|---|---|---|
| stonkyoloer/News_Spread_Engine | 196 | Python | 2025-10-04 | none | Screens event catalysts to build credit spread plans |
| calesthio/OptionsCanvas | 72 | Python | 2026-05-28 | NOASSERTION | 0DTE tool with client-side SL/TP that never touches the broker |
| EazyDuz1t/EzOptions-Schwab | 45 | Python | 2026-10-11 | GPL-3.0 | Real-time GEX/DEX/vanna/charm dashboard on the Schwab API |
| zrack/gex-terminal | 26 | Python | 2026-10-20 | MIT | Intraday gamma exposure TUI |
| cobriensr/Options-Strike-Calculator | 22 | TypeScript | 2026-10-30 | AGPL-3.0 | 0DTE SPX strike, iron condor and BWB calculator |
| sbauwow/schwagent | 27 | Python | 2026-09-25 | MIT | AI trading agent on Schwab with options, iron condor and wheel |
| nitinblue/income-desk | 18 | Python | 2026-10-30 | MIT | Systematic options income for small accounts |
| joncovington/MEICAgent | 7 | Python | 2026-07-11 | MIT | Multiple-Entry Iron Condor 0DTE agent via tastytrade |
| FlashAlpha-lab/0dte-options-analytics | 13 | Python | 2026-08-26 | MIT | Pin risk, gamma regime, expected move |
| Marfusios/premium-tracker | 15 | TypeScript | 2025-08-19 | none | IBKR statement tracker for option sellers |
| CryptoGnome/WheelForge, vahagn-madatyan/wheel-it | 6 / 4 | Python | 2025-08 / 2026-05 | Apache-2.0 | Wheel strategy algo templates (Alpaca-style) |
| SaltyMeat23/ThetaBot | 3 | Python | 2026-09-23 | MIT | Wheel bot for Robinhood |
| staskh/trading_skills | 397 | Python | 2026-10-30 | MIT | "Claude powered advisor system for option traders" |
| mcf-long-short/ibkr-options-volatility-trading | 376 | Python | 2025-01-23 | MIT | Straddle volatility trading on IBKR |
| henrawrrr/ThetaGangCSScreener | 2 | Python | 2021-09-14 | none | Credit spread chain screener. Abandoned |

Sources: [News_Spread_Engine](https://github.com/stonkyoloer/News_Spread_Engine), [OptionsCanvas](https://github.com/calesthio/OptionsCanvas), [EzOptions-Schwab](https://github.com/EazyDuz1t/EzOptions-Schwab), [gex-terminal](https://github.com/zrack/gex-terminal), [Options-Strike-Calculator](https://github.com/cobriensr/Options-Strike-Calculator), [schwagent](https://github.com/sbauwow/schwagent), [income-desk](https://github.com/nitinblue/income-desk), [MEICAgent](https://github.com/joncovington/MEICAgent), [0dte-options-analytics](https://github.com/FlashAlpha-lab/0dte-options-analytics), [premium-tracker](https://github.com/Marfusios/premium-tracker), [WheelForge](https://github.com/CryptoGnome/WheelForge), [wheel-it](https://github.com/vahagn-madatyan/wheel-it), [ThetaBot](https://github.com/SaltyMeat23/ThetaBot), [trading_skills](https://github.com/staskh/trading_skills), [ibkr-options-volatility-trading](https://github.com/mcf-long-short/ibkr-options-volatility-trading), [ThetaGangCSScreener](https://github.com/henrawrrr/ThetaGangCSScreener). Topic searches: [iron-condor](https://github.com/topics/iron-condor), [credit-spread](https://github.com/topics/credit-spread), [0dte](https://github.com/topics/0dte), [wheel-strategy](https://github.com/topics/wheel-strategy)

### Inferences
- No dominant, well-maintained open-source credit spread screener exists. Treat these repos as reference code for broker integration patterns, not as dependencies.
- Many recent repos are LLM/MCP "agent" wrappers. Low star counts and short histories mean their reliability is unproven. Avoid letting them place live orders without your own risk checks.

### Gaps
- The GitHub search for "options screener", "0dte bot" and "options-strategies" topics hit the rate limit and did not run, so other mid-sized projects may have been missed.

## Q4. Data and broker APIs (chains, greeks, multi-leg orders)

### Takeaway
For order placement with multi-leg spreads, the main options are IBKR (ib_async), Schwab (schwab-py), tastytrade (unofficial `tastytrade` SDK) and Tradier. Alpaca supports options up to Level 3 spreads. For historical chain data for backtesting, ThetaData ($40–160/month, 6–14 years), Massive (formerly Polygon, free to $199/month, 2–5+ years) and ORATS ($199–899/month, EOD back to 2007) are the main paid sources. yfinance only gives current-snapshot chains.

### Cited Findings
**SDK repos**
| SDK | Stars | Last push | License | PyPI latest | Notes |
|---|---|---|---|---|---|
| ib-api-reloaded/ib_async | 1,778 | 2026-10-29 | BSD-2 | 2.1.0 (2025-12-08) | "Python sync/async framework for Interactive Brokers API (replaces ib_insync)" |
| erdewit/ib_insync | 3,282 | 2024-03-14 | BSD-2 | — | **Archived** (archived=True). Use ib_async instead |
| alexgolec/schwab-py | 480 | 2026-08-26 | MIT | 1.5.1 (2025-06-30) | Unofficial Schwab wrapper |
| tastyware/tastytrade | 259 | 2026-08-07 | MIT | 13.2.3 (2026-08-07) | "unofficial, typed, asynchronous Python SDK" |
| tastytrade/tastytrade-sdk-python (official) | 106 | 2026-03-13 | MIT | — | **Archived** |
| tastyware/tastytrade-cli | 79 | 2026-08-10 | MIT | — | CLI on top of the SDK |
| alpacahq/alpaca-py | 1,570 | 2026-10-30 | Apache-2.0 | 0.44.0 (2026-08-11) | Official SDK |
| massive-com/client-python (redirect from polygon-io/client-python) | 1,524 | 2026-10-26 | MIT | `massive` 2.9.1 (2026-10-26). Legacy `polygon-api-client` 1.16.3 (2025-10-30) | Official Massive.com client |
| ranaroussi/yfinance | 25,758 | 2026-10-29 | Apache-2.0 | 1.7.0 (2026-08-26) | Unofficial Yahoo scraper |
| baileydanseglio/thetadata-python | 69 | 2024-06-27 | MIT | — | **Archived** |
| PyPI `thetadata` | — | — | — | 1.0.17 (2026-10-30) | Current ThetaData Python package |
| PyPI `tradier-python` | — | — | MIT | 0.1.3 (2021-11-07) | Stale third-party wrapper. Call Tradier REST directly |

Sources: [ib_async](https://github.com/ib-api-reloaded/ib_async), [ib_insync](https://github.com/erdewit/ib_insync), [schwab-py](https://github.com/alexgolec/schwab-py), [tastyware/tastytrade](https://github.com/tastyware/tastytrade), [official tastytrade SDK](https://github.com/tastytrade/tastytrade-sdk-python), [tastytrade-cli](https://github.com/tastyware/tastytrade-cli), [alpaca-py](https://github.com/alpacahq/alpaca-py), [massive client-python](https://github.com/massive-com/client-python), [yfinance](https://github.com/ranaroussi/yfinance), [thetadata-python](https://github.com/baileydanseglio/thetadata-python), PyPI JSON for [thetadata](https://pypi.org/project/thetadata/), [tradier-python](https://pypi.org/project/tradier-python/), [polygon-api-client](https://pypi.org/project/polygon-api-client/), [massive](https://pypi.org/project/massive/)

**Pricing and capabilities**
- **ThetaData**: Options Value $40/month (6 years history), Standard $80/month (10 years), Pro $160/month (14 years). The pricing page shows no free tier and does not mention greeks — [ThetaData pricing](https://www.thetadata.net/pricing)
- **Massive (formerly Polygon.io)**: Options Basic $0 (2 years, end-of-day, 5 calls/min). Starter $29 (2 years, 15-min delayed, greeks/IV, flat files, websockets). Developer $79 (4 years, adds trades). Advanced $199 (5+ years, real-time, adds quotes). All paid plans are for non-professional individual use only — [Massive options](https://massive.com/options). The `polygon-io/client-python` repo now redirects to `massive-com/client-python` — [GitHub](https://github.com/massive-com/client-python)
- **ORATS Data API**: Delayed $199/month, Live $299, Live Intraday $599, All-In $899. EOD history back to 2007. 1-minute intraday back to August 2020 (the same page also says October 2020 for the Intraday Backtester add-on, an internal inconsistency). Greeks and IV-rank endpoints are included — [ORATS Data API](https://orats.com/data-api)
- **Tradier**: The brokerage API supports "Equity, option, multileg, and combo orders, plus OCO, OTO, and OTOCO" with order preview. The page uses a four-leg spread as an example, but no maximum leg count was stated. Market data includes option chains with greeks — [Tradier multileg docs](https://docs.tradier.com/reference/brokerage-api-trading-place-multileg-order)
- **tastytrade Open API**: REST/JSON, "option chains with Greeks", IV rank, complex orders (OTO/OCO/OTOCO) across equities, options, futures and crypto. It also publishes an open-source MCP server — [tastytrade developer](https://developer.tastytrade.com/)
- **Alpaca**: Options trading is live. Level 1 covers covered calls and cash-secured puts, Level 2 long calls and puts, and Level 3 spreads (call and put spreads). Stop and stop-limit orders are single-leg only. Real-time and historical option data are offered — [Alpaca options docs](https://docs.alpaca.markets/docs/options-trading)
- **Schwab via schwab-py**: Option chains, an options order template module, and streaming (level one quotes, level two book, account activity). Requires creating a Schwab developer app. Token lifetimes are short. It is unofficial and not affiliated with Schwab — [schwab-py docs](https://schwab-py.readthedocs.io/en/latest/). developer.schwab.com returned 403 to automated fetch.
- **IBKR market data**: The OPRA top-of-book non-professional fee was not confirmed from an official page. A third-party blog says $1.50/month, waived at $20+/month in commissions ([dev.to](https://dev.to/xqliu/interactive-brokers-market-data-subscription-which-one-do-i-actually-need-in-2026-164g)). An IBKR KB snippet mentions USD 4.50/month for OPRA top of book without specifying the tier ([IBKR KB](https://ibkb.interactivebrokers.com/fr/node/2840)). OPRA's own pass-through non-pro fee is about $1.25/user/month ([ThetaData OPRA guide](https://thetadata.net/articles/2026-05-29-opra-fee-guide-for-options-market-data))

### Inferences
- **The best fit for multi-leg live trading from Python today:**
  - IBKR via ib_async: broadest product coverage including SPX, plus combo/BAG orders, but you must run TWS or Gateway.
  - tastytrade via tastyware/tastytrade: async and typed, built for an options-centric broker, but the official SDK is archived, so you rely on the community package.
  - Schwab via schwab-py.
- **Cheapest viable historical chain data:** Massive Starter ($29) for about 2 years, or ThetaData Value ($40) for 6 years. ORATS is the premium choice for smoothed IV/greeks and long EOD history.
- **yfinance:** usable only for prototyping current-chain screens. It gives no historical chains and is an unofficial scraper.

### Gaps
- **CBOE DataShop pricing and datasets:** not fetched in this pass.
- **Alpaca details:** whether Alpaca supports index options (SPX) and four-leg mleg orders (iron condors) was not stated on the page fetched.
- **Schwab rules:** Schwab's exact developer approval process and refresh-token lifetime were not verified (fetch blocked).
- **ThetaData greeks:** whether ThetaData's Value tier includes greeks is not stated on the pricing page.

## Q5. Taiwan (TAIFEX 台指選擇權) options APIs and data

### Takeaway
永豐金 **Shioaji** is the most developer-friendly TAIFEX option API. It is actively maintained (PyPI 1.7.10 on 2026-10-29), has a simulation mode, option chain contracts, tick and K-bar history, and native **2-leg combo orders** (price spreads, straddles, strangles, time spreads, conversion/reversal). That means an iron condor has to be sent as two vertical-spread combo orders. 富邦 **Fubon Neo** (`fubon_neo` 2.3.1, 2026-10-16) is the main alternative. TAIFEX's own OpenAPI returns only the latest trading day.

### Cited Findings
- Sinotrade/Shioaji: 528 stars, last push 2026-10-29, no license field. This repo mainly hosts issues and Docker, and the SDK is distributed on PyPI as `shioaji` 1.7.10 (2026-10-29) — [GitHub](https://github.com/Sinotrade/Shioaji), [PyPI](https://pypi.org/project/shioaji/)
- Sinotrade/shioaji-pro-app: 401 stars, TypeScript, AGPL-3.0, last push 2026-10-27. It is a "professional trading terminal for Taiwan markets (TWSE/TPEX/TAIFEX)" — [GitHub](https://github.com/Sinotrade/shioaji-pro-app)
- **Shioaji combo contracts:** `api.contracts.combo()` builds a ComboContract from two legs. Supported option combo types are TimeSpread, PriceSpread (call spread with legs ordered high strike then low; put spread ordered low strike then high), Straddle, Strangle and ConversionReversal. Straddle and ConversionReversal require an explicit combo_type — [Shioaji docs (llms-full.txt)](https://sinotrade.github.io/llms-full.txt)
- **Shioaji ComboOrder:** orders take a net price. The docs example notes that standard option combos cannot use ROD and use IOC instead ("標準選擇權組合不可用 ROD"). The native exchange combo code is "選擇權組合暫不提供" (not yet provided for option combos) — [Shioaji docs](https://sinotrade.github.io/llms-full.txt)
- **Shioaji other features:** a simulation mode (`sj.Shioaji(simulation=True)`); historical data as Ticks and Kbars, subject to daily traffic limits; option contracts queried by root (e.g. TXO), with filters for strike and call/put — [Shioaji docs](https://sinotrade.github.io/llms-full.txt), [Shioaji site](https://sinotrade.github.io/)
- **Fubon Neo:** the SDK is distributed as `fubon_neo` wheels (latest 2.3.1, 2026-10-16). A community MCP server documents API-key login (`apikey_login`) and futures/options market data modules. I did not confirm combo (複式單) order support because the official doc page returned 403 — [PyPI fubon_neo](https://pypi.org/project/fubon-neo/), [fubon-api-mcp-server wiki](https://github.com/Mofesto/fubon-api-mcp-server/wiki), [vocus article](https://www.vocus.cc/article/672d8492fd89780001fdd134)
- **TAIFEX OpenAPI** (openapi.taifex.com.tw): a third-party project reports that all 135 endpoints return only the latest trading day. Historical daily options data must be downloaded from the taifex.com.tw download pages, which support date ranges but cap each query. The official FAQ says historical databases must be requested through a paid application — [TWSEMCPServer release notes](https://github.com/twjackysu/TWSEMCPServer/releases/tag/v1.7.0), [TAIFEX FAQ](https://www.taifex.com.tw/cht/9/tradersQAIS), [data.gov.tw dataset](https://data.gov.tw/dataset/11600)
- **Related Taiwan repos:**
  - twjackysu/TWSEMCPServer: 180 stars, MIT, last push 2026-10-22. MCP server over the TWSE/TPEx/TAIFEX OpenAPIs.
  - catcat222222/twchips: 74 stars, MIT, last push 2026-08-16. TAIFEX daily quotes and institutional positions.
  - Yvictor/IVtws: 95 stars, last push 2016. TAIFEX quote crawler with real-time IV calculation. Abandoned.
  - Sources: [TWSEMCPServer](https://github.com/twjackysu/TWSEMCPServer), [twchips](https://github.com/catcat222222/twchips), [IVtws](https://github.com/Yvictor/IVtws)
- **PyPI `pytaifex`:** a TAIFEX-related package exists — [PyPI pytaifex](https://pypi.org/project/pytaifex/)

### Inferences
- **For a Taiwan user trading TXO:** Shioaji is the best documented choice for automation, with simulation, an option chain and native 2-leg spread orders. A TXO iron condor equals a put PriceSpread plus a call PriceSpread, sent as two combo orders. With IOC, one side can fill and the other miss, so the tool needs leg-risk handling.
- **Greeks for TXO:** neither Shioaji nor the TAIFEX OpenAPI was found to provide greeks. Compute them locally with py_vollib's Black-76 against the TX futures price.
- **TXO backtesting data:** history has to be assembled from TAIFEX daily downloads, Shioaji tick and K-bar history (traffic-limited), or a paid TAIFEX historical data application.

### Gaps
- **Fubon Neo combo orders:** whether it supports option combo orders, and its exact functions, is unconfirmed (official docs page returned 403).
- **元大 (Yuanta) API:** not researched. The GitHub search hit the rate limit and no web search was run.
- **Shioaji history depth:** the history depth for TXO option ticks and K-bars, and the exact daily traffic limits, were not extracted.
- **Licenses:** Shioaji's license terms (no SPDX on GitHub) were not determined.
