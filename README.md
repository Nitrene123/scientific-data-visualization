# 科研数据可视化

[简体中文](README.md) | [繁體中文](README.zh-TW.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

面向 Codex、Claude 和其他 Agent 的可复现科研数据可视化技能，提供 50 个可直接运行的 Matplotlib 模板、选图规则、原始兼容色板和 PNG/PDF/SVG 导出流程。

## 主要功能

- 覆盖比较、分布、相关、降维、分类评估、生存分析、组学分析、时间序列、空间/网络和三维数据等常见科研图形。
- 内置 3D 柱阵、热力投影、响应面、散点、体数据和向量场模板，只有在第三维具有明确科学含义时才推荐使用。
- 默认使用项目原有的兼容色板：蓝绿主色、暖红/橙强调色和中性灰，并保留 `viridis`、`magma`、`RdBu_r` 等连续色图。
- 所有模板使用确定性模拟数据，统一导出高清 PNG、PDF 和 SVG，便于预览、修改和论文排版。
- 提供选图边界与科研制图质控说明，避免把装饰性图形误当作数据证据。

## 使用方式

1. 将本仓库作为一个 skill 目录安装到 Agent 的 skills 目录。
2. 阅读 `SKILL.md`，根据数据结构和研究问题选择模板。
3. 在 Windows 中运行：

   ```bash
   python scripts/render_template.py --list
   python scripts/render_template.py 3d-bar-heat-projection
   ```

4. 渲染结果默认写入当前工作区的 `绘图复刻/outputs/`，模板脚本复制到 `绘图复刻/scripts/`。

## 自动加载到 Codex、Claude 和其他 Agent

本仓库采用 Agent Skills 目录约定：技能目录的根部必须直接包含 `SKILL.md`。安装到对应的 skills 目录后，Agent 会在新会话启动时扫描技能描述，并根据用户任务自动匹配；如果没有自动触发，可在提示中明确说“使用科研数据可视化技能”。

### Codex

Windows 用户可以把仓库复制到用户级 Codex skills 目录：

```powershell
git clone https://github.com/Nitrene123/scientific-data-visualization.git
$repo = Join-Path (Get-Location) "scientific-data-visualization"
$codexSkill = Join-Path $env:USERPROFILE ".codex\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $codexSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $codexSkill -Recurse -Force
```

关闭并重新打开 Codex 会话即可让它重新扫描 `SKILL.md`。若使用项目级 skills 目录，把同一仓库放到项目的 `.codex/skills/scientific-data-visualization/`，并确保 `SKILL.md` 位于该目录根部。

### Claude Code

把仓库复制到 Claude Code 的项目级 `.claude/skills/` 或用户级 `.claude/skills/`：

```powershell
$claudeSkill = Join-Path $env:USERPROFILE ".claude\skills\scientific-data-visualization"
New-Item -ItemType Directory -Force -Path $claudeSkill | Out-Null
Copy-Item -Path (Join-Path $repo "*") -Destination $claudeSkill -Recurse -Force
```

如果 Claude Code 使用独立项目根目录，将 `$claudeSkill` 改为 `<项目根目录>\.claude\skills\scientific-data-visualization`。例如本机独立安装可使用 `D:\claude-code-cn-plus\.claude\skills\scientific-data-visualization`。重新启动 Claude Code 会话后即可自动发现。

### 其他兼容 Agent

将整个仓库目录放入该 Agent 配置的 skills 目录，并保持以下结构：

~~~text
<skills-root>/scientific-data-visualization/
├── SKILL.md
├── scripts/
├── references/
└── assets/
~~~

Agent Skills 兼容实现通常读取 `SKILL.md` 的 `name` 和 `description` 作为匹配信息。若某个 Agent 只支持显式加载，请在其配置中添加此目录，或在对话中直接引用该技能名称。

### 自动加载检查

- 检查 `SKILL.md` 是否位于技能目录第一层，而不是嵌套在额外的仓库目录中。
- 新开会话或重启 Agent，使它重新扫描 skills 目录。
- 用“请使用科研数据可视化技能生成一个 3D 柱阵热力投影图”进行冒烟测试。
- 用 `python scripts/render_template.py --list` 检查 50 个模板是否可见。

## 模板分类

| 类别 | 代表模板 |
| --- | --- |
| 比较与分布 | `grouped-comparison`、`paired-raincloud`、`ridge-plot`、`forest-plot` |
| 关系与相关 | `hexbin-fit`、`correlation-pairgrid`、`bland-altman`、`ma-plot` |
| 组学与降维 | `expression-heatmap`、`volcano-plot`、`manhattan-plot`、`gsea-curve`、`umap-clusters`、`ordination-pcoa` |
| 分类与模型评估 | `confusion-matrix`、`cv-roc-ci`、`precision-recall-curve`、`calibration-reliability`、`det-curve`、`learning-curve` |
| 组成、流与层级 | `sankey-flow`、`nature-chord-diagram`、`treemap-hierarchy`、`sunburst-hierarchy`、`upset-plot`、`waterfall-contribution` |
| 时间、空间与网络 | `time-series-ribbon`、`event-timeline`、`survival-km`、`spatial-map`、`network-graph`、`ohlc-candlestick` |
| 三维与多变量 | `3d-bar-heatmap`、`3d-bar-heat-projection`、`3d-response-surface`、`3d-scatter`、`3d-volume`、`3d-vector-field`、`parallel-coordinates`、`radar-profile`、`ternary-composition` |
| 诊断与综合 | `residual-diagnostics`、`taylor-diagram`、`multiclass-shap-combo`、`prediction-marginal-grid`、`rf-tpe-surface`、`urban-park-cooling-combo`、`grouped-circular-heatmap`、`grouped-corr-split-violin` |

完整模板 ID、适用问题、数据要求和选图边界见 `references/figure-catalog.md` 与 `references/visualization-catalog.md`。

## 模板预览

以下缩略图直接对应 `assets/previews/` 中的 50 个模板预览文件；点击图片可查看原图。

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

## 输出格式

| 格式 | 适用场景 | 说明 |
| --- | --- | --- |
| PNG | 快速预览、汇报和文档 | 高清位图输出 |
| PDF | 论文排版和打印 | 矢量输出 |
| SVG | 后期编辑和网页 | 矢量输出 |

## 处理流程

1. 明确研究问题、观测单位、变量类型、分组/配对关系和不确定性含义。
2. 依据 `references/visualization-catalog.md` 选择最小且可解释的视觉语法。
3. 使用内置模板或复制最近模板后进行定制，保持标签、分组顺序、尺度和配色一致。
4. 同时导出 PNG/PDF/SVG，并检查文字、图例、坐标轴、色条、异常值和重叠情况。
5. 记录真实数据来源；模拟模板只能作为示例，不能当作实证结果。

## 使用限制

- 3D 图仅用于确有空间、时间、响应面或场数据含义的第三维；普通二维数据优先使用二维图。
- 连续色板应对应有序数值，发散色板应对应有意义的中心点；避免彩虹色和仅靠红绿区分。
- 模板内置数据是确定性模拟数据，不代表任何真实研究或用户数据。
- 对用户真实数据作图时，应在交付中说明数据来源、变换、缺失值处理和统计检验。

## 仓库结构

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

## 配色

`scripts/palette.py` 保留原项目色板作为默认主题。无序分类优先使用 `QUALITATIVE`，有序数值优先使用 `viridis` 或 `magma`，以有意义中点为基准的数据使用 `RdBu_r`。需要恢复历史图形风格时，不要在模板中另行定义一套互相冲突的颜色。

## 内容责任

本仓库提供可复现的科研制图模板和方法建议。示例数据仅用于演示；使用者应自行核对真实数据、统计假设、单位、图注和目标期刊规范。
