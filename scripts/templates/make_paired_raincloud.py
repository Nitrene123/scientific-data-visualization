from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from palette import HIGHLIGHT, PRIMARY, apply_paper_style
import numpy as np
from matplotlib.patches import Patch


PALETTE = {
    "Versicolor": {"edge": HIGHLIGHT, "fill": "#F3B7B5"},
    "Virginica": {"edge": PRIMARY, "fill": "#B7D1E5"},
}


def configure_matplotlib() -> None:
    mpl.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "DejaVu Serif", "serif"],
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "axes.spines.right": False,
            "axes.spines.top": False,
            "axes.linewidth": 2.3,
            "xtick.major.width": 2.3,
            "ytick.major.width": 2.3,
            "legend.frameon": False,
        }
    )
    apply_paper_style()


def synthetic_sepal_width_data(seed: int = 20260624) -> dict[tuple[str, str], np.ndarray]:
    """Create deterministic repeated-measures data for the paired raincloud."""
    rng = np.random.default_rng(seed)
    n = 50
    pre_versicolor = rng.normal(2.74, 0.31, n)
    pre_virginica = rng.normal(3.00, 0.36, n)
    data = {
        ("Pre", "Versicolor"): pre_versicolor,
        ("Pre", "Virginica"): pre_virginica,
        ("Post", "Versicolor"): pre_versicolor + rng.normal(0.86, 0.24, n),
        ("Post", "Virginica"): pre_virginica + rng.normal(-0.35, 0.24, n),
    }
    return {key: np.clip(values, 2.05, 4.35) for key, values in data.items()}


def kde_1d(values: np.ndarray, grid: np.ndarray, bw_adjust: float = 1.0) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    std = max(np.std(values, ddof=1), 1e-3)
    bandwidth = max(1.06 * std * values.size ** (-1 / 5) * bw_adjust, 0.055)
    z = (grid[:, None] - values[None, :]) / bandwidth
    density = np.exp(-0.5 * z**2).mean(axis=1) / (bandwidth * np.sqrt(2 * np.pi))
    return density / density.max()


def draw_half_violin(
    ax: plt.Axes,
    values: np.ndarray,
    anchor_x: float,
    side: str,
    fill_color: str,
    edge_color: str,
    width: float = 0.28,
    alpha: float = 0.74,
    zorder: int = 1,
) -> None:
    grid = np.linspace(max(2.05, values.min() - 0.16), min(4.35, values.max() + 0.16), 240)
    density = kde_1d(values, grid, bw_adjust=0.92) * width
    if side == "left":
        ax.fill_betweenx(
            grid,
            anchor_x - density,
            anchor_x,
            facecolor=fill_color,
            edgecolor=edge_color,
            linewidth=1.0,
            alpha=alpha,
            zorder=zorder,
        )
    else:
        ax.fill_betweenx(
            grid,
            anchor_x,
            anchor_x + density,
            facecolor=fill_color,
            edgecolor=edge_color,
            linewidth=1.0,
            alpha=alpha,
            zorder=zorder,
        )


def draw_points(
    ax: plt.Axes,
    values: np.ndarray,
    x: float,
    fill_color: str,
    edge_color: str,
    seed: int,
) -> None:
    rng = np.random.default_rng(seed)
    jitter = rng.normal(0.0, 0.022, values.size)
    ax.scatter(
        x + jitter,
        values,
        s=23,
        facecolors=mpl.colors.to_rgba(fill_color, 0.56),
        edgecolors=edge_color,
        linewidths=0.55,
        alpha=0.78,
        zorder=4,
    )


def draw_box(
    ax: plt.Axes,
    values: np.ndarray,
    x: float,
    fill_color: str,
    edge_color: str,
) -> None:
    bp = ax.boxplot(
        values,
        positions=[x],
        widths=0.095,
        patch_artist=True,
        showfliers=False,
        whis=(0, 100),
        zorder=5,
    )
    for box in bp["boxes"]:
        box.set(facecolor=mpl.colors.to_rgba(fill_color, 0.55), edgecolor=edge_color, linewidth=1.0)
    for whisker in bp["whiskers"]:
        whisker.set(color=edge_color, linewidth=1.0)
    for cap in bp["caps"]:
        cap.set(color=edge_color, linewidth=1.0)
    for median in bp["medians"]:
        median.set(color=edge_color, linewidth=1.0)


