#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def _fix_console_encoding():
    """Windows 控制台默认 GBK；直接 print('✓') 会 UnicodeEncodeError 并中断后续步骤
    （表现为前半段有产物、后半段静默消失）。这里把输出流切到 UTF-8 兜住。"""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


_fix_console_encoding()

SCRIPT_MAP = {
    "multiclass-shap-combo": "make_multiclass_shap_combo.py",
    "paired-raincloud": "make_paired_raincloud.py",
    "cv-roc-ci": "make_cv_roc_ci.py",
    "taylor-diagram": "make_taylor_diagram.py",
    "correlation-pairgrid": "make_correlation_pairgrid.py",
    "prediction-marginal-grid": "make_prediction_marginal_grid.py",
    "rf-tpe-surface": "make_rf_tpe_surface.py",
    "grouped-corr-split-violin": "make_grouped_corr_split_violin.py",
    "grouped-circular-heatmap": "make_grouped_circular_heatmap.py",
    "urban-park-cooling-combo": "make_urban_park_cooling_combo.py",
    "nature-chord-diagram": "make_nature_chord_diagram.py",
    "grouped-comparison": "make_grouped_comparison.py",
    "ridge-plot": "make_ridge_plot.py",
    "hexbin-fit": "make_hexbin_fit.py",
    "expression-heatmap": "make_expression_heatmap.py",
    "ordination-pcoa": "make_ordination_pcoa.py",
    "umap-clusters": "make_umap_clusters.py",
    "volcano-plot": "make_volcano_plot.py",
    "forest-plot": "make_forest_plot.py",
    "sankey-flow": "make_sankey_flow.py",
    "network-graph": "make_network_graph.py",
    "spatial-map": "make_spatial_map.py",
    "upset-plot": "make_upset_plot.py",
    "ternary-composition": "make_ternary_composition.py",
    "parallel-coordinates": "make_parallel_coordinates.py",
    "radar-profile": "make_radar_profile.py",
    "3d-bar-heatmap": "make_3d_bar_heatmap.py",
    "3d-bar-heat-projection": "make_3d_bar_heat_projection.py",
    "3d-response-surface": "make_3d_response_surface.py",
    "precision-recall-curve": "make_precision_recall_curve.py",
    "calibration-reliability": "make_calibration_reliability.py",
    "survival-km": "make_survival_km.py",
    "residual-diagnostics": "make_residual_diagnostics.py",
    "manhattan-plot": "make_manhattan_plot.py",
    "confusion-matrix": "make_confusion_matrix.py",
    "bland-altman": "make_bland_altman.py",
    "ma-plot": "make_ma_plot.py",
    "enrichment-dotplot": "make_enrichment_dotplot.py",
    "treemap-hierarchy": "make_treemap_hierarchy.py",
    "waterfall-contribution": "make_waterfall_contribution.py",
    "time-series-ribbon": "make_time_series_ribbon.py",
    "3d-scatter": "make_3d_scatter.py",
    "3d-volume": "make_3d_volume.py",
    "3d-vector-field": "make_3d_vector_field.py",
    "det-curve": "make_det_curve.py",
    "learning-curve": "make_learning_curve.py",
    "gsea-curve": "make_gsea_curve.py",
    "sunburst-hierarchy": "make_sunburst_hierarchy.py",
    "event-timeline": "make_event_timeline.py",
    "ohlc-candlestick": "make_ohlc_candlestick.py",
}

