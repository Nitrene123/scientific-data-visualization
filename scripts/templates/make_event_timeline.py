from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, HIGHLIGHT, QUALITATIVE


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "event_timeline_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    labels = ["Baseline", "Intervention", "Adaptation", "Follow-up"]
    starts = np.array([0, 5, 12, 21])
    ends = np.array([5, 12, 21, 30])
    milestones = np.array([2, 8, 16, 26])
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    y = np.arange(len(labels))[::-1]
    for idx, (label, start, end, milestone) in enumerate(zip(labels, starts, ends, milestones)):
        ax.barh(y[idx], end - start, left=start, height=0.42, color=QUALITATIVE[idx], alpha=0.83, edgecolor="white", linewidth=0.9)
        ax.scatter(milestone, y[idx], color=HIGHLIGHT, s=48, marker="D", edgecolor="white", linewidth=0.7, zorder=4)
        ax.text(start + 0.25, y[idx], label, ha="left", va="center", fontsize=9, color="#1F2933")
    ax.axvline(13, color=HIGHLIGHT, ls="--", lw=1.1, label="Key decision point")
    ax.set_yticks([])
    ax.set_xlabel("Study day")
    ax.set_title("Event timeline with phases and milestones", pad=13, weight="bold")
    ax.grid(True, axis="x", color=GRID, alpha=0.55, linewidth=0.6)
    ax.legend(loc="lower right", frameon=True, framealpha=0.9, fontsize=8.7)
    ax.set_xlim(-0.5, 31)
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
