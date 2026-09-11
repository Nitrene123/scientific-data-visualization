# Plot Recipes

Use bundled scripts first. These notes are only for customization after a template has been copied into the workspace.

- SHAP composite: stacked horizontal mean-absolute importance bars plus class/model beeswarm strips and a feature-value colorbar.
- Paired raincloud: half-violins, jittered observations, box geometry, mean diamonds, and connected mean trends.
- ROC with CI: fold curves interpolated to a shared FPR grid, mean curve, standard-deviation band, AUC mean ± sd legend, and diagonal baseline.
- Taylor diagram: polar coordinates with angle `arccos(correlation)` and radius as model standard deviation.
- Correlation grid: lower scatter/fitted CI, diagonal histograms, upper coefficient cells with diverging colors and stars.
- Prediction marginal grid: predicted-vs-actual scatter plus top/right histograms and KDE-like curves.
- 3D tuning surface: `mpl_toolkits.mplot3d`, smooth response surface, colorbar, and checked camera angle.
- Split violin + correlation matrix: signed lower-triangle marker matrix plus left/right half-violin distribution comparison.
- Circular heatmap: polar bars, flipped outer labels, central legend, and ring-specific color scales.
- Chord diagram: outer `Wedge` sectors and translucent Bezier `PathPatch` ribbons.
- Urban cooling composite: stacked city bars, raincloud metric panels, city legend, and boxplots with connected means.
- Grouped comparison: raw jittered observations, mean markers, confidence intervals, and a restrained group trend.
- Ridge plot: normalized one-dimensional kernel densities offset by condition with a shared quantitative axis.
- Hexbin fit: log-count hexagons for overplotted points plus an explicitly labeled fitted curve.
- Expression heatmap: standardized matrix, meaningful row/column ordering, group separators, and a labeled colour scale.
- Ordination: group-colored points, 95% reference ellipses, explained axis fractions, and method metadata.
- UMAP clusters: embedding points with cluster labels; method and preprocessing must be reported with real data.
- Volcano: effect size against adjusted significance, threshold guides, and deterministic label selection.
- Forest: point estimates with asymmetric confidence intervals and a domain-specific null reference line.
- Sankey: proportional ribbons between ordered stages with node totals and a consistent category palette.
- Network: explicit node/edge semantics, edge-width weighting, group color, and filtering for dense graphs.
- Spatial map: projected regions or points, a scale-aware color/size legend, and geographic context.
- UpSet: intersection-size bars paired with a membership matrix, ordered by intersection size.
- Ternary: barycentric coordinates inside a three-component simplex with component labels and composition color.
- Parallel coordinates: normalized axes, transparent individual paths, and highlighted group summaries.
- Radar: a small number of common normalized metrics, closed profiles, and a restrained legend.
