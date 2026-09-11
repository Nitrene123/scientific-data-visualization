from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "upset_plot_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    sets = ["RNA-seq", "Proteomics", "Metabolomics", "ATAC-seq", "Screen"]
    membership = np.array([[1, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 1, 1, 0], [1, 1, 0, 0, 1], [0, 1, 1, 0, 1], [1, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 1, 1, 1]])
    counts = np.array([28, 22, 19, 17, 14, 12, 10, 9, 7, 5])
    order = np.argsort(counts)[::-1]
    membership, counts = membership[order], counts[order]
    fig = plt.figure(figsize=(9.0, 6.1))
    gs = fig.add_gridspec(2, 1, height_ratios=[1.25, 2.0], hspace=0.05)
    top = fig.add_subplot(gs[0])
    bottom = fig.add_subplot(gs[1], sharex=top)
    x = np.arange(len(counts))
    top.bar(x, counts, color="#4e79a7", width=0.68)
    top.set_ylabel("Intersection size")
    top.spines["bottom"].set_visible(False)
    top.tick_params(axis="x", bottom=False, labelbottom=False)
    for j in range(len(counts)):
        active = np.flatnonzero(membership[j])
        bottom.plot([j, j], [active.min(), active.max()], color="#4e79a7", lw=2, zorder=1)
        bottom.scatter([j] * len(active), active, s=62, color="#4e79a7", zorder=2)
        inactive = np.flatnonzero(~membership[j].astype(bool))
        bottom.scatter([j] * len(inactive), inactive, s=36, color="#d9d9d9", zorder=2)
    bottom.set_yticks(np.arange(len(sets)), sets)
    bottom.set_xlabel("Set intersection (ordered by size)")
    bottom.set_ylim(-0.5, len(sets) - 0.5)
    bottom.grid(axis="y", color="#eeeeee", lw=0.7)
    top.set_title("UpSet plot of multi-omics set intersections", pad=12, weight="bold")
    fig.subplots_adjust(left=0.20, right=0.97, bottom=0.14, top=0.88, hspace=0.08)
    save(fig)


if __name__ == "__main__":
    main()
