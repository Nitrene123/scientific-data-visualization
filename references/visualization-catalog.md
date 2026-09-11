# 可视化图片分类索引

**本文件可独立使用。** 下面的图形家族分类、识别边界与选图建议自成体系，
不依赖任何外部素材；表里的「代表编号」只是对某批参考图集的索引，图集不在也能正常选图。

> 图集来源（**可选、外部、可能已不存在**）：某次微信收发的 `可视化图片.zip`（139 张 PNG）
> 与 `可视化图片(1).zip`（148 张）。这些是使用者本机路径下的私人物料，**不随本 skill 分发**。
> 若该路径不存在，直接忽略「代表编号」列，用左侧的图形家族与用途列选图即可；
> 需要具体版式参考时，改用本 skill 自带的 `assets/previews/`（见下）与 `plot-recipes.md`。

编号按压缩包中文件的时间序列（22:20:24 至 23:07:45）排列，而非图片上写的“案例”号。复合图可出现在多个类别中，故下表的编号允许重叠。

## 随 skill 分发的版式参考（`assets/previews/`）

以下 50 张是**实际可运行的模板渲染结果**，比外部图集更可靠——它们与本 skill 的
`scripts/templates/` 一一对应，可直接对照版式并立即复现：

| 预览图 | 对应模板 id |
|---|---|
| `paired_raincloud_replica.png` | `paired-raincloud` 配对云雨图 |
| `cv_roc_ci_replica.png` | `cv-roc-ci` 交叉验证 ROC 与置信区间 |
| `taylor_diagram_replica.png` | `taylor-diagram` 泰勒图 |
| `correlation_pairgrid_replica.png` | `correlation-pairgrid` 相关矩阵组合图 |
| `prediction_marginal_grid_replica.png` | `prediction-marginal-grid` 预测/真实值边缘分布 |
| `rf_tpe_surface_replica.png` | `rf-tpe-surface` TPE 调参 3D 曲面 |
| `grouped_corr_split_violin_replica.png` | `grouped-corr-split-violin` 下三角相关矩阵+半边小提琴 |
| `grouped_circular_heatmap_replica.png` | `grouped-circular-heatmap` 分组环形热图 |
| `urban_park_cooling_combo_replica.png` | `urban-park-cooling-combo` 堆叠+云雨+箱线组合 |
| `nature_chord_diagram_replica.png` | `nature-chord-diagram` Nature 风格和弦图 |
| `multiclass_shap_combo_replica.png` | `multiclass-shap-combo` 多分类 SHAP 组合图 |
| `grouped_comparison_replica.png` | `grouped-comparison` 分组比较、原始点与 95% CI |
| `ridge_plot_replica.png` | `ridge-plot` 多组密度山脊图 |
| `hexbin_fit_replica.png` | `hexbin-fit` 大样本密度与拟合趋势 |
| `expression_heatmap_replica.png` | `expression-heatmap` 表达矩阵热图 |
| `ordination_pcoa_replica.png` | `ordination-pcoa` PCoA 主坐标散点 |
| `umap_clusters_replica.png` | `umap-clusters` UMAP 聚类嵌入 |
| `volcano_plot_replica.png` | `volcano-plot` 差异分析火山图 |
| `forest_plot_replica.png` | `forest-plot` 估计值与置信区间 |
| `sankey_flow_replica.png` | `sankey-flow` 状态流向 |
| `network_graph_replica.png` | `network-graph` 节点—边网络 |
| `spatial_map_replica.png` | `spatial-map` 区域空间分布 |
| `upset_plot_replica.png` | `upset-plot` 集合交集 |
| `ternary_composition_replica.png` | `ternary-composition` 三部分组成 |
| `parallel_coordinates_replica.png` | `parallel-coordinates` 多指标轮廓 |
| `radar_profile_replica.png` | `radar-profile` 多对象雷达轮廓 |
| `3d_bar_heatmap_replica.png` | `3d-bar-heatmap` 三维柱阵与轨迹地面投影 |
| `3d_bar_heat_projection_replica.png` | `3d-bar-heat-projection` 三维柱阵与底部热力投影 |
| `3d_response_surface_replica.png` | `3d-response-surface` 三维响应面与路径投影 |
| `precision_recall_curve_replica.png` | `precision-recall-curve` PR 曲线 |
| `calibration_reliability_replica.png` | `calibration-reliability` 校准/可靠性图 |
| `survival_km_replica.png` | `survival-km` Kaplan–Meier 生存曲线 |
| `residual_diagnostics_replica.png` | `residual-diagnostics` 回归残差诊断 |
| `manhattan_plot_replica.png` | `manhattan-plot` 全基因组关联峰图 |
| `confusion_matrix_replica.png` | `confusion-matrix` 分类错误结构 |
| `bland_altman_replica.png` | `bland-altman` 两方法一致性 |
| `ma_plot_replica.png` | `ma-plot` 平均表达与 fold change |
| `enrichment_dotplot_replica.png` | `enrichment-dotplot` 通路富集点图 |
| `treemap_hierarchy_replica.png` | `treemap-hierarchy` 层级组成树图 |
| `waterfall_contribution_replica.png` | `waterfall-contribution` 贡献分解瀑布图 |
| `time_series_ribbon_replica.png` | `time-series-ribbon` 时间序列与不确定性 |
| `3d_scatter_replica.png` | `3d-scatter` 三维聚类散点 |
| `3d_volume_replica.png` | `3d-volume` 三维体素/阈值体数据 |
| `3d_vector_field_replica.png` | `3d-vector-field` 三维向量场 |
| `det_curve_replica.png` | `det-curve` 检测错误率权衡 |
| `learning_curve_replica.png` | `learning-curve` 学习/泛化曲线 |
| `gsea_curve_replica.png` | `gsea-curve` 基因集富集曲线 |
| `sunburst_hierarchy_replica.png` | `sunburst-hierarchy` 父子层级旭日图 |
| `event_timeline_replica.png` | `event-timeline` 事件时间线 |
| `ohlc_candlestick_replica.png` | `ohlc-candlestick` OHLC/K 线 |

