# 图形类型补充与选图研究笔记

**核对日期：2026-09-11**

本笔记用于扩展本技能的图形分类、选图边界和科研制图质控。联网检索优先采用官方文档：Matplotlib 的 `mplot3d` 说明了 3D 线、散点、网格、曲面、三角曲面、等高线、柱形和向量场等图元；Plotly 的官方图形对象文档进一步覆盖了 `Scatter3d`、`Surface`、`Mesh3d`、`Cone`、`Streamtube`、`Volume` 和 `Isosurface` 等三维轨迹与场数据表达。[Matplotlib mplot3d](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html) · [Matplotlib 3D gallery](https://matplotlib.org/stable/gallery/mplot3d/index.html) · [Plotly graph objects](https://plotly.com/python-api-reference/plotly.graph_objects.html)

## 已纳入可运行模板

| 类型 | 适用数据语义 | 当前模板 | 关键约束 |
| --- | --- | --- | --- |
| 三维柱阵/柱状热力图 | x、y 是离散轴，z 是强度/数量/响应 | `3d-bar-heatmap` | 3D 深度确实有解释价值；提供颜色标尺与轨迹的地面投影 |
| 三维响应面 | 两个连续输入 + 一个连续响应 | `3d-response-surface` | 表面、等高线、路径和地面投影需能互相校验 |
| Precision–Recall | 二分类，尤其是阳性类稀少 | `precision-recall-curve` | 与阳性率基线区分；报告 AP 或操作点 |
| 校准/可靠性图 | 概率预测是否与观测频率一致 | `calibration-reliability` | x 为平均预测概率，y 为实际阳性比例；下方显示预测分布 |
| Kaplan–Meier 生存曲线 | 时间到事件数据，含删失 | `survival-km` | 显示删失标记、置信区间和 at-risk 表 |
| 残差诊断组合图 | 回归/预测模型的适配性检查 | `residual-diagnostics` | 残差-拟合值、Q–Q、尺度位置、异常/影响筛查 |
| Manhattan 图 | 全基因组或分区索引的关联检验 | `manhattan-plot` | `−log10(p)` 轴、染色体分隔、阈值线与峰值标注 |
| 混淆矩阵 | 分类器在固定阈值下的类别错误结构 | `confusion-matrix` | 同时显示计数和行百分比；不要把颜色当作唯一信息 |
| Bland–Altman | 两测量方法的一致性与偏差随量级的变化 | `bland-altman` | bias、95% limits of agreement 和可接受误差范围 |
| MA 图 | 平均表达量与倍数变化的强度依赖结构 | `ma-plot` | 零线、效应阈值和显著/关注点编码 |
| 富集点图 | 通路富集的比例、基因数与显著性 | `enrichment-dotplot` | 横轴/大小/颜色分别承载不同语义 |
| Treemap / Sunburst | 父子层级中的组成和占比 | `treemap-hierarchy` | 面积编码总量，层级边界清楚 |
| 瀑布图 | 基线到终值的正负增量分解 | `waterfall-contribution` | 只有可加总贡献才使用 |
| 时间序列置信带 | 动态均值、不确定性和事件窗口 | `time-series-ribbon` | 区分观测波动、置信区间和预测区间 |
| 三维散点 | 三个真实坐标维度下的样本几何关系 | `3d-scatter` | 需配合视角、透明度或 2D 投影核查遮挡 |

校准图与 PR 图的统计含义参考 scikit-learn 官方用户指南：校准图横轴是平均预测概率、纵轴是对应组的阳性比例，PR 图用于在类别不平衡时观察 precision/recall 的权衡。[Calibration curves](https://scikit-learn.org/stable/modules/calibration.html) · [Precision–recall example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Kaplan–Meier 的拟合对象、置信区间和生存函数绘图接口参考 lifelines 官方文档。[lifelines Quickstart](https://lifelines.readthedocs.io/en/stable/Quickstart.html) · [KaplanMeierFitter](https://lifelines.readthedocs.io/en/stable/fitters/univariate/KaplanMeierFitter.html)

## 扩充后的图形分类地图

| 图形家族 | 常见子类型 | 典型科学问题 | 当前状态 |
| --- | --- | --- | --- |
| 三维几何与场 | 3D bar、bar + heat projection、scatter3d、wireframe、surface、trisurf、contour3D | 空间结构、双输入响应、三维采样与场 | 3D bar、柱阵热力投影、响应面已内置；其余可按选型规则定制 |
| 三维向量/流场 | quiver、cone、streamtube、流线 | 方向、速度、流动路径 | `3d-vector-field` 已内置；streamtube 仍需专用库或定制 |
| 三维体数据 | voxel、volume、isosurface、mesh | 体素、密度场、医学/工程体数据 | `3d-volume` 已内置；需体数据和遮挡控制 |
| 判别与概率质量 | ROC/CI、PR、DET、校准/可靠性、lift/gain | 判别能力、类别不平衡、概率可信度 | ROC、PR、校准、DET 已内置；lift/gain 待定制 |
| 学习与泛化 | learning curve、validation curve、误差收敛 | 数据量是否足够、偏差/方差与过拟合 | `learning-curve` 已内置 |
| 模型诊断与一致性 | 残差诊断、Q–Q、Bland–Altman、误差分布 | 模型假设、偏差、异方差、重复测量一致性 | 残差、Bland–Altman 已内置 |
| 生存与事件史 | Kaplan–Meier、累计风险、Nelson–Aalen、事件时间线 | 生存概率、风险累积、删失与事件时序 | KM、事件时间线已内置 |
| 组学富集轨迹 | GSEA running score、enrichment map、dot plot | 排名基因列表中的集合富集和峰值位置 | `gsea-curve` 与富集点图已内置 |
| 组学与遗传统计 | volcano、Manhattan、MA、染色体轨迹、clustergram | 差异、全基因组信号、表达与聚类 | volcano、Manhattan、热图已内置；MA 待定制 |
| 层级与组成 | sunburst、treemap、icicle、Sankey、parallel categories、ternary | 层级占比、状态流向、组成关系 | Sankey、ternary、parallel、treemap、sunburst 已内置；icicle 待定制 |
| 时间序列与金融 | 折线/带状、事件时间线、waterfall、OHLC、candlestick | 动态变化、贡献分解、价格与交易区间 | `event-timeline`、waterfall、`ohlc-candlestick` 已内置 |
| 空间与网络 | choropleth、点地图、网络、弦图、circos | 地理分布、节点关系、跨组连接 | 地图、网络、弦图已有 |

Plotly 官方 Python 分类页也将 scientific、statistical、financial、map、AI/ML 和 3D 图形分开组织，并提供 box/violin/ECDF、parallel categories、contour 等统计图族，可作为后续定制模板的候选清单。[Plotly Python chart types](https://plotly.com/python/) · [Statistical charts](https://plotly.com/python/statistical-charts/)

## 配色补充

当前库默认恢复原始模板风格：旧模板保留原有的蓝/青、暖红/橙和中性灰组合；新增模板使用 `scripts/palette.py` 中的兼容色板。有序数值使用 `viridis`/`magma`，围绕零或临界值的数据使用有明确中心的 `RdBu_r`。Matplotlib 官方将 sequential、diverging、cyclic、qualitative 分开定义，Seaborn 也明确建议按类别、有序数值和中心值选择不同色板。[Matplotlib colormap guide](https://matplotlib.org/stable/tutorials/colors/colormaps.html) · [Seaborn color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)

原来 33 个模板中相互独立的颜色已经按历史脚本恢复；新增模板使用共享 `scripts/palette.py` 的旧版兼容颜色：关键路径/阈值用暖红 `#C65D3B`，主数据用青蓝 `#2A7F9E`，正向元素用绿 `#3F9D54`，连续响应使用 `viridis`/`magma`。完整说明见 [references/palette-guide.md](palette-guide.md)。

## 3D 图的专项规则

1. 3D 不是默认的“高级版 2D”。只有第三维是空间坐标、时间/层级轴或有明确单位的响应量时才使用；如果目标是精确比较大小，优先 2D 热图、等高线或分面。
2. 三维柱阵适用于两个离散维度上的格点强度。柱子太密时降低柱宽、减少透视遮挡，并保留颜色标尺；需要定位热点时使用 `3d-bar-heat-projection`，让底部投影与柱体共享同一色标。
3. 三维响应面适用于两个连续输入与一个响应。表面应配合等高线、地面投影或关键点；红色路径只有在代表真实观测/优化/时间轨迹时才加入。
4. 大型 3D 散点、体数据和流场必须先处理遮挡、采样密度和视角敏感性；同一结论最好提供 2D 投影或切片作为可核查补充。

## 科研出版质量检查

Nature Research Figure Guide 建议最终尺寸下的字体和刻度可读、坐标轴有单位、使用可访问的配色、减少不必要的复杂性，并优先提交可编辑矢量图和清晰的图组布局。[Preparing figures](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/) · [Building and exporting figure panels](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/) · [Nature formatting guide](https://www.nature.com/nature/for-authors/formatting-guide?trk=public_post-text)

本 skill 的模板因此统一遵守：确定性模拟数据、PNG/PDF/SVG 三种输出、坐标轴与单位、明确图例/阈值/不确定性含义、避免标签重叠，以及把 3D 图的投影线与图例写清楚。所有模板的模拟值仅用于版式与代码示例，不应被当作真实研究结果。

补充的 3D 体素与向量场模板也遵循“数据结构先于立体效果”的规则：规则网格才用 voxel，真实方向/速度分量才用 quiver；如果用户只有二维表格或二维点，优先降级为热图、等高线、散点或分面图。
