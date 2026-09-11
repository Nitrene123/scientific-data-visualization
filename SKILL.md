---
name: scientific-data-visualization
description: "Use this skill for data-driven scientific visualizations: selecting or reviewing an appropriate chart type, reproducing built-in scientific figure templates, or creating custom research plots. Especially applies to 科研绘图模板, 3D柱阵/响应面/散点/体数据/向量场, 混淆矩阵, Bland–Altman一致性图, MA图, 富集点图, Treemap/Sunburst, 瀑布图, 时间序列置信带, 事件时间线, OHLC/K线, DET与学习曲线, GSEA曲线, SHAP蜂群柱状图, 配对云雨图, 交叉验证ROC, PR与校准曲线, 生存曲线, 残差诊断, 曼哈顿图, 泰勒图, 相关矩阵组合图, 预测真实值边缘分布图, TPE调参3D曲面, 下三角相关矩阵半边小提琴图, 分组环形热图, 城市公园降温组合图, Nature和弦图, 热图, 火山图, 降维图, or 数据可视化选图. It does not cover editable conceptual diagrams, which belong to separate conceptual-diagram skills."
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob
---

# MathModel Figure Templates

This skill contains ready-to-run Python/matplotlib scripts for the figure templates. Paths in this file are **relative to this skill's own directory** — the folder holding this `SKILL.md`. Resolve them against wherever the skill is installed; never assume a fixed absolute location such as a sandbox mount.

## Visual Selection and Review

When the requested chart is not a named template, first establish the visual contract: the scientific question, observational unit, variable types, groups or pairing, transformation/normalization, and the conclusion the reader must see. Then read [references/visualization-catalog.md](references/visualization-catalog.md) to identify appropriate visual grammar and nearby examples from the supplied research-figure atlas.

- Compare groups with raw points plus an estimate/interval; retain pairing with connecting lines or paired points.
- Show distributions with violin, raincloud, box, or ridge plots; state sample size and what uncertainty bars mean.
- Show continuous relationships with scatter/fit plots; use 2D density or hexbin when overplotting is severe.
- Use heatmaps and correlations only after stating scaling, correlation method, clustering/distance, and ordering.
- For PCA/PCoA/NMDS/UMAP, report preprocessing, method and distance/neighbour settings; embeddings are not evidence of significance by themselves.
- Use volcano plots only for effect size against a stated p or adjusted-p value, with threshold and label-selection rules.
- Use Sankey, chord, circos, maps, ternary, or UpSet plots only when their underlying flow, relationship, spatial, compositional, or set-intersection structure is real. Do not choose them merely for ornament.
- Use 3D only when the third coordinate carries a real spatial, temporal, or response meaning. For a discrete x/y matrix with magnitude z, use a 3D bar matrix only when height adds interpretation; otherwise prefer a 2D heatmap. For a dense discrete matrix, `3d-bar-heat-projection` adds a floor heatmap/contour projection to localize peaks without relying on perspective alone. For two continuous inputs and a response, use a response surface with contours or a ground projection to preserve readability. Add a path overlay only when it represents a real trajectory or optimization path, not a decorative stroke.
- Use the shared legacy-compatible palette in `scripts/palette.py`: `QUALITATIVE` for unordered groups, `viridis`/`magma` for ordered numeric values, and `RdBu_r` for values centered on a meaningful midpoint. Avoid rainbow scales and red–green pairs; use shape, line type, or direct labels when color alone is insufficient.
- Use a precision–recall curve when the positive class is imbalanced or the operating point emphasizes retrieval; use a calibration/reliability diagram to judge probability agreement, not discrimination. Use Kaplan–Meier for time-to-event data with censoring and include censor marks and an at-risk table where space permits.
- Use residual diagnostics to assess model adequacy (residuals vs fitted, Q–Q, scale–location, and influence/outlier screening). Use a Manhattan plot for genome-wide indexed association tests, with an explicit p-value scale and threshold.
- Use a confusion matrix for class-wise error structure, Bland–Altman for agreement between two measurement methods, and an MA plot for mean-abundance versus fold-change structure. Use enrichment dot plots when pathway identity, gene ratio, count, and adjusted significance must be shown together.
- Use treemap/sunburst for hierarchical composition, waterfall for additive contribution decomposition, and a time-series ribbon for a trajectory with uncertainty and event windows. Use 3D scatter only when three measured coordinates add spatial or geometric meaning; otherwise use a 2D embedding or paired panels.
- Use DET curves for false-positive versus false-negative operating trade-offs and learning curves for performance versus training-set size. Use GSEA running-score curves only when a ranked list and a defined gene set are available. Use event timelines for intervals and milestones, and OHLC/candlesticks only for open–high–low–close data.
- Use voxel volumes or 3D vector fields only when the input is a real 3D grid/vector field; do not use them to add depth to ordinary 2D data. For Sunburst, preserve parent–child hierarchy and use the inner/outer rings consistently.

