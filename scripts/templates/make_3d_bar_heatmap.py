from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.lines import Line2D
from matplotlib.colors import Normalize
import numpy as np

from palette import THREED


def configure_matplotlib() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "font.size": 10,
            "axes.linewidth": 0.75,
        }
    )


def response_surface(hours: np.ndarray, days: np.ndarray) -> np.ndarray:
    return (
        82
        + 45 * np.exp(-((hours - 7.5) / 3.0) ** 2)
        + 105 * np.exp(-((hours - 17.2) / 2.2) ** 2)
        + 22 * np.sin(days / 1.8)
        + 11 * np.cos(hours / 2.6 + days / 2.0)
    )


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "3d_bar_heatmap_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    configure_matplotlib()
    hours = np.arange(0, 24, 1.5)
    days = np.arange(0, 8, 1.0)
    xx, yy = np.meshgrid(hours, days)
    heights = response_surface(xx, yy)
    norm = Normalize(vmin=float(heights.min()), vmax=float(heights.max()))

    fig = plt.figure(figsize=(9.6, 6.8))
    ax = fig.add_axes([0.07, 0.08, 0.78, 0.82], projection="3d")
    dx = float(hours[1] - hours[0])
    dy = float(days[1] - days[0])
    colors = THREED(norm(heights.ravel()))
    ax.bar3d(
        (xx.ravel() - dx * 0.43),
        (yy.ravel() - dy * 0.40),
        np.zeros(xx.size),
        dx * 0.82,
        dy * 0.78,
        heights.ravel(),
        color=colors,
        shade=True,
        edgecolor=(1, 1, 1, 0.10),
        linewidth=0.18,
    )

    # A meaningful high-response trajectory, shown both on the bars and as a ground projection.
    path_x = np.linspace(1.0, 22.3, 160)
    path_y = 3.5 + 2.05 * np.sin((path_x - 2.0) / 3.8) + 0.20 * np.cos(path_x / 1.4)
    path_y = np.clip(path_y, days.min() + 0.2, days.max() - 0.2)
    path_z = response_surface(path_x, path_y) + 8
    ax.plot(path_x, path_y, np.zeros_like(path_x) + 3, color="#d73027", lw=1.8, ls="--", alpha=0.72)
    ax.plot(path_x, path_y, path_z, color="#d73027", lw=2.7, solid_capstyle="round")
    ax.scatter(path_x[[0, -1]], path_y[[0, -1]], path_z[[0, -1]], color="#d73027", s=22, depthshade=False)

    ax.set_title("3D response matrix with trajectory projection", pad=18, weight="bold", fontsize=12)
    ax.set_xlabel("Time of day (h)", labelpad=8)
    ax.set_ylabel("Day index", labelpad=8)
    ax.set_zlabel("Response (kWh)", labelpad=8)
    ax.set_xlim(hours.min() - 0.8, hours.max() + 0.8)
    ax.set_ylim(days.min() - 0.5, days.max() + 0.5)
    ax.set_zlim(0, float(heights.max()) * 1.16)
    ax.set_xticks(np.arange(0, 25, 4))
    ax.set_yticks(days)
    ax.view_init(elev=28, azim=-58)
    ax.set_box_aspect((1.55, 0.82, 1.02))
    ax.xaxis.pane.set_facecolor((0.94, 0.96, 0.96, 0.42))
    ax.yaxis.pane.set_facecolor((0.94, 0.96, 0.96, 0.42))
    ax.zaxis.pane.set_facecolor((0.97, 0.97, 0.97, 0.30))
    ax.grid(True, color="#b7c2c2", alpha=0.28, linewidth=0.55)

    sm = ScalarMappable(norm=norm, cmap=THREED)
    sm.set_array(heights)
    cbar = fig.colorbar(sm, ax=ax, fraction=0.035, pad=0.10, shrink=0.73)
    cbar.set_label("Bar height / response (kWh)", labelpad=8)
    cbar.ax.tick_params(labelsize=8)
    ax.legend(
        [Line2D([0], [0], color="#d73027", lw=2.7), Line2D([0], [0], color="#d73027", lw=1.8, ls="--")],
        ["Observed trajectory", "Ground projection"],
        loc="upper left",
        bbox_to_anchor=(0.01, 0.99),
        frameon=True,
        framealpha=0.9,
        fontsize=8.5,
    )
    save(fig)


if __name__ == "__main__":
    main()
