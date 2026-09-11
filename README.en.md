# Scientific Data Visualization

[简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

A reproducible Agent Skill for scientific data visualization with 50 runnable Matplotlib templates, chart-selection guidance, the original compatible palette, and PNG/PDF/SVG export.

## Features

- Covers comparison, distribution, correlation, dimensionality reduction, model evaluation, survival analysis, omics, time series, spatial/network data, and 3D data.
- Includes 3D bar matrices, heatmap projections, response surfaces, 3D scatter, volume, and vector-field templates.
- Keeps the original project palette by default and provides `viridis`, `magma`, and `RdBu_r` for continuous values.
- Includes 50 preview images and reproducible scripts that export PNG, PDF, and SVG.

## Usage

```bash
python scripts/render_template.py --list
python scripts/render_template.py 3d-bar-heat-projection
```

Outputs are written to `绘图复刻/outputs/` by default.

## Automatic loading in Codex, Claude, and other Agents

This repository follows the Agent Skills directory convention: `SKILL.md` must be directly at the root of the installed skill directory. After installation, start a new Agent session so it can rescan the skills directory. Skill matching uses the `name` and `description` in `SKILL.md`; if automatic matching does not trigger, explicitly ask the Agent to use the scientific data visualization skill.

### Codex on Windows

```powershell
git clone https://github.com/Nitrene123/scientific-data-visualization.git
$repo = Join-Path (Get-Location) "scientific-data-visualization"
$codexSkill = Join-Path $env:USERPROFILE ".codex\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $codexSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $codexSkill -Recurse -Force
```

For project-scoped installation, use `<project>/.codex/skills/scientific-data-visualization/` instead.

### Claude Code on Windows

```powershell
$claudeSkill = Join-Path $env:USERPROFILE ".claude\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $claudeSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $claudeSkill -Recurse -Force
```

For a standalone Claude Code project, use `<project>/.claude/skills/scientific-data-visualization/`. Restart Claude Code after installation.

### Other compatible Agents

Copy the repository into the Agent's configured skills directory and preserve this layout:

~~~text
<skills-root>/scientific-data-visualization/
├── SKILL.md
├── scripts/
├── references/
└── assets/
~~~

## Preview gallery

The README contains the 50-image gallery. Original preview files are also available in [assets/previews](assets/previews).

## Limitations

Bundled data is deterministic simulated data for illustration only. Use 3D charts only when the third dimension has a real scientific meaning.
