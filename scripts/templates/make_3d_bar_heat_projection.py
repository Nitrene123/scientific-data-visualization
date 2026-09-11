from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.lines import Line2D
import numpy as np

from palette import GRID, HIGHLIGHT, INK, THREED


def response_matrix(hours: np.ndarray, days: np.ndarray) -> np.ndarray:
    """Deterministic discrete response surface for a bar matrix example."""
    xx, yy = np.meshgrid(hours, days)
    rng = np.random.default_rng(20260911)
    baseline = 95 + 38 * np.exp(-((xx - 8.0) / 5.4) ** 2) + 25 * np.exp(-((xx - 17.0) / 3.0) ** 2)
    day_pattern = 18 * np.sin((yy + 1.2) / 1.6) + 12 * np.cos(xx / 2.4 + yy / 2.1)
    noise = rng.normal(0, 18, size=xx.shape)
    spikes = 265 * np.exp(-((xx - 11.0) / 0.7) ** 2 - ((yy - 3.0) / 0.75) ** 2)
    return np.clip(baseline + day_pattern + noise + spikes, 0, None)


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "3d_bar_heat_projection_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "font.size": 9.5,
            "axes.linewidth": 0.75,
        }
    )
    hours = np.arange(0, 24, 1.0)
    days = np.arange(0, 7, 1.0)
    xx, yy = np.meshgrid(hours, days)
    values = response_matrix(hours, days)
    norm = Normalize(vmin=float(values.min()), vmax=float(values.max()))
    cmap = THREED
    colors = cmap(norm(values.ravel()))
    peak_mask = values.ravel() >= np.quantile(values, 0.985)
    colors[peak_mask] = mpl.colors.to_rgba(HIGHLIGHT)

    fig = plt.figure(figsize=(10.5, 7.2))
    ax = fig.add_subplot(111, projection="3d")
    dx, dy = 0.78, 0.74
    floor_z = -12.0
    ax.contourf(xx, yy, values, zdir="z", offset=floor_z, levels=14, cmap=cmap, alpha=0.72)
    ax.bar3d(
        xx.ravel() - dx / 2,
        yy.ravel() - dy / 2,
        np.zeros(values.size),
        dx,
        dy,
        values.ravel(),
        color=colors,
        shade=True,
        edgecolor=(1, 1, 1, 0.16),
        linewidth=0.14,
    )

    peak_idx = np.flatnonzero(peak_mask)
    ax.scatter(
        xx.ravel()[peak_idx],
        yy.ravel()[peak_idx],
        np.full(peak_idx.size, floor_z + 1.5),
        color=HIGHLIGHT,
        s=18,
        marker="o",
        depthshade=False,
        label="Peak projection",
    )
    ax.set_title("3D bar matrix with heatmap projection", pad=18, weight="bold", fontsize=13)
    ax.set_xlabel("Hour of day (h)", labelpad=8)
    ax.set_ylabel("Day index", labelpad=8)
    ax.set_zlabel("Response / demand", labelpad=8)
    ax.set_xlim(hours.min() - 0.6, hours.max() + 0.6)
    ax.set_ylim(days.min() - 0.6, days.max() + 0.6)
    ax.set_zlim(floor_z, float(values.max()) * 1.12)
    ax.set_xticks(np.arange(0, 25, 4))
    ax.set_yticks(days)
    ax.view_init(elev=28, azim=-58)
    ax.set_box_aspect((1.75, 0.78, 1.12))
    ax.xaxis.pane.set_facecolor((0.94, 0.96, 0.96, 0.38))
    ax.yaxis.pane.set_facecolor((0.94, 0.96, 0.96, 0.38))
    ax.zaxis.pane.set_facecolor((0.97, 0.97, 0.97, 0.28))
    ax.grid(True, color=GRID, alpha=0.35, linewidth=0.5)

    sm = ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array(values)
    cbar = fig.colorbar(sm, ax=ax, fraction=0.035, pad=0.09, shrink=0.72)
    cbar.set_label("Response intensity", labelpad=8)
    ax.legend(
        [Line2D([0], [0], color=HIGHLIGHT, marker="o", lw=0, markersize=5)],
        ["Peak position on the floor projection"],
        loc="upper left",
        bbox_to_anchor=(0.01, 0.98),
        frameon=True,
        framealpha=0.9,
        fontsize=8.2,
    )
    fig.text(0.5, 0.018, "Bar height and floor colors encode the same response matrix; the floor projection supports peak localization.", ha="center", color=INK, fontsize=8.7)
    fig.subplots_adjust(left=0.02, right=0.96, top=0.90, bottom=0.08)
    save(fig)


if __name__ == "__main__":
    main()
