# Scientific Data Visualization

[简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

A reproducible Agent Skill for scientific data visualization with 50 runnable Matplotlib templates, chart-selection guidance, the original compatible palette, and PNG/PDF/SVG export.

## Features

- Covers comparison, distribution, correlation, dimensionality reduction, model evaluation, survival analysis, omics, time series, spatial/network data, and 3D data.
- Includes 3D bar matrices, heatmap projections, response surfaces, 3D scatter, volume, and vector-field templates; use 3D only when the third dimension has a real scientific meaning.
- Keeps the original project palette by default and provides `viridis`, `magma`, and `RdBu_r` for continuous values.
- Includes deterministic example data, 50 preview images, and reproducible scripts that export PNG, PDF, and SVG.
- Provides chart-selection boundaries and scientific figure quality-control guidance.

## Usage

1. Install this repository as a skill directory in the Agent's skills directory.
2. Read `SKILL.md` and choose a template based on the data structure and research question.
3. On Windows, run:

   ```bash
   python scripts/render_template.py --list
   python scripts/render_template.py 3d-bar-heat-projection
   ```

4. Outputs are written to `绘图复刻/outputs/` by default, and the template script is copied to `绘图复刻/scripts/`.

## Automatic loading in Codex, Claude, and other Agents

This repository follows the Agent Skills directory convention: `SKILL.md` must be directly at the root of the installed skill directory. After installation, start a new Agent session so it can rescan the skills directory. Skill matching uses the `name` and `description` in `SKILL.md`; if automatic matching does not trigger, explicitly ask the Agent to use the scientific data visualization skill.

### Codex on Windows

Clone the repository and copy it to the user-level Codex skills directory:

```powershell
git clone https://github.com/Nitrene123/scientific-data-visualization.git
$repo = Join-Path (Get-Location) "scientific-data-visualization"
$codexSkill = Join-Path $env:USERPROFILE ".codex\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $codexSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $codexSkill -Recurse -Force
```

Restart the Codex session so it rescans `SKILL.md`. For project-scoped installation, use `<project>/.codex/skills/scientific-data-visualization/` instead.

### Claude Code on Windows

Copy the repository to Claude Code's project-level `.claude/skills/` or user-level `.claude/skills/` directory:

```powershell
$claudeSkill = Join-Path $env:USERPROFILE ".claude\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $claudeSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $claudeSkill -Recurse -Force
```

For a standalone Claude Code project, set `$claudeSkill` to `<project>\.claude\skills\scientific-data-visualization`. For example, the standalone installation used on this machine is `D:\claude-code-cn-plus\.claude\skills\scientific-data-visualization`. Restart Claude Code after installation.

### Other compatible Agents

Copy the repository into the Agent's configured skills directory and preserve this layout:

~~~text
<skills-root>/scientific-data-visualization/
├── SKILL.md
├── scripts/
├── references/
└── assets/
~~~

Agent Skills-compatible implementations typically read `name` and `description` from `SKILL.md` for matching. If an Agent only supports explicit loading, add this directory in its configuration or reference the skill by name in the conversation.

### Automatic-loading checklist

- Check that `SKILL.md` is directly inside the skill directory, not nested under an extra repository directory.
- Start a new session or restart the Agent so it rescans the skills directory.
- Smoke-test with: “Use the scientific data visualization skill to create a 3D bar matrix with a heatmap projection.”
- Run `python scripts/render_template.py --list` to confirm that all 50 templates are visible.

## Template categories

| Category | Representative templates |
| --- | --- |
| Comparison and distribution | `grouped-comparison`, `paired-raincloud`, `ridge-plot`, `forest-plot` |
| Relationships and correlation | `hexbin-fit`, `correlation-pairgrid`, `bland-altman`, `ma-plot` |
| Omics and dimensionality reduction | `expression-heatmap`, `volcano-plot`, `manhattan-plot`, `gsea-curve`, `umap-clusters`, `ordination-pcoa` |
| Classification and model evaluation | `confusion-matrix`, `cv-roc-ci`, `precision-recall-curve`, `calibration-reliability`, `det-curve`, `learning-curve` |
| Composition, flow, and hierarchy | `sankey-flow`, `nature-chord-diagram`, `treemap-hierarchy`, `sunburst-hierarchy`, `upset-plot`, `waterfall-contribution` |
| Time, spatial, and network data | `time-series-ribbon`, `event-timeline`, `survival-km`, `spatial-map`, `network-graph`, `ohlc-candlestick` |
| 3D and multivariate data | `3d-bar-heatmap`, `3d-bar-heat-projection`, `3d-response-surface`, `3d-scatter`, `3d-volume`, `3d-vector-field`, `parallel-coordinates`, `radar-profile`, `ternary-composition` |
| Diagnostics and composite figures | `residual-diagnostics`, `taylor-diagram`, `multiclass-shap-combo`, `prediction-marginal-grid`, `rf-tpe-surface`, `urban-park-cooling-combo`, `grouped-circular-heatmap`, `grouped-corr-split-violin` |

See `references/figure-catalog.md` and `references/visualization-catalog.md` for all template IDs, use cases, data requirements, and selection boundaries.

## Template preview gallery

The thumbnails below correspond directly to the 50 preview files in `assets/previews/`; click an image to open the original file.

<table>
<tr>
<td><a href="assets/previews/3d_bar_heat_projection_replica.png"><img src="assets/previews/3d_bar_heat_projection_replica.png" alt="3d-bar-heat-projection" width="180"></a><br><sub><code>3d-bar-heat-projection</code></sub></td>
<td><a href="assets/previews/3d_bar_heatmap_replica.png"><img src="assets/previews/3d_bar_heatmap_replica.png" alt="3d-bar-heatmap" width="180"></a><br><sub><code>3d-bar-heatmap</code></sub></td>
<td><a href="assets/previews/3d_response_surface_replica.png"><img src="assets/previews/3d_response_surface_replica.png" alt="3d-response-surface" width="180"></a><br><sub><code>3d-response-surface</code></sub></td>
<td><a href="assets/previews/3d_scatter_replica.png"><img src="assets/previews/3d_scatter_replica.png" alt="3d-scatter" width="180"></a><br><sub><code>3d-scatter</code></sub></td>
<td><a href="assets/previews/3d_vector_field_replica.png"><img src="assets/previews/3d_vector_field_replica.png" alt="3d-vector-field" width="180"></a><br><sub><code>3d-vector-field</code></sub></td>
</tr>
<tr>
<td><a href="assets/previews/3d_volume_replica.png"><img src="assets/previews/3d_volume_replica.png" alt="3d-volume" width="180"></a><br><sub><code>3d-volume</code></sub></td>
<td><a href="assets/previews/bland_altman_replica.png"><img src="assets/previews/bland_altman_replica.png" alt="bland-altman" width="180"></a><br><sub><code>bland-altman</code></sub></td>
<td><a href="assets/previews/calibration_reliability_replica.png"><img src="assets/previews/calibration_reliability_replica.png" alt="calibration-reliability" width="180"></a><br><sub><code>calibration-reliability</code></sub></td>
<td><a href="assets/previews/confusion_matrix_replica.png"><img src="assets/previews/confusion_matrix_replica.png" alt="confusion-matrix" width="180"></a><br><sub><code>confusion-matrix</code></sub></td>
<td><a href="assets/previews/correlation_pairgrid_replica.png"><img src="assets/previews/correlation_pairgrid_replica.png" alt="correlation-pairgrid" width="180"></a><br><sub><code>correlation-pairgrid</code></sub></td>
</tr>
<tr>
<td><a href="assets/previews/cv_roc_ci_replica.png"><img src="assets/previews/cv_roc_ci_replica.png" alt="cv-roc-ci" width="180"></a><br><sub><code>cv-roc-ci</code></sub></td>
<td><a href="assets/previews/det_curve_replica.png"><img src="assets/previews/det_curve_replica.png" alt="det-curve" width="180"></a><br><sub><code>det-curve</code></sub></td>
<td><a href="assets/previews/enrichment_dotplot_replica.png"><img src="assets/previews/enrichment_dotplot_replica.png" alt="enrichment-dotplot" width="180"></a><br><sub><code>enrichment-dotplot</code></sub></td>
<td><a href="assets/previews/event_timeline_replica.png"><img src="assets/previews/event_timeline_replica.png" alt="event-timeline" width="180"></a><br><sub><code>event-timeline</code></sub></td>
<td><a href="assets/previews/expression_heatmap_replica.png"><img src="assets/previews/expression_heatmap_replica.png" alt="expression-heatmap" width="180"></a><br><sub><code>expression-heatmap</code></sub></td>
</tr>
<tr>
<td><a href="assets/previews/forest_plot_replica.png"><img src="assets/previews/forest_plot_replica.png" alt="forest-plot" width="180"></a><br><sub><code>forest-plot</code></sub></td>
<td><a href="assets/previews/grouped_circular_heatmap_replica.png"><img src="assets/previews/grouped_circular_heatmap_replica.png" alt="grouped-circular-heatmap" width="180"></a><br><sub><code>grouped-circular-heatmap</code></sub></td>
<td><a href="assets/previews/grouped_comparison_replica.png"><img src="assets/previews/grouped_comparison_replica.png" alt="grouped-comparison" width="180"></a><br><sub><code>grouped-comparison</code></sub></td>
<td><a href="assets/previews/grouped_corr_split_violin_replica.png"><img src="assets/previews/grouped_corr_split_violin_replica.png" alt="grouped-corr-split-violin" width="180"></a><br><sub><code>grouped-corr-split-violin</code></sub></td>
<td><a href="assets/previews/gsea_curve_replica.png"><img src="assets/previews/gsea_curve_replica.png" alt="gsea-curve" width="180"></a><br><sub><code>gsea-curve</code></sub></td>
</tr>
<tr>
<td><a href="assets/previews/hexbin_fit_replica.png"><img src="assets/previews/hexbin_fit_replica.png" alt="hexbin-fit" width="180"></a><br><sub><code>hexbin-fit</code></sub></td>
<td><a href="assets/previews/learning_curve_replica.png"><img src="assets/previews/learning_curve_replica.png" alt="learning-curve" width="180"></a><br><sub><code>learning-curve</code></sub></td>
<td><a href="assets/previews/ma_plot_replica.png"><img src="assets/previews/ma_plot_replica.png" alt="ma-plot" width="180"></a><br><sub><code>ma-plot</code></sub></td>
<td><a href="assets/previews/manhattan_plot_replica.png"><img src="assets/previews/manhattan_plot_replica.png" alt="manhattan-plot" width="180"></a><br><sub><code>manhattan-plot</code></sub></td>
<td><a href="assets/previews/multiclass_shap_combo_replica.png"><img src="assets/previews/multiclass_shap_combo_replica.png" alt="multiclass-shap-combo" width="180"></a><br><sub><code>multiclass-shap-combo</code></sub></td>
</tr>
<tr>
<td><a href="assets/previews/nature_chord_diagram_replica.png"><img src="assets/previews/nature_chord_diagram_replica.png" alt="nature-chord-diagram" width="180"></a><br><sub><code>nature-chord-diagram</code></sub></td>
<td><a href="assets/previews/network_graph_replica.png"><img src="assets/previews/network_graph_replica.png" alt="network-graph" width="180"></a><br><sub><code>network-graph</code></sub></td>
<td><a href="assets/previews/ohlc_candlestick_replica.png"><img src="assets/previews/ohlc_candlestick_replica.png" alt="ohlc-candlestick" width="180"></a><br><sub><code>ohlc-candlestick</code></sub></td>
<td><a href="assets/previews/ordination_pcoa_replica.png"><img src="assets/previews/ordination_pcoa_replica.png" alt="ordination-pcoa" width="180"></a><br><sub><code>ordination-pcoa</code></sub></td>
<td><a href="assets/previews/paired_raincloud_replica.png"><img src="assets/previews/paired_raincloud_replica.png" alt="paired-raincloud" width="180"></a><br><sub><code>paired-raincloud</code></sub></td>
</tr>
<tr>
<td><a href="assets/previews/parallel_coordinates_replica.png"><img src="assets/previews/parallel_coordinates_replica.png" alt="parallel-coordinates" width="180"></a><br><sub><code>parallel-coordinates</code></sub></td>
<td><a href="assets/previews/precision_recall_curve_replica.png"><img src="assets/previews/precision_recall_curve_replica.png" alt="precision-recall-curve" width="180"></a><br><sub><code>precision-recall-curve</code></sub></td>
<td><a href="assets/previews/prediction_marginal_grid_replica.png"><img src="assets/previews/prediction_marginal_grid_replica.png" alt="prediction-marginal-grid" width="180"></a><br><sub><code>prediction-marginal-grid</code></sub></td>
<td><a href="assets/previews/radar_profile_replica.png"><img src="assets/previews/radar_profile_replica.png" alt="radar-profile" width="180"></a><br><sub><code>radar-profile</code></sub></td>
<td><a href="assets/previews/residual_diagnostics_replica.png"><img src="assets/previews/residual_diagnostics_replica.png" alt="residual-diagnostics" width="180"></a><br><sub><code>residual-diagnostics</code></sub></td>
</tr>
<tr>
<td><a href="assets/previews/rf_tpe_surface_replica.png"><img src="assets/previews/rf_tpe_surface_replica.png" alt="rf-tpe-surface" width="180"></a><br><sub><code>rf-tpe-surface</code></sub></td>
<td><a href="assets/previews/ridge_plot_replica.png"><img src="assets/previews/ridge_plot_replica.png" alt="ridge-plot" width="180"></a><br><sub><code>ridge-plot</code></sub></td>
<td><a href="assets/previews/sankey_flow_replica.png"><img src="assets/previews/sankey_flow_replica.png" alt="sankey-flow" width="180"></a><br><sub><code>sankey-flow</code></sub></td>
<td><a href="assets/previews/spatial_map_replica.png"><img src="assets/previews/spatial_map_replica.png" alt="spatial-map" width="180"></a><br><sub><code>spatial-map</code></sub></td>
<td><a href="assets/previews/sunburst_hierarchy_replica.png"><img src="assets/previews/sunburst_hierarchy_replica.png" alt="sunburst-hierarchy" width="180"></a><br><sub><code>sunburst-hierarchy</code></sub></td>
</tr>
<tr>
<td><a href="assets/previews/survival_km_replica.png"><img src="assets/previews/survival_km_replica.png" alt="survival-km" width="180"></a><br><sub><code>survival-km</code></sub></td>
<td><a href="assets/previews/taylor_diagram_replica.png"><img src="assets/previews/taylor_diagram_replica.png" alt="taylor-diagram" width="180"></a><br><sub><code>taylor-diagram</code></sub></td>
<td><a href="assets/previews/ternary_composition_replica.png"><img src="assets/previews/ternary_composition_replica.png" alt="ternary-composition" width="180"></a><br><sub><code>ternary-composition</code></sub></td>
<td><a href="assets/previews/time_series_ribbon_replica.png"><img src="assets/previews/time_series_ribbon_replica.png" alt="time-series-ribbon" width="180"></a><br><sub><code>time-series-ribbon</code></sub></td>
<td><a href="assets/previews/treemap_hierarchy_replica.png"><img src="assets/previews/treemap_hierarchy_replica.png" alt="treemap-hierarchy" width="180"></a><br><sub><code>treemap-hierarchy</code></sub></td>
</tr>
<tr>
<td><a href="assets/previews/umap_clusters_replica.png"><img src="assets/previews/umap_clusters_replica.png" alt="umap-clusters" width="180"></a><br><sub><code>umap-clusters</code></sub></td>
<td><a href="assets/previews/upset_plot_replica.png"><img src="assets/previews/upset_plot_replica.png" alt="upset-plot" width="180"></a><br><sub><code>upset-plot</code></sub></td>
<td><a href="assets/previews/urban_park_cooling_combo_replica.png"><img src="assets/previews/urban_park_cooling_combo_replica.png" alt="urban-park-cooling-combo" width="180"></a><br><sub><code>urban-park-cooling-combo</code></sub></td>
<td><a href="assets/previews/volcano_plot_replica.png"><img src="assets/previews/volcano_plot_replica.png" alt="volcano-plot" width="180"></a><br><sub><code>volcano-plot</code></sub></td>
<td><a href="assets/previews/waterfall_contribution_replica.png"><img src="assets/previews/waterfall_contribution_replica.png" alt="waterfall-contribution" width="180"></a><br><sub><code>waterfall-contribution</code></sub></td>
</tr>
</table>

## Output formats

| Format | Use case | Description |
| --- | --- | --- |
| PNG | Quick previews, presentations, and documents | High-resolution raster output |
| PDF | Manuscript layout and printing | Vector output |
| SVG | Post-editing and web use | Vector output |

## Workflow

1. Define the scientific question, observational unit, variable types, grouping/pairing structure, and uncertainty meaning.
2. Use `references/visualization-catalog.md` to choose the smallest interpretable visual grammar.
3. Use a bundled template or copy the nearest template for customization, keeping labels, group order, scales, and colors consistent.
4. Export PNG/PDF/SVG and check text, legends, axes, colorbars, outliers, and overlap.
5. Record the real data provenance; simulated templates are examples and must not be presented as empirical results.

## Limitations

- Use 3D charts only when the third dimension represents meaningful spatial, temporal, response-surface, or field data; prefer 2D charts for ordinary 2D data.
- Use sequential palettes for ordered values and diverging palettes around a meaningful midpoint; avoid rainbow scales and red–green-only distinctions.
- Bundled data is deterministic simulated data and does not represent any real study or user data.
- When plotting real data, document data provenance, transformations, missing-value handling, and statistical tests in the handoff.

## Repository structure

~~~text
scientific-data-visualization/
├── SKILL.md
├── README.md
├── scripts/
│   ├── palette.py
│   ├── render_template.py
│   └── templates/
├── references/
│   ├── figure-catalog.md
│   ├── visualization-catalog.md
│   ├── chart-types-research.md
│   └── palette-guide.md
└── assets/
    └── previews/
~~~

## Palette

`scripts/palette.py` keeps the original project palette as the default theme. Use `QUALITATIVE` for unordered groups, `viridis` or `magma` for ordered values, and `RdBu_r` for data centered on a meaningful midpoint. Do not define a conflicting color system inside individual templates.

## Content responsibility

This repository provides reproducible scientific figure templates and methodological guidance. Example data is for demonstration only; users are responsible for checking real data, statistical assumptions, units, captions, and target-journal requirements.
