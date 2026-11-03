# scibox shared publication style

This style is based on the figures in the supplied Nature Communications article and its supplement. The article and supplement are one study, so the palette is a practical reference for model comparisons and scientific panels rather than a universal rule for every discipline. Graphic font details are estimates because the embedded figures are raster images.

## Categorical colors

The recurring model series use the first five colors below and distinguish them with marker shapes. These RGB values match the paper's apparent Matplotlib Tab10 colors closely; small raster and export differences are expected.

| Role | Color | Hex | Marker in the paper's model examples |
| --- | --- | --- | --- |
| Focal model / Cross-Unet | Red | `#D62728` | Circle |
| Baseline / Cross-Former | Blue | `#1F77B4` | Square |
| Baseline / Transformer | Green | `#2CA02C` | Up triangle |
| Baseline / TimeFilter | Orange | `#FF7F0E` | Diamond |
| Baseline / TimeMixer | Purple | `#9467BD` | Down triangle |
| Ground truth / neutral reference | Near-black | `#111111` | Circle or solid line |

`QUALITATIVE` and `QUALITATIVE_MARKERS` share the same index order; `series_style(index)` returns the color/marker pair for custom model-comparison plots without forcing markers onto reference or guide lines. `MODEL_COLORS` and `MODEL_MARKERS` provide stable mappings for the paper's named model examples. The remaining colors are brown `#8C564B`, pink `#E377C2`, gray `#7F7F7F`, olive `#BCBD22`, and cyan `#17BECF`. Do not use red and green as the only way to distinguish important groups; retain shape, line style, or direct labels as secondary cues.

## Typography and axes

- Use an Arial-like sans-serif face for plot labels; use the configured sans-serif fallbacks if Arial is unavailable.
- Use approximately 8.5 pt as the base size, 9 pt for axis labels, 7.5 pt for tick labels, and 8 pt for legends. These are starting values; check at the final printed width.
- Use bold lowercase panel tags (`a`, `b`, `c`) with consistent placement. Keep figure titles in the caption unless an in-figure title adds needed context.
- Use white figure and axes backgrounds, near-black labels and spines, and approximately 0.8 pt axis lines.
- Use light-gray dashed grid lines around `#D9D9D9`, about 0.65 pt wide. Enable only the grid direction that helps read the values.
- Preserve each chart's appropriate frame geometry; the reference paper uses both full panel frames and left/bottom-only axes depending on the chart.

## Lines, points, and uncertainty

- Start with 1.6 pt series lines and 4 pt markers. Give each model a stable color and a distinct marker in multi-series plots.
- Use restrained semi-transparent ribbons (often alpha 0.12–0.20) only for supplied or computed uncertainty. State whether a band is a standard deviation, confidence interval, or another quantity.
- For observed-versus-predicted time series, use a dark observed line and colored predictions. A light forecast-window background and a dashed boundary can separate input from forecast, when those periods are defined in the data.
- For forest plots, align metric columns and comparison groups, use point markers with horizontal intervals, and show the scientifically meaningful reference value.

## Multi-panel composition

- Keep comparable panels on aligned axes with shared limits and consistent encodings.
- Mark panels with bold lowercase letters and keep the tag away from data and tick labels.
- Put one compact shared legend above or below the panel group when series mappings are common. Use local legends only when mappings differ.
- Use alternating light panel bands only to distinguish real groups, such as forecast horizons; keep the plotting background white.
- Reserve enough room for axis labels and legends at one- or two-column publication width. Reduce decorative titles and repeated labels before shrinking text.

## Continuous color maps and chart-specific exceptions

- Use `viridis` for ordered positive or standardized attention-like values, `magma` where a dark-to-light intensity scale suits the data, and `RdBu_r` for values centered on a meaningful midpoint such as zero or correlation zero.
- Keep the existing `THREED` scale for the two 3D bar-matrix templates; it encodes continuous response magnitude and is not a model category palette.
- Use pastel fills for flow or block diagrams only when they make component grouping clearer. Use a chart's established semantic colors for status, sign, or risk when those meanings are part of the data.
- Do not copy any values, uncertainty ranges, labels, or conclusions from the reference paper into user plots.

## Export and review

- Export PNG at 300 dpi for a preview and PDF/SVG for vector editing and print when supported by the chart.
- Keep PDF fonts embedded as TrueType and SVG text editable (`pdf.fonttype = 42`, `svg.fonttype = none`).
- Inspect the exported figure at full size and at its intended manuscript width. Check legend placement, panel tags, tick-label overlap, color distinctions, and whether every uncertainty mark has a data source.

The executable defaults live in [`scripts/palette.py`](../scripts/palette.py), especially `apply_paper_style()`, `QUALITATIVE`, `QUALITATIVE_MARKERS`, `series_style()`, `MODEL_COLORS`, and `MODEL_MARKERS`.
