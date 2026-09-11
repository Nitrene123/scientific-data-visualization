from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def kde(values: np.ndarray, grid: np.ndarray) -> np.ndarray:
    bandwidth = max(np.std(values) * values.size ** (-0.2) * 0.8, 0.08)
    z = (grid[:, None] - values[None, :]) / bandwidth
    density = np.exp(-0.5 * z * z).mean(axis=1)
    return density / density.max()


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "ridge_plot_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    groups = ["Week 0", "Week 2", "Week 4", "Week 6", "Week 8", "Week 10"]
    colors = plt.cm.viridis(np.linspace(0.08, 0.92, len(groups)))
    grid = np.linspace(-2.7, 3.8, 500)
    fig, ax = plt.subplots(figsize=(8.2, 6.4))
    for i, (label, color) in enumerate(zip(groups, colors)):
        values = rng.normal(-0.25 + i * 0.42, 0.42 + i * 0.025, 130)
        density = kde(values, grid)
        baseline = i * 0.72
        ax.fill_between(grid, baseline, baseline + density * 0.72, color=color, alpha=0.78, lw=0)
        ax.plot(grid, baseline + density * 0.72, color="#263238", lw=1.1)
        ax.axhline(baseline, color="#ffffff", lw=0.8, alpha=0.75)
        ax.text(-2.82, baseline + 0.08, label, ha="right", va="center", fontsize=10)
    ax.set_xlim(-2.85, 3.85)
    ax.set_ylim(-0.05, len(groups) * 0.72 + 0.5)
    ax.set_yticks([])
    ax.set_xlabel("Effect score")
    ax.set_title("Ridge density plot across repeated conditions", pad=14, weight="bold")
    ax.grid(axis="x", color="#dddddd", lw=0.8, alpha=0.65)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