def draw_mean_trend(
    ax: plt.Axes,
    data: dict[tuple[str, str], np.ndarray],
    mean_positions: dict[tuple[str, str], float],
) -> None:
    for species in ["Versicolor", "Virginica"]:
        edge = PALETTE[species]["edge"]
        xs = [mean_positions[("Pre", species)], mean_positions[("Post", species)]]
        ys = [data[("Pre", species)].mean(), data[("Post", species)].mean()]
        ax.plot(xs, ys, color=edge, linewidth=1.25, alpha=0.9, zorder=6)
        ax.scatter(xs, ys, marker="D", s=34, color=edge, edgecolor="white", linewidth=0.55, zorder=7)


def draw_pair_connectors(ax: plt.Axes, data: dict[tuple[str, str], np.ndarray], positions: dict[tuple[str, str], float]) -> None:
    """Connect each synthetic subject's repeated measurement across conditions."""
    for species, seed in [("Versicolor", 2), ("Virginica", 1)]:
        rng = np.random.default_rng(seed)
        jitter = rng.normal(0.0, 0.022, data[("Pre", species)].size)
        x_pre = positions[("Pre", f"{species}_points")] + jitter
        x_post = positions[("Post", f"{species}_points")] + jitter
        color = PALETTE[species]["edge"]
        for x0, x1, y0, y1 in zip(x_pre, x_post, data[("Pre", species)], data[("Post", species)]):
            ax.plot([x0, x1], [y0, y1], color=color, linewidth=0.28, alpha=0.035, zorder=3)


def draw_bottom_bracket(ax: plt.Axes, pre_x: float, post_x: float) -> None:
    transform = ax.get_xaxis_transform()
    y = -0.105
    tick_y = -0.120
    ax.plot([pre_x, post_x], [y, y], transform=transform, color="black", linewidth=1.0, clip_on=False)
    ax.plot([pre_x, pre_x], [y, tick_y], transform=transform, color="black", linewidth=1.0, clip_on=False)
    ax.plot([post_x, post_x], [y, tick_y], transform=transform, color="black", linewidth=1.0, clip_on=False)


