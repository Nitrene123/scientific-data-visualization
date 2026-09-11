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
    out = ROOT / "outputs" / "parallel_coordinates_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    axes = ["Accuracy", "Recall", "Precision", "F1", "AUC"]
    n = 32
    values = np.clip(rng.normal([0.78, 0.72, 0.80, 0.75, 0.84], [0.08, 0.10, 0.07, 0.09, 0.06], (n, len(axes))), 0.35, 0.99)
    groups = np.repeat([0, 1, 2], [11, 11, 10])
    colors = ["#4e79a7", "#f28e2b", "#59a14f"]
    x = np.arange(len(axes))
    fig, ax = plt.subplots(figsize=(8.0, 5.9))
    for row, group in zip(values, groups):
        ax.plot(x, row, color=colors[group], alpha=0.28, lw=1.0)
    for group, color in enumerate(colors):
        mean = values[groups == group].mean(axis=0)
        ax.plot(x, mean, color=color, lw=3.0, marker="o", ms=6, label=f"Model family {group + 1}")
    ax.set_xticks(x, axes)
    ax.set_ylim(0.3, 1.02)
    ax.set_ylabel("Scaled score")
    ax.set_title("Parallel coordinates for multimetric model profiles", pad=14, weight="bold")
    ax.grid(axis="y", color="#dddddd", lw=0.8)
    ax.legend(frameon=False, ncol=3, loc="lower center", bbox_to_anchor=(0.5, -0.24))
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
