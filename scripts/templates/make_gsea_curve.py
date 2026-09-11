from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, HIGHLIGHT, PRIMARY


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "gsea_curve_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    n = 420
    hits = np.array([22, 39, 61, 87, 115, 142, 186, 221, 248, 290, 318, 356, 388])
    hit_set = set(hits.tolist())
    running = [0.0]
    nhit = len(hits)
    for rank in range(1, n + 1):
        if rank in hit_set:
            running.append(running[-1] + 1.0 / nhit)
        else:
            running.append(running[-1] - 1.0 / (n - nhit))
    running = np.asarray(running)
    es_idx = int(np.argmax(np.abs(running)))
    es = float(running[es_idx])
    fig = plt.figure(figsize=(8.1, 6.2))
    grid = fig.add_gridspec(2, 1, height_ratios=[4.2, 0.55], hspace=0.10)
    ax = fig.add_subplot(grid[0])
    rug_ax = fig.add_subplot(grid[1], sharex=ax)
    ranks = np.arange(n + 1)
    ax.step(ranks, running, where="post", color=PRIMARY, lw=2.0, label=f"Running enrichment score (ES = {es:.2f})")
    ax.fill_between(ranks, running, 0, where=running >= 0, color=PRIMARY, alpha=0.12, step="post")
    ax.fill_between(ranks, running, 0, where=running < 0, color=HIGHLIGHT, alpha=0.12, step="post")
    ax.axhline(0, color="#7A8790", lw=0.85)
    ax.axvline(es_idx, color=HIGHLIGHT, ls="--", lw=1.0, label="Peak enrichment position")
    ax.set_ylabel("Running enrichment score")
    ax.set_title("Gene set enrichment analysis running-score curve", pad=13, weight="bold")
    ax.grid(True, color=GRID, alpha=0.50, linewidth=0.6)
    ax.legend(loc="lower right", frameon=True, framealpha=0.9, fontsize=8.5)
    rug_ax.vlines(hits, 0, 1, color=HIGHLIGHT, lw=1.4)
    rug_ax.set_ylim(0, 1)
    rug_ax.set_yticks([])
    rug_ax.set_xlabel("Rank in ordered list")
    rug_ax.text(0.01, 0.50, "Gene-set hits", transform=rug_ax.transAxes, va="center", fontsize=8.2, color="#667784")
    plt.setp(ax.get_xticklabels(), visible=False)
    fig.subplots_adjust(left=0.13, right=0.97, top=0.91, bottom=0.11)
    save(fig)


if __name__ == "__main__":
    main()
