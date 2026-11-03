from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from palette import apply_paper_style
from palette import GOLD, GRID, PRIMARY
import numpy as np
from matplotlib.gridspec import GridSpecFromSubplotSpec
from matplotlib.lines import Line2D


@dataclass(frozen=True)
class ModelPanel:
    name: str
    train_noise: float
    test_noise: float
    train_bias: float
    test_bias: float


PANELS = [
    ModelPanel(
        "RF",
        train_noise=3.8,
        test_noise=9.4,
        train_bias=0.3,
        test_bias=1.8,
    ),
    ModelPanel(
        "XGBoost",
        train_noise=3.4,
        test_noise=7.0,
        train_bias=0.1,
        test_bias=1.4,
    ),
    ModelPanel(
        "LightGBM",
        train_noise=4.4,
        test_noise=9.8,
        train_bias=0.4,
        test_bias=1.6,
    ),
    ModelPanel(
        "CatBoost",
        train_noise=7.1,
        test_noise=9.5,
        train_bias=0.2,
        test_bias=1.2,
    ),
]

TRAIN_COLOR = PRIMARY
TEST_COLOR = GOLD


def configure_matplotlib() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "font.size": 9,
            "axes.linewidth": 1.2,
            "xtick.major.width": 0.9,
            "ytick.major.width": 0.9,
            "xtick.major.size": 3.0,
            "ytick.major.size": 3.0,
            "legend.frameon": False,
        }
    )
    apply_paper_style()


def make_actual_values(rng: np.random.Generator, n: int) -> np.ndarray:
    low = rng.gamma(shape=2.1, scale=13.0, size=n)
    mid = rng.normal(loc=52.0, scale=14.0, size=n)
    high = rng.normal(loc=82.0, scale=11.0, size=n)
    selector = rng.choice([0, 1, 2], size=n, p=[0.46, 0.34, 0.20])
    values = np.where(selector == 0, low, np.where(selector == 1, mid, high))
    return np.clip(values, 0.0, 108.0)


def simulate_predictions(
    rng: np.random.Generator,
    actual: np.ndarray,
    noise: float,
    bias: float,
    shrink: float,
) -> np.ndarray:
    hetero = rng.normal(0.0, noise * (0.72 + 0.008 * actual), size=actual.size)
    systematic = bias + shrink * (actual - 55.0)
    pred = actual + systematic + hetero
    return np.clip(pred, -6.0, 112.0)


def regression_metrics(observed: np.ndarray, predicted: np.ndarray) -> tuple[float, float]:
    ss_total = float(np.sum((observed - observed.mean()) ** 2))
    r_squared = 1.0 - float(np.sum((observed - predicted) ** 2)) / ss_total
    rmse = float(np.sqrt(np.mean((observed - predicted) ** 2)))
    return r_squared, rmse


def kde_1d(values: np.ndarray, grid: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    std = max(np.std(values, ddof=1), 1e-3)
    bandwidth = max(1.06 * std * values.size ** (-1 / 5), 3.2)
    z = (grid[:, None] - values[None, :]) / bandwidth
    density = np.exp(-0.5 * z**2).mean(axis=1) / (bandwidth * np.sqrt(2 * np.pi))
    return density


def draw_top_distribution(ax: plt.Axes, train: np.ndarray, test: np.ndarray, train_color: str, test_color: str) -> None:
    bins = np.linspace(0, 110, 20)
    for values, color in [(test, test_color), (train, train_color)]:
        ax.hist(
            values,
            bins=bins,
            density=True,
            facecolor=mpl.colors.to_rgba(color, 0.12),
            edgecolor=mpl.colors.to_rgba(color, 0.58),
            linewidth=1.05,
        )
        grid = np.linspace(0, 110, 240)
        density = kde_1d(values, grid)
        ax.plot(grid, density, color=color, lw=1.45, alpha=0.88)
    ax.set_xlim(-5, 110)
    ax.set_ylim(bottom=0)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=0)


def draw_right_distribution(ax: plt.Axes, train: np.ndarray, test: np.ndarray, train_color: str, test_color: str) -> None:
    bins = np.linspace(-5, 112, 20)
    max_density = 0.0
    for values, color in [(test, test_color), (train, train_color)]:
        counts, edges = np.histogram(values, bins=bins, density=True)
        max_density = max(max_density, float(counts.max()))
        centers = (edges[:-1] + edges[1:]) / 2
        heights = np.diff(edges)
        ax.barh(
            centers,
            counts,
            height=heights,
            facecolor=mpl.colors.to_rgba(color, 0.12),
            edgecolor=mpl.colors.to_rgba(color, 0.58),
            linewidth=1.05,
        )
        grid = np.linspace(-5, 112, 240)
        density = kde_1d(values, grid)
        max_density = max(max_density, float(density.max()))
        ax.plot(density, grid, color=color, lw=1.45, alpha=0.88)
    ax.set_ylim(-5, 112)
    ax.set_xlim(0, max_density * 1.15)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=0)


