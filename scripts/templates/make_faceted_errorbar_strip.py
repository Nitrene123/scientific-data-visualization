from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))
sys.path.insert(0, str(ROOT))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GOLD, GRID, HIGHLIGHT, INK, MUTED, PRIMARY, PURPLE, SECONDARY, WHITE


METHODS = [
    ("Method A", PRIMARY, "o"),
    ("Method B", GOLD, "s"),
    ("Method C", SECONDARY, "^"),
    ("Method D", HIGHLIGHT, "D"),
    ("Method E", PURPLE, "v"),
]


def lighten(color: str, amount: float = 0.62) -> tuple[float, float, float]:
    """Blend a series color toward white for low-emphasis replicate points."""
    base = np.asarray(mpl.colors.to_rgb(color), dtype=float)
    return tuple(base + (1.0 - base) * amount)


def configure_matplotlib() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 1.25,
            "xtick.major.width": 1.1,
            "ytick.major.width": 1.1,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "legend.frameon": False,
        }
    )


def synthetic_benchmark_data(seed: int = 20261030) -> list[dict[str, object]]:
    """Create deterministic faceted benchmark data with raw replicates and intervals."""
    rng = np.random.default_rng(seed)
    panels = [
        {
            "title": "Small workload",
            "xscale": "linear",
            "xlim": (0.40, 1.20),
            "centers": np.array([0.58, 0.70, 0.77, 0.80, 0.83]),
            "noise": 0.018,
        },
        {
            "title": "Medium workload",
            "xscale": "linear",
            "xlim": (1.00, 4.00),
            "centers": np.array([1.42, 1.66, 1.86, 1.98, 2.32]),
            "noise": 0.050,
        },
        {
            "title": "Large workload",
            "xscale": "log",
            "xlim": (2.4, 42.0),
            "centers": np.array([3.6, 5.2, 6.8, 8.2, 10.4]),
            "noise": 0.075,
        },
    ]

    for panel_index, panel in enumerate(panels):
        observations: list[dict[str, object]] = []
        for method_index, (name, color, marker) in enumerate(METHODS):
            base = np.array(
                [
                    0.60 + 0.035 * method_index,
                    0.68 + 0.030 * method_index,
                    0.78 - 0.018 * method_index,
                    0.86 - 0.020 * method_index,
                    0.70 + 0.015 * method_index,
                ]
            )
            y = np.clip(base + rng.normal(0, panel["noise"], base.size), 0.04, 0.98)
            x = panel["centers"][method_index] + rng.normal(
                0, panel["noise"] * (0.45 if panel["xscale"] == "linear" else 0.75), base.size
            )
            observations.append(
                {
                    "name": name,
                    "color": color,
                    "marker": marker,
                    "x": x,
                    "y": y,
                }
            )
        panel["observations"] = observations
        panel["reference"] = {
            "x": panel["xlim"][0] * (1.12 if panel["xscale"] == "linear" else 1.10),
            "y": 0.015 + panel_index * 0.004,
        }
    return panels


def draw_method(ax: plt.Axes, observation: dict[str, object], panel_index: int) -> None:
    color = str(observation["color"])
    marker = str(observation["marker"])
    x = np.asarray(observation["x"], dtype=float)
    y = np.asarray(observation["y"], dtype=float)
    order = np.argsort(y)

    ax.scatter(
        x,
        y,
        s=24,
        color=lighten(color),
        alpha=0.78,
        edgecolors="none",
        zorder=2,
    )
    ax.plot(x[order], y[order], color=color, alpha=0.78, linewidth=1.55, zorder=3)
    ax.scatter(
        x[order],
        y[order],
        s=45,
        marker=marker,
        color=color,
        edgecolors=WHITE,
        linewidths=0.55,
        alpha=0.94,
        zorder=4,
    )

    mean_x = float(np.mean(x))
    mean_y = float(np.mean(y))
    sem_y = float(np.std(y, ddof=1) / np.sqrt(y.size))
    ax.errorbar(
        mean_x,
        mean_y,
        yerr=1.96 * sem_y,
        fmt="none",
        ecolor=color,
        elinewidth=1.2,
        capsize=2.8,
        capthick=1.2,
        zorder=5,
    )


def make_figure(output_stem: Path, show_annotation: bool = False) -> None:
    """Render the figure; keep the explanatory note off unless preparing slides."""
    configure_matplotlib()
    panels = synthetic_benchmark_data()
    fig, axes = plt.subplots(
        1,
        len(panels),
        figsize=(12.6, 4.7),
        sharey=True,
        gridspec_kw={"wspace": 0.32},
    )
    fig.subplots_adjust(left=0.085, right=0.985, bottom=0.19, top=0.72)

    for panel_index, (ax, panel) in enumerate(zip(axes, panels)):
        for observation in panel["observations"]:
            draw_method(ax, observation, panel_index)

        reference = panel["reference"]
        ax.scatter(
            [reference["x"]],
            [reference["y"]],
            marker="*",
            s=90,
            color="#B24C88",
            edgecolors=WHITE,
            linewidths=0.7,
            zorder=6,
        )
        ax.set_title(str(panel["title"]), fontsize=11, color=INK, pad=8)
        ax.set_xscale(str(panel["xscale"]))
        ax.set_xlim(*panel["xlim"])
        if panel["xscale"] == "log":
            ax.set_xticks([3, 10, 30])
            ax.set_xticklabels(["3", "10", "30"])
        ax.set_ylim(-0.03, 1.05)
        ax.set_yticks([0.0, 0.5, 1.0])
        ax.grid(axis="y", color=GRID, linewidth=0.75, alpha=0.62)
        ax.tick_params(axis="both", labelsize=9, colors=INK)
        ax.set_xlabel("Proposal time (ms)", fontsize=10, color=INK, labelpad=8)
        ax.spines["left"].set_color(INK)
        ax.spines["bottom"].set_color(INK)

        if panel_index > 0:
            ax.tick_params(axis="y", labelleft=False)

    axes[0].set_ylabel(r"Local regret $\rho$", fontsize=11, color=INK, labelpad=8)
    fig.suptitle(
        "Faceted benchmark: local regret versus proposal time",
        fontsize=13,
        weight="bold",
        color=INK,
        y=0.965,
    )
    if show_annotation:
        fig.text(
            0.5,
            0.035,
            "faint points = replicates · connected markers = ordered observations · bars = 95% CI",
            ha="center",
            fontsize=8.5,
            color=MUTED,
        )

    handles = [
        plt.Line2D(
            [0],
            [0],
            color=color,
            marker=marker,
            markerfacecolor=color,
            markeredgecolor=WHITE,
            markeredgewidth=0.55,
            linewidth=1.5,
            markersize=6,
            label=name,
        )
        for name, color, marker in METHODS
    ]
    handles.append(
        plt.Line2D(
            [0],
            [0],
            color="none",
            marker="*",
            markerfacecolor="#B24C88",
            markeredgecolor=WHITE,
            markersize=8,
            label="Reference",
        )
    )
    fig.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.86),
        ncol=6,
        fontsize=8.4,
        handletextpad=0.35,
        columnspacing=1.0,
    )

    output_stem.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_stem.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(output_stem.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(output_stem.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    make_figure(ROOT / "outputs" / "faceted_errorbar_strip_replica")


if __name__ == "__main__":
    main()
