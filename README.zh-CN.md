# 科研数据可视化

[简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

面向 Codex、Claude 和其他 Agent 的可复现科研数据可视化技能，提供 50 个可直接运行的 Matplotlib 模板、选图规则、原始兼容色板以及 PNG/PDF/SVG 导出流程。

## 主要功能

- 覆盖比较、分布、相关、降维、模型评估、生存分析、组学、时间序列、空间/网络和三维数据。
- 内置 3D 柱阵、热力投影、响应面、3D 散点、体数据和向量场模板。
- 默认保留原项目色板，并提供 `viridis`、`magma`、`RdBu_r` 连续色图。
- 提供 50 张预览图、50 个模板脚本以及 PNG、PDF、SVG 输出。

## 使用方式

```bash
python scripts/render_template.py --list
python scripts/render_template.py 3d-bar-heat-projection
```

## 自动加载到 Codex、Claude 和其他 Agent

本仓库遵循 Agent Skills 目录约定：技能目录根部必须直接包含 `SKILL.md`。安装后重新启动 Agent 会话，使其重新扫描 skills 目录；如果没有自动触发，可在提示中明确说“使用科研数据可视化技能”。

### Codex（Windows）

```powershell
git clone https://github.com/Nitrene123/scientific-data-visualization.git
$repo = Join-Path (Get-Location) "scientific-data-visualization"
$codexSkill = Join-Path $env:USERPROFILE ".codex\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $codexSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $codexSkill -Recurse -Force
```

### Claude Code（Windows）

```powershell
$claudeSkill = Join-Path $env:USERPROFILE ".claude\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $claudeSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $claudeSkill -Recurse -Force
```

项目级安装分别使用 `.codex/skills/scientific-data-visualization/` 和 `.claude/skills/scientific-data-visualization/`。若 Claude Code 使用独立项目根目录，请将目标路径改为该项目的 `.claude/skills/scientific-data-visualization/`。

### 自动加载检查

- 确认 `SKILL.md` 位于技能目录第一层。
- 新开会话或重启 Agent。
- 运行 `python scripts/render_template.py --list` 确认 50 个模板可见。

## 模板预览

英文主 README 包含 50 张模板缩略图画廊；完整原图位于 [assets/previews](assets/previews)。

## 限制

模板内置数据是确定性模拟数据，仅用于演示，不代表真实研究结果。只有在第三维具有明确科学含义时才使用 3D 图。
