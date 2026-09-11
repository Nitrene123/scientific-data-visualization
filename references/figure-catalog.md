# Figure Template Catalog

Each id maps to a bundled script under `scripts/templates/`.

| id | script | figure |
| --- | --- | --- |
| `multiclass-shap-combo` | `make_multiclass_shap_combo.py` | 多分类 SHAP 柱状图与蜂群图组合图 |
| `paired-raincloud` | `make_paired_raincloud.py` | 配对云雨图 |
| `cv-roc-ci` | `make_cv_roc_ci.py` | 交叉验证 ROC 曲线与置信区间图 |
| `taylor-diagram` | `make_taylor_diagram.py` | 多模型评价泰勒图 |
| `correlation-pairgrid` | `make_correlation_pairgrid.py` | 数据分布、拟合线、置信区间、相关系数组合图 |
| `prediction-marginal-grid` | `make_prediction_marginal_grid.py` | 预测值与真实值边缘分布组合图 |
| `rf-tpe-surface` | `make_rf_tpe_surface.py` | TPE 优化 RF 模型 3D 曲面图 |
| `grouped-corr-split-violin` | `make_grouped_corr_split_violin.py` | 下三角相关矩阵 + 特征分组与半边小提琴图 |
| `grouped-circular-heatmap` | `make_grouped_circular_heatmap.py` | 分组环形热图 |
| `urban-park-cooling-combo` | `make_urban_park_cooling_combo.py` | 堆叠图 + 云雨图 + 箱线图组合图 |
| `nature-chord-diagram` | `make_nature_chord_diagram.py` | Nature 风格和弦图 |
| `grouped-comparison` | `make_grouped_comparison.py` | 分组比较、原始点、均值与 95% CI |
| `ridge-plot` | `make_ridge_plot.py` | 多组山脊密度图 |
| `hexbin-fit` | `make_hexbin_fit.py` | 大样本 hexbin 密度与拟合趋势 |
| `expression-heatmap` | `make_expression_heatmap.py` | 表达矩阵/特征强度热图 |
| `ordination-pcoa` | `make_ordination_pcoa.py` | PCoA 主坐标散点与组间椭圆 |
| `umap-clusters` | `make_umap_clusters.py` | UMAP 聚类嵌入图 |
| `volcano-plot` | `make_volcano_plot.py` | 差异分析火山图 |
| `forest-plot` | `make_forest_plot.py` | 估计值与置信区间森林图 |
| `sankey-flow` | `make_sankey_flow.py` | 状态转化 Sankey/Alluvial 流向图 |
| `network-graph` | `make_network_graph.py` | 节点—边相互作用网络图 |
| `spatial-map` | `make_spatial_map.py` | 区域与采样强度空间地图 |
| `upset-plot` | `make_upset_plot.py` | 多集合交集 UpSet 图 |
| `ternary-composition` | `make_ternary_composition.py` | 三部分组成三元图 |
| `parallel-coordinates` | `make_parallel_coordinates.py` | 多指标平行坐标图 |
| `radar-profile` | `make_radar_profile.py` | 多对象指标雷达图 |
| `3d-bar-heatmap` | `make_3d_bar_heatmap.py` | 三维柱阵/热力强度与轨迹投影 |
| `3d-bar-heat-projection` | `make_3d_bar_heat_projection.py` | 三维柱阵 + 底部热力/等高线投影 |
| `3d-response-surface` | `make_3d_response_surface.py` | 多面板三维响应面与路径投影 |
| `precision-recall-curve` | `make_precision_recall_curve.py` | 类别不平衡下的 Precision–Recall 曲线 |
| `calibration-reliability` | `make_calibration_reliability.py` | 概率预测校准/可靠性图与预测分布 |
| `survival-km` | `make_survival_km.py` | Kaplan–Meier 生存曲线、置信区间与风险表 |
| `residual-diagnostics` | `make_residual_diagnostics.py` | 回归残差、Q–Q、尺度位置与异常诊断组合图 |
| `manhattan-plot` | `make_manhattan_plot.py` | 全基因组关联检验 Manhattan 图 |
| `confusion-matrix` | `make_confusion_matrix.py` | 分类错误结构混淆矩阵与行百分比 |
| `bland-altman` | `make_bland_altman.py` | 两种测量方法的一致性 Bland–Altman 图 |
| `ma-plot` | `make_ma_plot.py` | 平均表达量与 log2 fold change 的 MA 图 |
| `enrichment-dotplot` | `make_enrichment_dotplot.py` | 通路富集比、基因数与显著性点图 |
| `treemap-hierarchy` | `make_treemap_hierarchy.py` | 层级组成矩形树图（兼容旭日图选型） |
| `waterfall-contribution` | `make_waterfall_contribution.py` | 正负贡献分解瀑布图 |
| `time-series-ribbon` | `make_time_series_ribbon.py` | 时间序列、置信带与事件窗口 |
| `3d-scatter` | `make_3d_scatter.py` | 三维聚类散点与中心点 |
| `3d-volume` | `make_3d_volume.py` | 三维体素/阈值体数据 |
| `3d-vector-field` | `make_3d_vector_field.py` | 三维向量场与 quiver 箭头 |
| `det-curve` | `make_det_curve.py` | 检测错误率 FPR/FNR 权衡曲线 |
| `learning-curve` | `make_learning_curve.py` | 训练集规模与泛化性能曲线 |
| `gsea-curve` | `make_gsea_curve.py` | 基因集富集运行得分曲线 |
| `sunburst-hierarchy` | `make_sunburst_hierarchy.py` | 父子层级旭日图 |
| `event-timeline` | `make_event_timeline.py` | 阶段区间、里程碑与事件时间线 |
| `ohlc-candlestick` | `make_ohlc_candlestick.py` | OHLC/K 线价格区间图 |