def draw_scatter_panel(
    ax: plt.Axes,
    actual_train: np.ndarray,
    pred_train: np.ndarray,
    actual_test: np.ndarray,
    pred_test: np.ndarray,
) -> None:
    ax.plot([-5, 110], [-5, 110], color="#777777", lw=0.9, linestyle="--", zorder=0)
    ax.scatter(
        actual_test,
        pred_test,
        s=23,
        facecolors="none",
        edgecolors=mpl.colors.to_rgba(TEST_COLOR, 0.76),
        marker="s",
        linewidths=0.85,
        label="Test",
        zorder=2,
    )
    ax.scatter(
        actual_train,
        pred_train,
        s=23,
        facecolors="none",
        edgecolors=mpl.colors.to_rgba(TRAIN_COLOR, 0.78),
        marker="o",
        linewidths=0.85,
        label="Train",
        zorder=3,
    )
    ax.set_xlim(-5, 110)
    ax.set_ylim(-5, 112)
    ax.set_xlabel("Actual", fontsize=9, labelpad=3)
    ax.set_ylabel("Predicted", fontsize=9, labelpad=3)
    ax.tick_params(labelsize=8)
    ax.grid(True, color=GRID, linestyle="--", linewidth=0.5, alpha=0.55)
    train_r2, train_rmse = regression_metrics(actual_train, pred_train)
    test_r2, test_rmse = regression_metrics(actual_test, pred_test)
    metric_text = (
        f"Train  R$^2$ = {train_r2:.2f}  RMSE = {train_rmse:.1f}\n"
        f"Test    R$^2$ = {test_r2:.2f}  RMSE = {test_rmse:.1f}"
    )
    ax.text(
        0.97,
        0.035,
        metric_text,
        transform=ax.transAxes,
        fontsize=7.0,
        ha="right",
        va="bottom",
        bbox=dict(boxstyle="square,pad=0.18", facecolor="white", edgecolor="none", alpha=0.88),
    )


def draw_model_panel(fig: plt.Figure, slot, panel: ModelPanel, seed: int, panel_label: str) -> None:
    rng = np.random.default_rng(seed)
    actual_train = make_actual_values(rng, 230)
    actual_test = make_actual_values(rng, 92)
    pred_train = simulate_predictions(rng, actual_train, panel.train_noise, panel.train_bias, shrink=-0.018)
    pred_test = simulate_predictions(rng, actual_test, panel.test_noise, panel.test_bias, shrink=-0.055)

    sub = GridSpecFromSubplotSpec(
        2,
        2,
        subplot_spec=slot,
        height_ratios=[0.30, 1.0],
        width_ratios=[1.0, 0.34],
        hspace=0.06,
        wspace=0.06,
    )
    ax_top = fig.add_subplot(sub[0, 0])
    ax_main = fig.add_subplot(sub[1, 0])
    ax_right = fig.add_subplot(sub[1, 1], sharey=ax_main)
    ax_blank = fig.add_subplot(sub[0, 1])
    ax_blank.axis("off")

    draw_top_distribution(ax_top, actual_train, actual_test, TRAIN_COLOR, TEST_COLOR)
    draw_scatter_panel(ax_main, actual_train, pred_train, actual_test, pred_test)
    draw_right_distribution(ax_right, pred_train, pred_test, TRAIN_COLOR, TEST_COLOR)
    ax_top.set_title(panel.name, fontsize=9.5, fontweight="bold", pad=4)
    ax_main.text(0.025, 0.97, panel_label, transform=ax_main.transAxes,
                 ha="left", va="top", fontsize=10, fontweight="bold")


def make_figure(output_stem: Path) -> None:
    configure_matplotlib()
    fig = plt.figure(figsize=(10.4, 8.2))
    outer = fig.add_gridspec(
        2,
        2,
        left=0.055,
        right=0.982,
        bottom=0.055,
        top=0.925,
        wspace=0.22,
        hspace=0.28,
    )

    for idx, panel in enumerate(PANELS):
        draw_model_panel(fig, outer[idx // 2, idx % 2], panel,
                         seed=20260505 + idx * 103, panel_label=chr(ord("a") + idx))

    fig.legend(
        handles=[
            Line2D([], [], color=TRAIN_COLOR, marker="o", markerfacecolor="none", lw=1.2, label="Train"),
            Line2D([], [], color=TEST_COLOR, marker="s", markerfacecolor="none", lw=1.2, label="Test"),
        ],
        loc="upper center",
        bbox_to_anchor=(0.5, 0.985),
        ncol=2,
        frameon=False,
        fontsize=8,
        handlelength=1.6,
        columnspacing=1.1,
    )

    output_stem.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_stem.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(output_stem.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(output_stem.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    make_figure(ROOT / "outputs" / "prediction_marginal_grid_replica")


if __name__ == "__main__":
    main()
