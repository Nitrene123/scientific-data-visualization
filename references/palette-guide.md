# scibox-figure 原始配色规范

当前库默认恢复原始模板的视觉语言。旧模板保留各自的原始色值；新增模板
使用下列兼容色板。配色先服从数据语义，再考虑装饰性：

| 数据语义 | 默认选择 | 适用例子 |
| --- | --- | --- |
| 无序类别 | `QUALITATIVE`（深紫、砖红、棕橙、绿、靛蓝、青蓝、浅蓝、灰） | 分组散点、网络节点、模型比较 |
| 有序数值 | `viridis` 或 `magma` | 热图、空间强度、密度 |
| 连续 3D 柱阵/热力投影 | `THREED` | `3d-bar-heatmap`、`3d-bar-heat-projection` |
| 围绕临界点/零值 | `RdBu_r`，并固定中心 | 相关、差异、残差、效应量 |
| 强调路径/阈值 | `HIGHLIGHT = #C65D3B` | 轨迹、阈值线、关键标注 |
| 背景和辅助线 | `PANEL`、`GRID`、`MUTED` | 面板底色、网格、说明文字 |

## 3D 专用连续色板

`THREED` 是参考图风格的连续色图：低值从浅薄荷绿/青绿色开始，中间过渡到黄绿色和黄色，高值进入暖橙与砖红。当前仅用于 `3d-bar-heatmap` 与 `3d-bar-heat-projection`，能同时保留低值区域的层次和高值峰值的醒目度。3D 聚类散点仍使用 `QUALITATIVE`，因为颜色表达的是类别而不是数值大小。

## 当前两类来源

| 色板来源 | 当前处理 |
| --- | --- |
| 原始模板色板 | 原有 33 个模板已恢复其原始脚本中的颜色与色图；新增模板按相同的蓝/青、暖红/橙、灰色语言补齐 |
| 统一优化色板 | 本次不作为默认使用；此前的统一优化值不覆盖当前原始风格 |

## 硬性规则

- 禁止把彩虹色图、红绿配对作为默认编码；类别同时使用颜色和图例/形状语义。
- 连续变量不能使用定类色板；有序变量不能用随机类别色。
- 发散色图必须有明确的中心值（通常为 0），并使用对称或解释清楚的范围。
- 线条、置信带和散点的透明度只负责层次，不应让关键颜色变成难以辨识的浅灰。
- 最终缩小到论文版面后仍需区分；必要时用线型、点型、直接标注补充颜色信息。

实现位置：`scripts/palette.py`。模板通过渲染器复制该文件到项目的 `scripts/`，因此新增或自定义模板也可直接 `from palette import ...`。

选择依据：即使恢复原始风格，仍按数据语义选择定类、连续和发散色图；Matplotlib 将色图分为 sequential、diverging、cyclic、qualitative，Seaborn 进一步区分定类、连续和发散色板，Nature Figure Guide 要求考虑色盲可访问性。[Matplotlib colormap guide](https://matplotlib.org/stable/tutorials/colors/colormaps.html) · [Seaborn color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html) · [Nature accessibility guidance](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/)