ALIASES = {
    "shap": "multiclass-shap-combo",
    "multiclass-shap": "multiclass-shap-combo",
    "raincloud": "paired-raincloud",
    "roc": "cv-roc-ci",
    "cv-roc": "cv-roc-ci",
    "taylor": "taylor-diagram",
    "pairgrid": "correlation-pairgrid",
    "correlation": "correlation-pairgrid",
    "pred-true": "prediction-marginal-grid",
    "prediction": "prediction-marginal-grid",
    "surface": "rf-tpe-surface",
    "tpe": "rf-tpe-surface",
    "split-violin": "grouped-corr-split-violin",
    "circular-heatmap": "grouped-circular-heatmap",
    "urban-cooling": "urban-park-cooling-combo",
    "chord": "nature-chord-diagram",
    "circos": "nature-chord-diagram",
    "comparison": "grouped-comparison",
    "group-comparison": "grouped-comparison",
    "ridge": "ridge-plot",
    "density-ridge": "ridge-plot",
    "hexbin": "hexbin-fit",
    "density": "hexbin-fit",
    "heatmap": "expression-heatmap",
    "expression": "expression-heatmap",
    "pcoa": "ordination-pcoa",
    "ordination": "ordination-pcoa",
    "umap": "umap-clusters",
    "volcano": "volcano-plot",
    "forest": "forest-plot",
    "sankey": "sankey-flow",
    "alluvial": "sankey-flow",
    "network": "network-graph",
    "spatial": "spatial-map",
    "map": "spatial-map",
    "upset": "upset-plot",
    "ternary": "ternary-composition",
    "parallel": "parallel-coordinates",
    "radar": "radar-profile",
    "3d-bar": "3d-bar-heatmap",
    "bar3d": "3d-bar-heatmap",
    "3d-bars": "3d-bar-heatmap",
    "3d-heatmap": "3d-bar-heatmap",
    "3d-bar-projection": "3d-bar-heat-projection",
    "bar3d-projection": "3d-bar-heat-projection",
    "heat-projection": "3d-bar-heat-projection",
    "3d-surface": "3d-response-surface",
    "surface3d": "3d-response-surface",
    "response-surface": "3d-response-surface",
    "response3d": "3d-response-surface",
    "precision-recall": "precision-recall-curve",
    "pr-curve": "precision-recall-curve",
    "pr": "precision-recall-curve",
    "calibration": "calibration-reliability",
    "reliability": "calibration-reliability",
    "reliability-diagram": "calibration-reliability",
    "survival": "survival-km",
    "kaplan-meier": "survival-km",
    "km": "survival-km",
    "residual": "residual-diagnostics",
    "diagnostics": "residual-diagnostics",
    "residual-plot": "residual-diagnostics",
    "manhattan": "manhattan-plot",
    "genome-wide": "manhattan-plot",
    "confusion": "confusion-matrix",
    "confusion-matrix": "confusion-matrix",
    "cm": "confusion-matrix",
    "bland-altman": "bland-altman",
    "agreement": "bland-altman",
    "ma": "ma-plot",
    "ma-plot": "ma-plot",
    "enrichment": "enrichment-dotplot",
    "dotplot": "enrichment-dotplot",
    "enrichment-dot": "enrichment-dotplot",
    "treemap": "treemap-hierarchy",
    "hierarchy": "treemap-hierarchy",
    "waterfall": "waterfall-contribution",
    "contribution": "waterfall-contribution",
    "time-series": "time-series-ribbon",
    "timeseries": "time-series-ribbon",
    "ribbon": "time-series-ribbon",
    "3d-scatter": "3d-scatter",
    "scatter3d": "3d-scatter",
    "3d-volume": "3d-volume",
    "volume3d": "3d-volume",
    "voxel": "3d-volume",
    "3d-vector": "3d-vector-field",
    "vector-field": "3d-vector-field",
    "quiver3d": "3d-vector-field",
    "det": "det-curve",
    "det-curve": "det-curve",
    "learning": "learning-curve",
    "learning-curve": "learning-curve",
    "gsea": "gsea-curve",
    "enrichment-curve": "gsea-curve",
    "sunburst": "sunburst-hierarchy",
    "sunburst-hierarchy": "sunburst-hierarchy",
    "event": "event-timeline",
    "timeline": "event-timeline",
    "event-timeline": "event-timeline",
    "ohlc": "ohlc-candlestick",
    "candlestick": "ohlc-candlestick",
    "k-line": "ohlc-candlestick",
}