def make_figure(output_stem: Path) -> None:
    configure_matplotlib()
    data = synthetic_sepal_width_data()
    fig, ax = plt.subplots(figsize=(7.4, 5.8))
    fig.subplots_adjust(left=0.12, right=0.98, bottom=0.22, top=0.86)

    positions = {
        ("Pre", "violin"): 0.76,
        ("Pre", "Virginica_points"): 0.94,
        ("Pre", "Versicolor_points"): 1.07,
        ("Pre", "Versicolor_box"): 1.20,
        ("Pre", "Virginica_box"): 1.33,
        ("Post", "Virginica_box"): 2.02,
        ("Post", "Versicolor_box"): 2.15,
        ("Post", "Virginica_points"): 2.28,
        ("Post", "Versicolor_points"): 2.41,
        ("Post", "violin"): 2.55,
    }

    draw_half_violin(
        ax,
        data[("Pre", "Virginica")],
        positions[("Pre", "violin")],
        "left",
        PALETTE["Virginica"]["fill"],
        PALETTE["Virginica"]["edge"],
        width=0.26,
        alpha=0.76,
        zorder=1,
    )
    draw_half_violin(
        ax,
        data[("Pre", "Versicolor")],
        positions[("Pre", "violin")] + 0.02,
        "left",
        PALETTE["Versicolor"]["fill"],
        PALETTE["Versicolor"]["edge"],
        width=0.22,
        alpha=0.70,
        zorder=2,
    )
    draw_half_violin(
        ax,
        data[("Post", "Versicolor")],
        positions[("Post", "violin")],
        "right",
        PALETTE["Versicolor"]["fill"],
        PALETTE["Versicolor"]["edge"],
        width=0.31,
        alpha=0.78,
        zorder=2,
    )
    draw_half_violin(
        ax,
        data[("Post", "Virginica")],
        positions[("Post", "violin")] - 0.02,
        "right",
        PALETTE["Virginica"]["fill"],
        PALETTE["Virginica"]["edge"],
        width=0.27,
        alpha=0.72,
        zorder=1,
    )

    draw_pair_connectors(ax, data, positions)

    draw_points(ax, data[("Pre", "Virginica")], positions[("Pre", "Virginica_points")], PALETTE["Virginica"]["fill"], PALETTE["Virginica"]["edge"], 1)
    draw_points(ax, data[("Pre", "Versicolor")], positions[("Pre", "Versicolor_points")], PALETTE["Versicolor"]["fill"], PALETTE["Versicolor"]["edge"], 2)
    draw_points(ax, data[("Post", "Virginica")], positions[("Post", "Virginica_points")], PALETTE["Virginica"]["fill"], PALETTE["Virginica"]["edge"], 1)
    draw_points(ax, data[("Post", "Versicolor")], positions[("Post", "Versicolor_points")], PALETTE["Versicolor"]["fill"], PALETTE["Versicolor"]["edge"], 2)

    draw_box(ax, data[("Pre", "Versicolor")], positions[("Pre", "Versicolor_box")], PALETTE["Versicolor"]["fill"], PALETTE["Versicolor"]["edge"])
    draw_box(ax, data[("Pre", "Virginica")], positions[("Pre", "Virginica_box")], PALETTE["Virginica"]["fill"], PALETTE["Virginica"]["edge"])
    draw_box(ax, data[("Post", "Versicolor")], positions[("Post", "Versicolor_box")], PALETTE["Versicolor"]["fill"], PALETTE["Versicolor"]["edge"])
    draw_box(ax, data[("Post", "Virginica")], positions[("Post", "Virginica_box")], PALETTE["Virginica"]["fill"], PALETTE["Virginica"]["edge"])

    mean_positions = {
        ("Pre", "Versicolor"): positions[("Pre", "Versicolor_box")],
        ("Post", "Versicolor"): positions[("Post", "Versicolor_box")],
        ("Pre", "Virginica"): positions[("Pre", "Virginica_box")],
        ("Post", "Virginica"): positions[("Post", "Virginica_box")],
    }
    draw_mean_trend(ax, data, mean_positions)

    ax.set_xlim(0.30, 3.12)
    ax.set_ylim(2.0, 4.5)
    ax.set_yticks(np.arange(2.0, 4.51, 0.5))
    ax.set_ylabel("Response (a.u.)", fontsize=9, labelpad=7)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_linewidth(0.9)
    ax.tick_params(axis="y", labelsize=8, width=0.75, length=3, pad=4)

    pre_label_x = 1.15
    post_label_x = 2.17
    draw_bottom_bracket(ax, pre_label_x, post_label_x)
    transform = ax.get_xaxis_transform()
    ax.text(pre_label_x, -0.145, "Pre", transform=transform, ha="center", va="top", fontsize=8.5)
    ax.text(post_label_x, -0.145, "Post", transform=transform, ha="center", va="top", fontsize=8.5)
    ax.text(
        (pre_label_x + post_label_x) / 2,
        -0.225,
        "Condition",
        transform=transform,
        ha="center",
        va="top",
        fontsize=9.5,
        fontweight="bold",
    )

    legend_handles = [
        Patch(facecolor=PALETTE["Versicolor"]["fill"], edgecolor=PALETTE["Versicolor"]["fill"], label="Group A"),
        Patch(facecolor=PALETTE["Virginica"]["fill"], edgecolor=PALETTE["Virginica"]["fill"], label="Group B"),
    ]
    fig.legend(
        handles=legend_handles,
        title="Group",
        loc="upper center",
        bbox_to_anchor=(0.55, 0.99),
        ncol=2,
        fontsize=8,
        title_fontsize=8.5,
        handlelength=1.5,
        columnspacing=1.0,
        borderaxespad=0.2,
    )

    output_stem.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_stem.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(output_stem.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(output_stem.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    make_figure(ROOT / "outputs" / "paired_raincloud_replica")


if __name__ == "__main__":
    main()
