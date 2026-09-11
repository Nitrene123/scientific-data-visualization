# 科研数据可视化

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