For the extended taxonomy and the official documentation checked for this library, read [references/chart-types-research.md](references/chart-types-research.md).
For the shared color system, read [references/palette-guide.md](references/palette-guide.md) and use `scripts/palette.py` in custom templates.

If a bundled template fits, take the Fast Path below. Otherwise create a reproducible custom plot in the current workspace, export PNG/PDF/SVG, and include the data provenance and validation in the handoff. Keep colour, labels, group order and scales consistent across a composite figure; do not infer quantitative conclusions from a screenshot alone.

## Fast Path

1. Match the requested chart in `references/figure-catalog.md`.
2. From the current workspace, run the renderer with the template id (`<skill-dir>` = the directory containing this `SKILL.md`):

```bash
python3 <skill-dir>/scripts/render_template.py paired-raincloud
```

On Windows use `python` rather than `python3`: `python3` resolves to the Microsoft Store stub, which exits silently and produces no output.

3. The renderer copies the bundled template script into `绘图复刻/scripts/`, runs it there, and writes outputs to `绘图复刻/outputs/`.
4. Return the generated PNG/PDF/SVG paths and the copied script path to the user.

Use `--list` to show supported ids:

```bash
python3 <skill-dir>/scripts/render_template.py --list
```

## Output Contract

- Work under the current workspace unless the user gives another path.
- Default project folder: `绘图复刻`.
- Script path: `绘图复刻/scripts/make_<template>.py`.
- Outputs: `绘图复刻/outputs/<template>_replica.png`, `.pdf`, `.svg`.
- Use the bundled scripts as the first choice; edit the copied workspace script only when the user requests customization.
- The bundled scripts use deterministic simulated data. Do not claim simulated values reproduce a source study exactly.

## ARS pipeline handoff

When this figure is created for `academic-pipeline`, return the normal output
paths together with a **Visual Asset Handoff** suitable for the paper's asset
ledger or Material Passport attachment. Include: figure purpose and proposed
caption, `source_skill: scientific-data-visualization`, the copied script path, PNG/PDF/SVG
paths, the exact data provenance (`simulated` or the supplied data/result path),
and validation performed. A simulated template remains illustrative and must not
be presented as an empirical result. ARS should only cite the exported figure
after this handoff is available.

## Template Ids

- `multiclass-shap-combo`
- `paired-raincloud`
- `cv-roc-ci`
- `taylor-diagram`
- `correlation-pairgrid`
- `prediction-marginal-grid`
- `rf-tpe-surface`
- `grouped-corr-split-violin`
- `grouped-circular-heatmap`
- `urban-park-cooling-combo`
- `nature-chord-diagram`
- `grouped-comparison`
- `ridge-plot`
- `hexbin-fit`
- `expression-heatmap`
- `ordination-pcoa`
- `umap-clusters`
- `volcano-plot`
- `forest-plot`
- `sankey-flow`
- `network-graph`
- `spatial-map`
- `upset-plot`
- `ternary-composition`
- `parallel-coordinates`
- `radar-profile`
- `3d-bar-heatmap`
- `3d-bar-heat-projection`
- `3d-response-surface`
- `precision-recall-curve`
- `calibration-reliability`
- `survival-km`
- `residual-diagnostics`
- `manhattan-plot`
- `confusion-matrix`
- `bland-altman`
- `ma-plot`
- `enrichment-dotplot`
- `treemap-hierarchy`
- `waterfall-contribution`
- `time-series-ribbon`
- `3d-scatter`
- `3d-volume`
- `3d-vector-field`
- `det-curve`
- `learning-curve`
- `gsea-curve`
- `sunburst-hierarchy`
- `event-timeline`
- `ohlc-candlestick`

## When Customizing

If the user asks for changes, copy/run the nearest template first, then edit the copied file in `绘图复刻/scripts/`. Preserve:

- `MPLCONFIGDIR` before importing matplotlib.
- deterministic seeds for simulated data.
- PNG/PDF/SVG export.
- readable labels, legends, and high-DPI output.

Use `references/plot-recipes.md` for implementation patterns.
