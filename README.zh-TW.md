# 科研資料視覺化

[簡體中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

面向 Codex、Claude 與其他 Agent 的可重現科研資料視覺化技能，提供 50 個可直接執行的 Matplotlib 模板、選圖規則、原始相容色板與 PNG/PDF/SVG 匯出流程。

## 主要功能

- 覆蓋比較、分布、相關、降維、分類評估、生存分析、組學、時間序列、空間/網路與三維資料等常見科研圖形。
- 內建 3D 柱陣、熱力投影、響應面、散點、體資料與向量場模板。
- 預設保留原專案相容色板，並提供 `viridis`、`magma`、`RdBu_r` 等連續色圖。
- 50 個模板均提供預覽圖，並輸出 PNG、PDF、SVG。

## 使用方式

```bash
python scripts/render_template.py --list
python scripts/render_template.py 3d-bar-heat-projection
```

輸出預設位於 `繪圖復刻/outputs/`。

## 自動載入到 Codex、Claude 與其他 Agent

本倉庫採用 Agent Skills 目錄約定，技能目錄根部必須直接包含 `SKILL.md`。安裝到對應 skills 目錄後，請重新啟動 Agent 會話以重新掃描技能。

### Codex（Windows）

```powershell
git clone https://github.com/Nitrene123/scientific-data-visualization.git
$repo = Join-Path (Get-Location) "scientific-data-visualization"
$codexSkill = Join-Path $env:USERPROFILE ".codex\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $codexSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $codexSkill -Recurse -Force
```

也可以把技能放到專案的 `.codex/skills/scientific-data-visualization/`。

### Claude Code（Windows）

```powershell
$claudeSkill = Join-Path $env:USERPROFILE ".claude\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $claudeSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $claudeSkill -Recurse -Force
```

若使用獨立專案根目錄，請將目標改為 `<專案根目錄>\.claude\skills\scientific-data-visualization`。沒有自動觸發時，可在提示中明確寫出「使用科研資料視覺化技能」。

## 模板預覽

完整預覽圖位於 [assets/previews](assets/previews)，README 縮圖畫廊位於 [README.md](README.md#模板預覽)。

## 限制

模板內建資料是確定性模擬資料，僅用於示範，不代表任何真實研究結果。三維圖只應在第三維具有明確科學含義時使用。
