#!/usr/bin/env python3
"""SPX / XSP 信用價差每日篩選器（只用標準庫）。

資料：Cboe 延遲報價（選擇權鏈含 bid/ask/IV/Greeks）、SPX 與 VIX 歷史。
輸出：docs/data/latest.json 與 docs/data/history/<日期>.json，供 GitHub Pages 頁面讀取。

這是依使用者自訂規則的篩選結果，不是投資建議。
"""
import json
import math
import re
import sys
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "data"
UA = {"User-Agent": "Mozilla/5.0 (spx-spread-screener)"}
CHAIN_URL = "https://cdn.cboe.com/api/global/delayed_quotes/options/_{}.json"
SPX_HIST_URL = "https://cdn.cboe.com/api/global/delayed_quotes/charts/historical/_SPX.json"
VIX_HIST_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
SYMBOL_RE = re.compile(r"^([A-Z]+)(\d{6})([CP])(\d{8})$")
MULT = 100


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


# ---------- 市場背景 ----------

def market_context(chain_meta, spx):
    closes = [float(x["close"]) for x in spx[-21:]]
    rets = [math.log(closes[i] / closes[i - 1]) for i in range(1, len(closes))]
    mean = sum(rets) / len(rets)
    rv20 = math.sqrt(sum((r - mean) ** 2 for r in rets) / (len(rets) - 1) * 252)

    rows = fetch(VIX_HIST_URL).decode().strip().splitlines()[1:]
    vix = [float(r.split(",")[4]) for r in rows[-252:]]
    cur = vix[-1]
    lo, hi = min(vix), max(vix)
    return {
        "spx": chain_meta["current_price"],
        "spx_change_pct": chain_meta.get("price_change_percent"),
        "iv30": chain_meta.get("iv30"),
        "vix": cur,
        "vix_date": rows[-1].split(",")[0],
        "vix_rank_1y": (cur - lo) / (hi - lo) if hi > lo else None,
        "vix_percentile_1y": sum(v < cur for v in vix) / len(vix),
        "rv20": rv20,
        "vrp_proxy": cur / 100 - rv20,
    }


# ---------- 選擇權鏈 ----------

def load_chain(symbol, root):
    d = json.loads(fetch(CHAIN_URL.format(symbol)))["data"]
    asof = datetime.fromisoformat(d["last_trade_time"]).date()
    expiries = {}
    for o in d["options"]:
        m = SYMBOL_RE.match(o["option"])
        # SPX 只用 SPXW（PM 結算），避開 AM 結算的月選開盤結算風險
        if not m or m.group(1) != root:
            continue
        exp = datetime.strptime(m.group(2), "%y%m%d").date()
        strike = int(m.group(4)) / 1000
        expiries.setdefault(exp, {"C": {}, "P": {}})[m.group(3)][strike] = o
    return d, asof, expiries


def mid(q):
    return (q["bid"] + q["ask"]) / 2


def leg_ok(q, cfg):
    if not q or q["bid"] <= 0 or q["ask"] <= 0 or q["ask"] < q["bid"]:
        return False
    return q["ask"] - q["bid"] <= max(cfg["max_leg_spread_abs"], cfg["max_leg_spread_pct"] * mid(q))


def atm_iv(book, fwd):
    ks = sorted(set(book["C"]) & set(book["P"]), key=lambda k: abs(k - fwd))
    for k in ks[:5]:
        c, p = book["C"][k], book["P"][k]
        if c["iv"] > 0 and p["iv"] > 0:
            return (c["iv"] + p["iv"]) / 2
    return None


def pick_short(side, target, cfg):
    best = None
    for k, q in side.items():
        if k % cfg["strike_multiple"] or not leg_ok(q, cfg) or not q.get("delta"):
            continue
        err = abs(abs(q["delta"]) - target)
        if best is None or err < best[0]:
            best = (err, k)
    return best[1] if best and best[0] < 0.03 else None


# ---------- 到期分佈與統計（與 docs/calculator/engine.js 相同的方法） ----------

def terminal_grid(S, T, mu, q, sigma, model, nu, n=4001):
    Z = 30.0 if model == "t" else 10.0
    dz = 2 * Z / (n - 1)
    c = math.sqrt((nu - 2) / nu) if model == "t" else 1.0
    s = sigma * math.sqrt(T)
    zs, ws = [], []
    for i in range(n):
        z = -Z + i * dz
        p = (1 + (z / c) ** 2 / nu) ** (-(nu + 1) / 2) if model == "t" else math.exp(-0.5 * z * z)
        zs.append(z)
        ws.append(p)
    sw = sum(ws)
    ws = [w / sw for w in ws]
    mgf = sum(w * math.exp(s * z) for w, z in zip(ws, zs))
    m0 = math.log(S) + (mu - q) * T - math.log(mgf)
    return [math.exp(m0 + s * z) for z in zs], ws


def historical_grid(S, closes, dte):
    """SPX 歷史上所有「相同交易日數」的實際 log 報酬（重疊視窗），等權重，不做任何模型假設。"""
    h = max(1, round(dte * 252 / 365))
    rets = [math.log(closes[i + h] / closes[i]) for i in range(len(closes) - h)]
    w = 1 / len(rets)
    return [S * math.exp(r) for r in rets], [w] * len(rets)