CJK_HINTS = {
    "多分类": "multiclass-shap-combo",
    "shap": "multiclass-shap-combo",
    "云雨": "paired-raincloud",
    "roc": "cv-roc-ci",
    "泰勒": "taylor-diagram",
    "相关矩阵组合": "correlation-pairgrid",
    "拟合线": "correlation-pairgrid",
    "预测": "prediction-marginal-grid",
    "真实": "prediction-marginal-grid",
    "tpe": "rf-tpe-surface",
    "曲面": "rf-tpe-surface",
    "半边小提琴": "grouped-corr-split-violin",
    "环形热图": "grouped-circular-heatmap",
    "城市公园": "urban-park-cooling-combo",
    "堆叠": "urban-park-cooling-combo",
    "和弦": "nature-chord-diagram",
    "circos": "nature-chord-diagram",
    "比较": "grouped-comparison",
    "山脊": "ridge-plot",
    "hexbin": "hexbin-fit",
    "密度": "hexbin-fit",
    "热图": "expression-heatmap",
    "pcoa": "ordination-pcoa",
    "降维": "ordination-pcoa",
    "umap": "umap-clusters",
    "火山": "volcano-plot",
    "森林图": "forest-plot",
    "sankey": "sankey-flow",
    "桑基": "sankey-flow",
    "网络": "network-graph",
    "地图": "spatial-map",
    "upset": "upset-plot",
    "三元": "ternary-composition",
    "平行坐标": "parallel-coordinates",
    "雷达": "radar-profile",
    "三维响应面": "3d-response-surface",
    "响应曲面": "3d-response-surface",
    "三维曲面": "3d-response-surface",
    "三维柱阵热力投影": "3d-bar-heat-projection",
    "三维柱状热力投影": "3d-bar-heat-projection",
    "柱阵热力投影": "3d-bar-heat-projection",
    "热力投影": "3d-bar-heat-projection",
    "三维柱阵": "3d-bar-heatmap",
    "三维柱": "3d-bar-heatmap",
    "3d柱": "3d-bar-heatmap",
    "三维": "3d-bar-heatmap",
    "precision-recall": "precision-recall-curve",
    "pr曲线": "precision-recall-curve",
    "精确率召回率": "precision-recall-curve",
    "校准": "calibration-reliability",
    "可靠性图": "calibration-reliability",
    "校准曲线": "calibration-reliability",
    "生存": "survival-km",
    "kaplan": "survival-km",
    "残差": "residual-diagnostics",
    "诊断图": "residual-diagnostics",
    "曼哈顿": "manhattan-plot",
    "全基因组": "manhattan-plot",
    "混淆矩阵": "confusion-matrix",
    "confusion": "confusion-matrix",
    "一致性": "bland-altman",
    "bland-altman": "bland-altman",
    "方法学一致性": "bland-altman",
    "ma图": "ma-plot",
    "ma plot": "ma-plot",
    "平均表达": "ma-plot",
    "富集点图": "enrichment-dotplot",
    "富集气泡": "enrichment-dotplot",
    "enrichment": "enrichment-dotplot",
    "树图": "treemap-hierarchy",
    "矩形树图": "treemap-hierarchy",
    "旭日图": "sunburst-hierarchy",
    "瀑布图": "waterfall-contribution",
    "贡献分解": "waterfall-contribution",
    "时间序列": "time-series-ribbon",
    "置信带": "time-series-ribbon",
    "三维散点": "3d-scatter",
    "3d散点": "3d-scatter",
    "三维体数据": "3d-volume",
    "体数据": "3d-volume",
    "体素": "3d-volume",
    "三维向量场": "3d-vector-field",
    "向量场": "3d-vector-field",
    "流场": "3d-vector-field",
    "det曲线": "det-curve",
    "检测误差": "det-curve",
    "学习曲线": "learning-curve",
    "泛化曲线": "learning-curve",
    "gsea": "gsea-curve",
    "富集曲线": "gsea-curve",
    "旭日": "sunburst-hierarchy",
    "旭日层级": "sunburst-hierarchy",
    "事件时间线": "event-timeline",
    "时间线": "event-timeline",
    "ohlc": "ohlc-candlestick",
    "k线": "ohlc-candlestick",
    "蜡烛图": "ohlc-candlestick",
}