Prompts from the MathModel Improve tab should include `$mathmodel-figure-templates` and the human-readable figure title. The agent should convert that title to one of the ids above and call `scripts/render_template.py`.

## 版式预览

每个模板都附有一张实际渲染结果，位于 `assets/previews/<id>_replica.png`（下划线形式，如
`paired_raincloud_replica.png`）。**选型前先看预览图**，比读文字描述可靠得多：

| id | 预览文件 |
|---|---|
| `paired-raincloud` | `assets/previews/paired_raincloud_replica.png` |
| `cv-roc-ci` | `assets/previews/cv_roc_ci_replica.png` |
| `taylor-diagram` | `assets/previews/taylor_diagram_replica.png` |
| `correlation-pairgrid` | `assets/previews/correlation_pairgrid_replica.png` |
| `prediction-marginal-grid` | `assets/previews/prediction_marginal_grid_replica.png` |
| `rf-tpe-surface` | `assets/previews/rf_tpe_surface_replica.png` |
| `grouped-corr-split-violin` | `assets/previews/grouped_corr_split_violin_replica.png` |
| `grouped-circular-heatmap` | `assets/previews/grouped_circular_heatmap_replica.png` |
| `urban-park-cooling-combo` | `assets/previews/urban_park_cooling_combo_replica.png` |
| `nature-chord-diagram` | `assets/previews/nature_chord_diagram_replica.png` |
| `multiclass-shap-combo` | `assets/previews/multiclass_shap_combo_replica.png` |
| `grouped-comparison` | `assets/previews/grouped_comparison_replica.png` |
| `ridge-plot` | `assets/previews/ridge_plot_replica.png` |
| `hexbin-fit` | `assets/previews/hexbin_fit_replica.png` |
| `expression-heatmap` | `assets/previews/expression_heatmap_replica.png` |
| `ordination-pcoa` | `assets/previews/ordination_pcoa_replica.png` |
| `umap-clusters` | `assets/previews/umap_clusters_replica.png` |
| `volcano-plot` | `assets/previews/volcano_plot_replica.png` |
| `forest-plot` | `assets/previews/forest_plot_replica.png` |
| `sankey-flow` | `assets/previews/sankey_flow_replica.png` |
| `network-graph` | `assets/previews/network_graph_replica.png` |
| `spatial-map` | `assets/previews/spatial_map_replica.png` |
| `upset-plot` | `assets/previews/upset_plot_replica.png` |
| `ternary-composition` | `assets/previews/ternary_composition_replica.png` |
| `parallel-coordinates` | `assets/previews/parallel_coordinates_replica.png` |
| `radar-profile` | `assets/previews/radar_profile_replica.png` |
| `3d-bar-heatmap` | `assets/previews/3d_bar_heatmap_replica.png` |
| `3d-bar-heat-projection` | `assets/previews/3d_bar_heat_projection_replica.png` |
| `3d-response-surface` | `assets/previews/3d_response_surface_replica.png` |
| `precision-recall-curve` | `assets/previews/precision_recall_curve_replica.png` |
| `calibration-reliability` | `assets/previews/calibration_reliability_replica.png` |
| `survival-km` | `assets/previews/survival_km_replica.png` |
| `residual-diagnostics` | `assets/previews/residual_diagnostics_replica.png` |
| `manhattan-plot` | `assets/previews/manhattan_plot_replica.png` |
| `confusion-matrix` | `assets/previews/confusion_matrix_replica.png` |
| `bland-altman` | `assets/previews/bland_altman_replica.png` |
| `ma-plot` | `assets/previews/ma_plot_replica.png` |
| `enrichment-dotplot` | `assets/previews/enrichment_dotplot_replica.png` |
| `treemap-hierarchy` | `assets/previews/treemap_hierarchy_replica.png` |
| `waterfall-contribution` | `assets/previews/waterfall_contribution_replica.png` |
| `time-series-ribbon` | `assets/previews/time_series_ribbon_replica.png` |
| `3d-scatter` | `assets/previews/3d_scatter_replica.png` |
| `3d-volume` | `assets/previews/3d_volume_replica.png` |
| `3d-vector-field` | `assets/previews/3d_vector_field_replica.png` |
| `det-curve` | `assets/previews/det_curve_replica.png` |
| `learning-curve` | `assets/previews/learning_curve_replica.png` |
| `gsea-curve` | `assets/previews/gsea_curve_replica.png` |
| `sunburst-hierarchy` | `assets/previews/sunburst_hierarchy_replica.png` |
| `event-timeline` | `assets/previews/event_timeline_replica.png` |
| `ohlc-candlestick` | `assets/previews/ohlc_candlestick_replica.png` |