def intrinsic(t, S, K):
    return max(S - K, 0.0) if t == "C" else max(K - S, 0.0)


def evaluate(legs, credit, cost, max_loss, grid):
    ST, w = grid
    pnl = []
    ev = p_win = s_win = s_loss = p_max = 0.0
    tol = max_loss * 0.99
    for x, wi in zip(ST, w):
        v = (credit + sum(l["qty"] * intrinsic(l["type"], x, l["strike"]) for l in legs)) * MULT - cost
        pnl.append((v, wi))
        ev += wi * v
        if v > 0:
            p_win += wi
            s_win += wi * v
        else:
            s_loss += wi * v
        if v <= -tol:
            p_max += wi
    pnl.sort()
    acc = tail = 0.0
    for v, wi in pnl:
        take = min(wi, 0.05 - acc)
        if take <= 0:
            break
        tail += take * v
        acc += take
    avg_win = s_win / p_win if p_win else 0.0
    avg_loss = s_loss / (1 - p_win) if p_win < 1 else 0.0
    return {
        "ev": ev,
        "pop": p_win,
        "avg_win": avg_win,
        "avg_loss": avg_loss,
        "p_max_loss": p_max,
        "cvar5": tail / 0.05,
        "be_win_rate": -avg_loss / (avg_win - avg_loss) if avg_win - avg_loss > 0 else None,
    }


# ---------- 組合建構 ----------

def vertical(book, opt_type, target, width, cfg):
    side = book[opt_type]
    ks = pick_short(side, target, cfg)
    if ks is None:
        return None, "找不到符合 delta 的 short 腳"
    kl = ks - width if opt_type == "P" else ks + width
    s, l = side.get(ks), side.get(kl)
    if not leg_ok(l, cfg):
        return None, "long 腳不存在或流動性不足"
    if s.get("open_interest", 0) < cfg["min_short_open_interest"]:
        return None, "short 腳未平倉量太低"
    return [
        {"type": opt_type, "strike": ks, "qty": -1, "q": s},
        {"type": opt_type, "strike": kl, "qty": 1, "q": l},
    ], None


def price_combo(legs, cfg):
    credit_mid = -sum(l["qty"] * mid(l["q"]) for l in legs)
    # natural：賣在 bid、買在 ask
    credit_nat = sum(l["q"]["bid"] for l in legs if l["qty"] < 0) - sum(l["q"]["ask"] for l in legs if l["qty"] > 0)
    fill = credit_mid - cfg["fill_haircut"] * (credit_mid - credit_nat)
    return credit_mid, credit_nat, fill


def build_candidates(und, S, expiries, asof, closes, cfg, rejects):
    out = []
    for exp, book in sorted(expiries.items()):
        dte = (exp - asof).days
        if not cfg["dte_min"] <= dte <= cfg["dte_max"]:
            continue
        T = dte / 365
        fwd = S * math.exp((cfg["rate"] - cfg["div_yield"]) * T)
        iv = atm_iv(book, fwd)
        if not iv:
            continue
        rv = iv * cfg["real_vol_ratio"]
        grid_base = terminal_grid(S, T, cfg["mu"], cfg["div_yield"], rv, cfg["model"], cfg["nu"])
        grid_hist = historical_grid(S, closes, dte)

        for delta in cfg["short_deltas"]:
            for width in cfg["widths"]:
                verts = {}
                for t in ("P", "C"):
                    legs, why = vertical(book, t, delta, width, cfg)
                    verts[t] = legs
                    if why:
                        rejects[why] = rejects.get(why, 0) + 1
                combos = []
                if "bull_put" in cfg["strategies"] and verts["P"]:
                    combos.append(("bull_put", verts["P"]))
                if "bear_call" in cfg["strategies"] and verts["C"]:
                    combos.append(("bear_call", verts["C"]))
                if "iron_condor" in cfg["strategies"] and verts["P"] and verts["C"]:
                    combos.append(("iron_condor", verts["P"] + verts["C"]))

                for name, legs in combos:
                    c_mid, c_nat, fill = price_combo(legs, cfg)
                    if fill / width < cfg["min_credit_to_width"]:
                        rejects["權利金/寬度太低"] = rejects.get("權利金/寬度太低", 0) + 1
                        continue
                    cost = cfg["commission_per_contract"] * len(legs)
                    max_loss = (width - fill) * MULT + cost
                    base = evaluate(legs, fill, cost, max_loss, grid_base)
                    hist = evaluate(legs, fill, cost, max_loss, grid_hist)
                    shorts = [l for l in legs if l["qty"] < 0]
                    out.append({
                        "underlying": und,
                        "strategy": name,
                        "expiry": exp.isoformat(),
                        "dte": dte,
                        "target_delta": delta,
                        "width": width,
                        "legs": [{
                            "type": l["type"], "strike": l["strike"], "qty": l["qty"],
                            "bid": l["q"]["bid"], "ask": l["q"]["ask"], "iv": l["q"]["iv"],
                            "delta": l["q"]["delta"], "oi": l["q"].get("open_interest", 0),
                        } for l in legs],
                        "short_deltas": [round(abs(l["q"]["delta"]), 3) for l in shorts],
                        "credit_mid": round(c_mid, 2),
                        "credit_natural": round(c_nat, 2),
                        "credit_fill": round(fill, 2),
                        "max_profit": round(fill * MULT - cost, 2),
                        "max_loss": round(max_loss, 2),
                        "credit_to_width": round(fill / width, 3),
                        "breakeven_win_rate_fixed": round(max_loss / (max_loss + fill * MULT - cost), 4),
                        "atm_iv": round(iv, 4),
                        "real_vol": round(rv, 4),
                        "base": {k: (round(v, 4) if isinstance(v, float) else v) for k, v in base.items()},
                        "historical": {k: (round(v, 4) if isinstance(v, float) else v) for k, v in hist.items()},
                        "ev_per_risk": round(base["ev"] / max_loss, 4),
                        "ev_per_risk_hist": round(hist["ev"] / max_loss, 4),
                        # 排序用：兩種分佈中較差者，避免只靠單一假設
                        "score": round(min(base["ev"], hist["ev"]) / max_loss, 4),
                    })
    return out


