# SPX / XSP 選擇權價差工具

研究與教育用途，**不是投資建議**。

- `docs/index.html`：網頁 app，底部選單切換「篩選」（每日報告，讀 `docs/data/latest.json`）與「計算器」
- `docs/engine.js`：損益／期望值計算核心
- `screener/screen.py`：每日篩選器，只用 Python 標準庫；規則在 `screener/config.json`
- `.github/workflows/daily-screen.yml`：每個交易日收盤後自動執行並 commit 結果
- `reports/`、`research_notes/`：策略研究報告與筆記

## 本機執行

```bash
python3 screener/screen.py
python3 -m http.server 8000 --directory docs   # 打開 http://localhost:8000
```

## 方法

- 資料：Cboe 延遲報價（SPXW 與 XSP 選擇權鏈的 bid/ask/IV/Delta；XSP = SPX 的 1/10）、SPX 歷史收盤（1975 起）、VIX 歷史。
- 成交價估計：mid 與 natural 之間，由 `fill_haircut` 控制。
- 每個組合用兩種到期分佈計算 EV、勝率、最大虧損機率、CVaR 5%：
  - **模型**：Student-t 肥尾，實現波動 = ATM IV × `real_vol_ratio`。
  - **歷史**：SPX 所有相同交易日數的實際報酬（重疊視窗）。
- 排序分數 = 兩者中較差的 EV ÷ 最大虧損。所有數字假設持有到期。

## GitHub Pages

Settings → Pages → Source 選 *Deploy from a branch*，Branch 選 `main`、資料夾 `/docs`。
網址會是 https://enhow1108.github.io/stock_options/ 。注意：免費帳號的 Pages 需要 public repo，網站本身也是公開的。