def normalize(value: str) -> str:
    value = value.strip().lower().replace("_", "-")
    value = re.sub(r"[^a-z0-9\-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def resolve_template(value: str) -> str:
    raw = value.strip()
    key = normalize(raw)
    if key in SCRIPT_MAP:
        return key
    if key in ALIASES:
        return ALIASES[key]
    lowered = raw.lower()
    for hint, template_id in CJK_HINTS.items():
        if hint.lower() in lowered:
            return template_id
    raise SystemExit(
        f"Unknown template: {value}\nAvailable ids: " + ", ".join(sorted(SCRIPT_MAP))
    )


def write_readme(project: Path, template_id: str, script_path: Path) -> None:
    readme = project / "README.md"
    output_stem = project / "outputs" / f"{script_path.stem.removeprefix('make_')}_replica"
    block = f"""
## {template_id}

Generated from the bundled MathModel figure-template skill.

```bash
python3 {script_path.as_posix()}
```

Outputs:

- `{output_stem.with_suffix('.png').as_posix()}`
- `{output_stem.with_suffix('.pdf').as_posix()}`
- `{output_stem.with_suffix('.svg').as_posix()}`
""".strip()
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        marker = f"## {template_id}"
        if marker in text:
            return
        readme.write_text(text.rstrip() + "\n\n" + block + "\n", encoding="utf-8")
    else:
        readme.write_text("# 绘图复刻\n\n" + block + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a bundled MathModel figure template.")
    parser.add_argument("template", nargs="?", help="Template id, alias, or Chinese title fragment")
    parser.add_argument("--project", default="绘图复刻", help="Output project directory, default: 绘图复刻")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite an existing copied workspace script")
    parser.add_argument("--list", action="store_true", help="List supported template ids")
    args = parser.parse_args()

    if args.list:
        for template_id in sorted(SCRIPT_MAP):
            print(template_id)
        return
    if not args.template:
        parser.error("template is required unless --list is used")

    template_id = resolve_template(args.template)
    skill_root = Path(__file__).resolve().parents[1]
    src = skill_root / "scripts" / "templates" / SCRIPT_MAP[template_id]
    if not src.exists():
        raise SystemExit(f"Bundled script missing: {src}")

    project = Path(args.project).expanduser().resolve()
    scripts_dir = project / "scripts"
    outputs_dir = project / "outputs"
    mpl_dir = project / ".mplconfig"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    outputs_dir.mkdir(parents=True, exist_ok=True)
    mpl_dir.mkdir(parents=True, exist_ok=True)

    dst = scripts_dir / src.name
    if dst.exists() and not args.overwrite:
        print(f"Using existing workspace script: {dst}")
    else:
        shutil.copy2(src, dst)
        print(f"Copied template script: {dst}")

    palette_src = skill_root / "scripts" / "palette.py"
    if palette_src.exists():
        shutil.copy2(palette_src, scripts_dir / palette_src.name)

    # 子进程同样要 UTF-8：模板脚本会打印 ✓/→ 等符号，在 Windows 的 GBK 控制台下
    # 会 UnicodeEncodeError 并中断，表现为「脚本复制了但产物缺失」。
    child_env = dict(os.environ, PYTHONIOENCODING="utf-8")
    result = subprocess.run([sys.executable, str(dst)], cwd=str(project),
                            check=False, env=child_env)
    if result.returncode != 0:
        raise SystemExit(result.returncode)

    write_readme(project, template_id, dst)

    stem = dst.stem.removeprefix("make_")
    for suffix in (".png", ".pdf", ".svg"):
        path = outputs_dir / f"{stem}_replica{suffix}"
        print(path)


if __name__ == "__main__":
    main()