def top_per_strategy(cands, n):
    """每個標的的每種策略各取前 n 名，方便比較（例如 iron condor 為何排在 bull put 後面）。"""
    seen = {}
    out = []
    for c in cands:
        key = (c["underlying"], c["strategy"])
        if seen.get(key, 0) < n:
            seen[key] = seen.get(key, 0) + 1
            out.append(c)
    return out


def main():
    cfg_path = ROOT / "screener" / "config.json"
    cfg = json.loads(cfg_path.read_text())
    spx = json.loads(fetch(SPX_HIST_URL))["data"]
    closes = [float(x["close"]) for x in spx if float(x["close"]) > 0]

    cands, counts, prices, mkt, asof, quote_time = [], {}, {}, None, None, ""
    for und, ucfg in cfg["underlyings"].items():
        meta, und_asof, expiries = load_chain(und, ucfg["root"])
        if mkt is None:
            mkt = market_context(meta, spx) if und == "SPX" else None
        asof = max(asof, und_asof) if asof else und_asof
        quote_time = max(quote_time, meta["last_trade_time"])
        prices[und] = meta["current_price"]
        merged = dict(cfg, **ucfg)
        rejects = {}
        # 歷史情境用 SPX 報酬率；XSP 是 SPX 的 1/10，報酬率相同
        found = build_candidates(und, meta["current_price"], expiries, und_asof, closes, merged, rejects)
        counts[und] = {"candidates": len(found), "rejected": rejects}
        cands += found
    if mkt is None:
        raise SystemExit("config.json 的 underlyings 需要包含 SPX（市場背景資料來源）")
    mkt["history_start"] = spx[0]["date"]
    mkt["underlyings"] = prices
    cands.sort(key=lambda c: c["score"], reverse=True)

    report = {
        "asof": asof.isoformat(),
        # Cboe 最後報價時間（美東時間，延遲約 15 分鐘）
        "quote_time": quote_time,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "Cboe delayed quotes",
        "disclaimer": "依自訂規則的模型篩選結果，僅供教育研究，不是投資建議。",
        "config": {k: v for k, v in cfg.items() if not k.startswith("_")},
        "market": mkt,
        "counts": counts,
        "candidates": top_per_strategy(cands, cfg["top_n_per_strategy"]),
    }

    # 報價時間沒變（休市、盤後重跑）就不改檔案，避免產生沒有內容的 commit
    latest = OUT / "latest.json"
    if latest.exists():
        try:
            if json.loads(latest.read_text()).get("quote_time") == quote_time:
                print(f"報價時間 {quote_time} 未變動，略過寫檔")
                return 0
        except ValueError:
            pass

    hist = OUT / "history"
    hist.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, ensure_ascii=False, indent=1)
    (OUT / "latest.json").write_text(text)
    (hist / f"{report['asof']}.json").write_text(text)
    days = sorted((p.stem for p in hist.glob("????-??-??.json")), reverse=True)
    (hist / "index.json").write_text(json.dumps(days))

    print(f"{report['asof']}  SPX {mkt['spx']:.2f}  XSP {prices.get('XSP', 0):.2f}  VIX {mkt['vix']:.2f}  "
          + "  ".join(f"{u} 候選 {c['candidates']} 筆" for u, c in counts.items()))
    for c in report["candidates"][:5]:
        ks = "/".join(f"{l['strike']:.0f}{l['type']}" for l in c["legs"])
        print(f"  {c['underlying']} {c['strategy']:<12} {c['expiry']} {ks:<28} 收 {c['credit_fill']:>6.2f}  "
              f"勝率 模型 {c['base']['pop']:.1%} / 歷史 {c['historical']['pop']:.1%}  EV/風險 {c['ev_per_risk']:+.3f} / {c['ev_per_risk_hist']:+.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
