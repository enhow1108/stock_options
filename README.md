# SPX 選擇權價差工具

研究與教育用途，**不是投資建議**。

- `docs/calculator/`：SPX 價差損益／期望值計算器（純前端，直接開 `index.html` 即可）
- `docs/index.html`：每日篩選報告頁（讀取 `docs/data/latest.json`）
- `screener/screen.py`：每日篩選器，只用 Python 標準庫；規則在 `screener/config.json`
- `.github/workflows/daily-screen.yml`：每個交易日收盤後自動執行並 commit 結果
- `reports/`、`research_notes/`：策略研究報告與筆記

## 本機執行

```bash
python3 screener/screen.py
```

## 方法

- 資料：Cboe 延遲報價（SPXW 選擇權鏈的 bid/ask/IV/Delta）、SPX 歷史收盤（1975 起）、VIX 歷史。
- 成交價估計：mid 與 natural 之間，由 `fill_haircut` 控制。
- 每個組合用兩種到期分佈計算 EV、勝率、最大虧損機率、CVaR 5%：
  - **模型**：Student-t 肥尾，實現波動 = ATM IV × `real_vol_ratio`。
  - **歷史**：SPX 所有相同交易日數的實際報酬（重疊視窗）。
- 排序分數 = 兩者中較差的 EV ÷ 最大虧損。所有數字假設持有到期。

## GitHub Pages

Settings → Pages → Source 選 *Deploy from a branch*，Branch 選 `main`、資料夾 `/docs`。
注意：Pages 網站是公開的（private repo 需要 GitHub Pro 才能開 Pages，而且網站本身仍然公開）。
