// SPX 價差損益 / 期望值計算核心（瀏覽器與 Node 共用）
// 所有價格以「每股」為單位，乘數 100。SPX 為歐式、現金交割，故用 Black-Scholes（含股息率 q）。
(function (root) {
  'use strict';

  const MULT = 100;
  const SQRT2PI = Math.sqrt(2 * Math.PI);

  function npdf(x) { return Math.exp(-0.5 * x * x) / SQRT2PI; }

  // Zelen & Severo 26.2.17，誤差 < 7.5e-8
  function ncdf(x) {
    const L = Math.abs(x);
    const k = 1 / (1 + 0.2316419 * L);
    const poly = k * (0.319381530 + k * (-0.356563782 + k * (1.781477937 + k * (-1.821255978 + k * 1.330274429))));
    const w = 1 - npdf(L) * poly;
    return x < 0 ? 1 - w : w;
  }

  function intrinsic(type, S, K) {
    return type === 'C' ? Math.max(S - K, 0) : Math.max(K - S, 0);
  }

  // 回傳 price、delta、gamma、vega（每 1 個 IV 百分點）、theta（每日曆日）
  function bs(type, S, K, T, r, q, sigma) {
    if (T <= 1e-8 || sigma <= 1e-8) {
      const p = intrinsic(type, S, K);
      const itm = type === 'C' ? S > K : S < K;
      return { price: p, delta: itm ? (type === 'C' ? 1 : -1) : 0, gamma: 0, vega: 0, theta: 0 };
    }
    const sqT = Math.sqrt(T);
    const sT = sigma * sqT;
    const d1 = (Math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / sT;
    const d2 = d1 - sT;
    const dfq = Math.exp(-q * T);
    const dfr = Math.exp(-r * T);
    const pdf1 = npdf(d1);
    let price, delta, theta;
    if (type === 'C') {
      price = S * dfq * ncdf(d1) - K * dfr * ncdf(d2);
      delta = dfq * ncdf(d1);
      theta = -S * dfq * pdf1 * sigma / (2 * sqT) - r * K * dfr * ncdf(d2) + q * S * dfq * ncdf(d1);
    } else {
      price = K * dfr * ncdf(-d2) - S * dfq * ncdf(-d1);
      delta = -dfq * ncdf(-d1);
      theta = -S * dfq * pdf1 * sigma / (2 * sqT) + r * K * dfr * ncdf(-d2) - q * S * dfq * ncdf(-d1);
    }
    return {
      price,
      delta,
      gamma: dfq * pdf1 / (S * sT),
      vega: S * dfq * pdf1 * sqT / 100,
      theta: theta / 365,
    };
  }

  // 簡化版 SPX skew：履約價每低於現價 10%，IV 增加 skewPts 個百分點（高於現價則遞減），下限為 base 的一半
  function skewIV(baseIV, skewPts, S, K) {
    const iv = baseIV + (skewPts / 100) * (-Math.log(K / S)) / 0.10;
    return Math.max(iv, baseIV * 0.5);
  }

  function roundStrike(K, step) { return Math.round(K / step) * step; }

  // 找出 |delta| 最接近目標值的履約價
  function strikeForDelta(type, target, m) {
    const step = m.strikeStep || 5;
    let best = null;
    const lo = roundStrike(m.S * 0.5, step);
    const hi = roundStrike(m.S * 1.5, step);
    for (let K = lo; K <= hi; K += step) {
      const d = Math.abs(bs(type, m.S, K, m.T, m.r, m.q, skewIV(m.iv, m.skew, m.S, K)).delta);
      const err = Math.abs(d - target);
      if (!best || err < best.err) best = { K, err };
    }
    return best.K;
  }

  // 預設組合。qty 正數 = 買進、負數 = 賣出（每組 1 口）
  function buildPreset(name, m, width, targetDelta) {
    const step = m.strikeStep || 5;
    const atm = roundStrike(m.S, step);
    const sp = () => strikeForDelta('P', targetDelta, m);
    const sc = () => strikeForDelta('C', targetDelta, m);
    switch (name) {
      case 'bull_put': { const k = sp(); return [{ type: 'P', strike: k, qty: -1 }, { type: 'P', strike: k - width, qty: 1 }]; }
      case 'bear_call': { const k = sc(); return [{ type: 'C', strike: k, qty: -1 }, { type: 'C', strike: k + width, qty: 1 }]; }
      case 'iron_condor': {
        const kp = sp(), kc = sc();
        return [
          { type: 'P', strike: kp - width, qty: 1 }, { type: 'P', strike: kp, qty: -1 },
          { type: 'C', strike: kc, qty: -1 }, { type: 'C', strike: kc + width, qty: 1 },
        ];
      }
      case 'iron_fly':
        return [
          { type: 'P', strike: atm - width, qty: 1 }, { type: 'P', strike: atm, qty: -1 },
          { type: 'C', strike: atm, qty: -1 }, { type: 'C', strike: atm + width, qty: 1 },
        ];
      case 'bull_call_debit': return [{ type: 'C', strike: atm, qty: 1 }, { type: 'C', strike: atm + width, qty: -1 }];
      case 'bear_put_debit': return [{ type: 'P', strike: atm, qty: 1 }, { type: 'P', strike: atm - width, qty: -1 }];
      default: return [];
    }
  }

  // 為每隻腳補上 iv 與理論價（若使用者未手動給價）
  function priceLegs(legs, m) {
    return legs.map((l) => {
      const iv = l.iv != null && l.iv > 0 ? l.iv : skewIV(m.iv, m.skew, m.S, l.strike);
      const theo = bs(l.type, m.S, l.strike, m.T, m.r, m.q, iv).price;
      const premium = l.premium != null && l.premium >= 0 ? l.premium : theo;
      return Object.assign({}, l, { iv, theo, premium });
    });
  }

  // 每組（1 口組合）的固定成本：手續費 × 腳數口數 + 滑價（每腳每股）× 100
  function costPerUnit(legs, m) {
    const n = legs.reduce((s, l) => s + Math.abs(l.qty), 0);
    return n * (m.commission || 0) + n * (m.slippage || 0) * MULT;
  }

  function netCredit(legs) { return -legs.reduce((s, l) => s + l.qty * l.premium, 0); }

  // 到期損益（每組，美元，已扣成本）
  function expiryPnL(legs, ST, credit, cost) {
    let v = 0;
    for (const l of legs) v += l.qty * intrinsic(l.type, ST, l.strike);
    return (v + credit) * MULT - cost;
  }

  // 評估日（距今 daysFwd 天、IV 平移 ivShift）的盤中市值損益
  function markPnL(legs, S, m, daysFwd, ivShift, credit, cost) {
    const T = Math.max(m.T - daysFwd / 365, 0);
    let v = 0;
    for (const l of legs) v += l.qty * bs(l.type, S, l.strike, T, m.r, m.q, Math.max(l.iv + ivShift, 0.01)).price;
    return (v + credit) * MULT - cost;
  }

  // 到期損益為分段線性，轉折點在各履約價
  function payoffShape(legs, credit, cost) {
    const strikes = [...new Set(legs.map((l) => l.strike))].sort((a, b) => a - b);
    const callSlope = legs.filter((l) => l.type === 'C').reduce((s, l) => s + l.qty, 0);
    const xs = [0, ...strikes, strikes[strikes.length - 1] * 10];
    const ys = xs.map((x) => expiryPnL(legs, x, credit, cost));
    const breakevens = [];
    for (let i = 0; i < xs.length - 1; i++) {
      const [x0, x1, y0, y1] = [xs[i], xs[i + 1], ys[i], ys[i + 1]];
      if (y0 === 0) breakevens.push(x0);
      else if ((y0 < 0 && y1 > 0) || (y0 > 0 && y1 < 0)) breakevens.push(x0 + (0 - y0) * (x1 - x0) / (y1 - y0));
    }
    const inner = ys.slice(0, -1);
    return {
      maxProfit: callSlope > 0 ? Infinity : Math.max(...inner),
      maxLoss: callSlope < 0 ? -Infinity : Math.min(...inner),
      breakevens: breakevens.map((b) => Math.round(b * 100) / 100),
    };
  }

  // 到期價格分佈：log 報酬 = 漂移 + σ√T·z，z 為標準常態或「變異數為 1」的 Student-t（肥尾）
  // 以數值積分取代模擬：均勻網格 + 權重正規化，並校正使 E[S_T] = S·e^{(μ−q)T}
  function terminalGrid(S, T, mu, q, sigma, model, nu) {
    const N = 12001, Z = model === 't' ? 30 : 10;
    const dz = (2 * Z) / (N - 1);
    const c = model === 't' ? Math.sqrt((nu - 2) / nu) : 1;
    const s = sigma * Math.sqrt(T);
    const z = new Float64Array(N), w = new Float64Array(N);
    let sw = 0;
    for (let i = 0; i < N; i++) {
      const zi = -Z + i * dz;
      z[i] = zi;
      const p = model === 't' ? Math.pow(1 + (zi / c) * (zi / c) / nu, -(nu + 1) / 2) : Math.exp(-0.5 * zi * zi);
      w[i] = p; sw += p;
    }
    let mgf = 0;
    for (let i = 0; i < N; i++) { w[i] /= sw; mgf += w[i] * Math.exp(s * z[i]); }
    const m0 = Math.log(S) + (mu - q) * T - Math.log(mgf);
    const ST = new Float64Array(N);
    for (let i = 0; i < N; i++) ST[i] = Math.exp(m0 + s * z[i]);
    return { ST, w };
  }

  // 由 skew 曲線反推的風險中性分佈（Breeden–Litzenberger：q(K) = e^{rT} ∂²C/∂K²）
  function impliedGrid(m) {
    const h = Math.max(m.S * 0.0005, 0.5);
    const lo = m.S * 0.2, hi = m.S * 2.5;
    const call = (K) => bs('C', m.S, K, m.T, m.r, m.q, skewIV(m.iv, m.skew, m.S, K)).price;
    const ST = [], w = [];
    let sw = 0, prev = call(lo - h), cur = call(lo);
    for (let K = lo; K <= hi; K += h) {
      const next = call(K + h);
      const d = Math.max((prev - 2 * cur + next) / (h * h), 0);
      ST.push(K); w.push(d); sw += d;
      prev = cur; cur = next;
    }
    for (let i = 0; i < w.length; i++) w[i] /= sw;
    return { ST: Float64Array.from(ST), w: Float64Array.from(w) };
  }

  function stats(legs, credit, cost, shape, grid) {
    const { ST, w } = grid;
    const N = ST.length;
    const pnl = new Float64Array(N);
    let ev = 0, pWin = 0, sWin = 0, sLoss = 0, pMaxLoss = 0;
    const lossTol = isFinite(shape.maxLoss) ? shape.maxLoss + Math.abs(shape.maxLoss) * 0.01 : -Infinity;
    for (let i = 0; i < N; i++) {
      const p = expiryPnL(legs, ST[i], credit, cost);
      pnl[i] = p;
      ev += w[i] * p;
      if (p > 0) { pWin += w[i]; sWin += w[i] * p; } else { sLoss += w[i] * p; }
      if (shape.maxLoss < 0 && p <= lossTol) pMaxLoss += w[i];
    }
    // CVaR 5%：最差 5% 情境的平均損益
    const idx = Array.from({ length: N }, (_, i) => i).sort((a, b) => pnl[a] - pnl[b]);
    let acc = 0, tail = 0;
    for (const i of idx) {
      const take = Math.min(w[i], 0.05 - acc);
      if (take <= 0) break;
      tail += take * pnl[i]; acc += take;
    }
    const avgWin = pWin > 0 ? sWin / pWin : 0;
    const avgLoss = pWin < 1 ? sLoss / (1 - pWin) : 0;
    return {
      ev, pop: pWin, avgWin, avgLoss, pMaxLoss,
      cvar5: tail / 0.05,
      // 以平均賺賠計算的損益兩平勝率
      breakevenWinRate: avgWin - avgLoss > 0 ? -avgLoss / (avgWin - avgLoss) : NaN,
    };
  }

  function positionGreeks(legs, m) {
    const g = { delta: 0, gamma: 0, vega: 0, theta: 0 };
    for (const l of legs) {
      const r = bs(l.type, m.S, l.strike, m.T, m.r, m.q, l.iv);
      for (const k of Object.keys(g)) g[k] += l.qty * r[k] * MULT;
    }
    return g;
  }

  // m: { S, T(年), r, q, iv, skew, realVol, mu, model, nu, commission, slippage }
  function analyze(rawLegs, m) {
    const legs = priceLegs(rawLegs, m);
    const credit = netCredit(legs);
    const cost = costPerUnit(legs, m);
    const shape = payoffShape(legs, credit, cost);
    // 市場隱含（風險中性）分佈—以理論價成交時 EV ≈ −成本；用市價時可看出價格是否偏離模型
    const rn = stats(legs, credit, cost, shape, impliedGrid(m));
    // 你的假設（實現波動、預期報酬、可選肥尾）
    const real = stats(legs, credit, cost, shape, terminalGrid(m.S, m.T, m.mu, m.q, m.realVol, m.model, m.nu));
    const risk = isFinite(shape.maxLoss) ? -shape.maxLoss : NaN;
    return {
      legs, credit, cost, shape, rn, real,
      greeks: positionGreeks(legs, m),
      evOnRisk: risk > 0 ? real.ev / risk : NaN,
      fixedBreakevenWinRate: isFinite(shape.maxLoss) && shape.maxProfit > 0
        ? -shape.maxLoss / (shape.maxProfit - shape.maxLoss) : NaN,
    };
  }

  const api = { MULT, npdf, ncdf, bs, skewIV, strikeForDelta, buildPreset, priceLegs, netCredit, costPerUnit,
    expiryPnL, markPnL, payoffShape, terminalGrid, impliedGrid, stats, positionGreeks, analyze };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.OptEngine = api;
})(typeof window !== 'undefined' ? window : globalThis);