| 图形家族 | 典型用途 | 图集中代表编号 |
|---|---|---|
| 点图、柱状图与带误差比较图 | 处理组或类别均值/比例比较 | 001、005–007、020、033、035、059、069、074–076 |
| 双 Y 轴组合图 | 两个不同量纲随同一自变量变化 | 006–007 |
| 折线、平滑与时间/剂量曲线 | 动态、剂量反应、非线性关系 | 003、054–057、066–068、079–081 |
| 散点、回归与边际分布图 | 两连续变量的关联、校准或拟合 | 017–018、022、026、030–031、036、044、052–053、063–064、082–084、088、104–106 |
| 气泡图 | 在二维关系中额外编码规模或权重 | 008、026、063–064、105–106、118 |
| 箱线、小提琴、雨云与蜂群图 | 组内分布、离散度与原始观测 | 004、024–025、032、060–061、070–072、123–125 |
| 山脊图/密度脊线 | 多组连续分布的横向比较 | 013–015、021、054、060–061、070–072 |
| 二维密度、hexbin 与等高线 | 大量点的局部密度和相关结构 | 017–018、036、104–105 |
| 热图与表达矩阵 | 多变量强度、样本—特征模式 | 008、016、019、026、097–098、107–110、121–123、137 |
| 相关矩阵与相关性面板 | 变量两两相关方向和强度 | 034、089–091、121–122、132–134 |
| 聚类热图/树状热图 | 依据相似性组织样本或特征 | 019、034、089、097–098、107–110 |
| PCA/PCoA、NMDS 与 UMAP | 高维样本或细胞的低维嵌入 | 002、085、126、131–133、139 |
| 火山图及火山图组合 | 差异分析的效应量与显著性筛选 | 028、099–104、113–115、127–128、138 |
| 森林图 | 多个估计量及其区间的横向比较 | 058、086–087、134、136 |
| Sankey / Alluvial | 类别、状态或组成的流向和转化 | 037–038、046–047、093 |
| 堆叠条形图 | 组成在样本/分组间的变化 | 069、074–076、099–101 |
| 网络图与弦图 | 节点关系、相互作用或跨组连接 | 023、027–029、045–047、091、135 |
| 环形树、circos 与环形热图 | 层级、谱系和多轨道注释 | 009–012、039–040、094–097、102–103、135 |
| 雷达图/径向多边形图 | 少量对象在共同指标集上的轮廓比较 | 051、088、100–101 |
| 径向柱形图 | 环形类别的大小或频次 | 039–040、092、102–103 |
| 地图与空间分布图 | 地理位置、区域比较、空间采样 | 041–043、049–050、108–109 |
| UpSet 图 | 多集合交集及其基数 | 116–117 |
| 三元图 | 三部分组成、比例或相对丰度 | 126–130 |
| 平行坐标图 | 多指标轮廓和样本路径 | 131 |
| 3D 图/三维散点面板 | 三维结构或多视角空间比较 | 135 |
| 配对散点/重复测量连接图 | 同一样本在多条件下的变化 | 130 |
| 三维柱阵/柱状热力图 | 两个离散轴上的强度、数量或响应，并叠加真实轨迹/投影 | 135 |
| 三维响应面与路径投影 | 两个连续输入对响应的联合影响、优化路径或观测轨迹 | 135 |
| Precision–Recall 曲线 | 类别不平衡下的检出率与阳性预测值权衡 | — |
| 校准/可靠性图 | 预测概率与实际阳性比例是否一致 | — |
| Kaplan–Meier 生存曲线 | 含删失的时间到事件差异 | — |
| 残差诊断组合图 | 回归模型的异方差、非正态、异常和影响点 | — |
| Manhattan 图 | 全基因组关联检验的染色体峰值与阈值 | — |
| 混淆矩阵 | 分类器的 TP、TN、FP、FN 结构与类别级错误 | — |
| Bland–Altman 一致性图 | 两种测量方法的偏差、限度与随量级变化的差异 | — |
| MA 图 | 平均丰度/表达量与倍数变化的关系 | — |
| 富集点图 | 通路、富集比例、基因数和多重校正显著性 | — |
| Treemap / Sunburst | 层级组成、占比和父子结构 | — |
| 瀑布图 | 基线到最终结果的正负增量分解 | — |
| 时间序列置信带 | 动态变化、预测不确定性和事件窗口 | — |
| 三维散点 | 三个真实坐标维度下的空间/几何聚类 | — |
| 三维体数据/体素 | 体素网格中的密度、信号或结构 | — |
| 三维向量场 | 速度、方向、力场或流动方向 | — |
| DET 曲线 | 假阳性率与假阴性率的检测权衡 | — |
| 学习曲线 | 训练样本规模与训练/验证性能的收敛关系 | — |
| GSEA 运行得分曲线 | 排序列表中的基因集富集位置与峰值 | — |
| Sunburst 旭日图 | 多级父子层级的组成和占比 | — |
| 事件时间线 | 阶段区间、关键里程碑和事件先后 | — |
| OHLC/K 线 | 开盘、最高、最低、收盘四值的时间变化 | — |

## 快速识别边界

- **山脊图 vs 小提琴图**：前者沿一个公共连续轴排列多个密度曲线；后者围绕类别轴对称显示单组密度。
- **热图 vs 相关矩阵**：二者都用颜色编码矩阵；只有行列为同一变量集合、单元格表达相关时才称相关矩阵。
- **网络图 vs 弦图 vs Sankey**：网络强调任意节点关系；弦图是圆形节点关系；Sankey 强调有方向或阶段顺序的流量守恒。
- **PCA/PCoA/NMDS/UMAP**：都呈现低维坐标，但数学含义不同；图注必须写算法、输入变换和距离/邻居设置，不能统称“降维图”。
- **火山图 vs 普通散点**：火山图固定为效应量对显著性（通常 `-log10(p)` 或校正后 p 值）；若坐标不满足此语义，应称散点图。
- **雷达图 vs 径向柱形图**：雷达图用多维顶点形成轮廓；径向柱形图以扇形长度/半径表示单变量大小。
- **3D 柱阵 vs 2D 热图**：仅当高度或透视关系本身帮助解释第三维时保留 3D；密集格点的精确比较通常用 2D 热图或等高线更可靠。
- **3D 柱阵热力投影**：当离散 x/y 矩阵既需要柱高表达响应量、又需要快速定位热点时，可在柱阵底部加入同一矩阵的热力/等高线投影；投影必须使用同一色标，不能用两套独立数值含义。
- **3D 响应面 vs 普通曲面图**：响应面必须有两个连续输入和有单位/语义的响应轴；表面配合等高线、地面投影或关键路径，避免只用透视效果制造“立体感”。
- **PR vs ROC vs 校准图**：PR 关注不平衡分类中的 precision/recall；ROC 关注阈值下的区分能力；校准图关注概率是否可信，三者不能互相替代。
- **Kaplan–Meier vs 时间序列折线**：KM 处理含删失的事件时间，需显示生存估计、删失标记和风险集；没有删失/事件语义时用普通时间序列。
- **混淆矩阵 vs ROC/PR**：混淆矩阵展示单个阈值下的错误构成；ROC/PR 展示跨阈值权衡，不能用一个替代另一个。
- **MA vs 火山图**：MA 保留平均丰度结构，适合检查强度依赖偏差；火山图强调效应量与显著性筛选。
- **富集点图 vs 普通气泡图**：富集点图的横轴、点大小和颜色必须分别有基因比例/计数/显著性语义。
- **瀑布图 vs 堆叠条形图**：瀑布图强调可加总的增量链条；普通组成比例没有基线到终值的加法关系时不要使用瀑布图。
- **Treemap vs Sunburst**：二者都表达层级组成；矩形面积适合精确比较，旭日环更适合强调父子路径和层级深度。
- **学习曲线 vs 时间序列**：学习曲线横轴是训练集规模，目标是泛化/收敛；普通时间序列横轴是时间或事件顺序，不能混用。
- **3D 体素 vs 3D 响应面**：体素要求规则三维网格，响应面要求两个输入与一个连续响应；没有相应数据结构时降级为 2D。

## 本批图集的结构特征

这批素材明显偏向生命科学与组学论文图：相关/表达矩阵、环形多轨道图、降维嵌入、火山图、富集组合图和差异丰度图占比较高。它们适合借鉴版式和信息层次，但不是普通表格数据的默认首选；对少量类别或简单比较，应优先用点图、区间图、散点图或分布图。

## 联网检索补充与规范（2026-09-11）

本次新增分类优先核对官方资料：Matplotlib 的 [mplot3d 工具包](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html) 和 [3D gallery](https://matplotlib.org/stable/gallery/mplot3d/index.html) 覆盖 3D 柱、散点、网格、曲面、三角曲面、等高线、向量场和体数据等基本图元；Plotly 的 [Python 图形分类](https://plotly.com/python/) 与 [graph objects API](https://plotly.com/python-api-reference/plotly.graph_objects.html) 补充了三维轨迹、网格、体积/等值面、统计图和层级图的命名体系。

概率图和生存图的边界参考 [scikit-learn calibration guide](https://scikit-learn.org/stable/modules/calibration.html)、[scikit-learn PR example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html) 与 [lifelines Kaplan–Meier 文档](https://lifelines.readthedocs.io/en/stable/fitters/univariate/KaplanMeierFitter.html)。出版级版式按 Nature Research Figure Guide 的 [preparing figures](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/) 和 [figure panels](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/) 执行：最终尺寸下可读、坐标轴有单位、配色可访问、图组布局清楚，并优先保留可编辑矢量文本。

更完整的“已内置 / 待定制”清单、3D 专项规则和检查项见 [references/chart-types-research.md](chart-types-research.md)。
统一色板与连续/发散/定类色图的使用见 [references/palette-guide.md](palette-guide.md)。

## 第二批补充：`可视化图片(1).zip`

第二包含 148 张 PNG。按文件名和 SHA-256 核验，其中 12 张是首包未出现的新图；另有 3 张首包图片未被包含。因此本索引保留首包内容，并将下列 12 张作为补充样本。时间码取自文件名末尾，避免与首包编号混淆。

| 时间码 | 图片标题中的主要类型 | 分类归属 | 可借鉴的信息 |
|---|---|---|---|
| 000725 | PCoA 图 | PCA/PCoA、NMDS 与 UMAP | 主坐标散点结合组别、边际箱线图和解释度标注 |
| 000739 | 分组柱状图 | 点图、柱状图与带误差比较图 | 多指标分面比较、误差条与显著性注释 |
| 000755 | 分组柱形图 | 点图、柱状图与带误差比较图 | 多处理组比较与统一色彩编码 |
| 000817 | 相关性热图 | 相关矩阵与相关性面板 | 聚类排序、下三角矩阵与边际汇总 |
| 000828 | 火山图 | 火山图及火山图组合 | 阈值线、差异方向和富集结果的联动 |
| 000837 | 山脊图 | 山脊图/密度脊线 | 组间密度对照，并配合排序条形汇总 |
| 000853 | 小提琴图 | 箱线、小提琴、雨云与蜂群图 | 多组分面、原始点和检验标记 |
| 000927 | 密度图 | 二维密度、hexbin 与等高线 | 二维核密度与边际分布的联合呈现 |
| 000941 | 散点附图 | 散点、回归与边际分布图 | 多面板散点、分组颜色与边际统计 |
| 001024 | 时间序列图 | 折线、平滑与时间/剂量曲线 | 干预前后曲线、置信带和事件参考线 |
| 001059 | 相关性矩阵图 | 相关矩阵与相关性面板 | 相关系数、显著性和效应方向的联合编码 |
| 001439 | 时间序列图 | 折线、平滑与时间/剂量曲线 | 与 001024 互补的重复测量曲线版式 |
