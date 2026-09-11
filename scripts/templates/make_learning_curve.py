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
    out = ROOT / "outputs" / "learning_curve_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    sizes = np.array([80, 140, 220, 320, 450, 600, 800, 1000])
    train = 0.985 - 0.035 * np.log1p(sizes / 90) / np.log(12)
    test = 0.63 + 0.30 * (1 - np.exp(-sizes / 340))
    train_sd = 0.010 + 0.014 * (sizes.max() - sizes) / sizes.max()
    test_sd = 0.040 - 0.018 * (sizes - sizes.min()) / (sizes.max() - sizes.min())
    fig, ax = plt.subplots(figsize=(7.8, 5.8))
    ax.plot(sizes, train, color=HIGHLIGHT, marker="o", ms=4.5, lw=1.9, label="Training score")
    ax.fill_between(sizes, train - train_sd, train + train_sd, color=HIGHLIGHT, alpha=0.13, lw=0)
    ax.plot(sizes, test, color=PRIMARY, marker="o", ms=4.5, lw=1.9, label="Validation score")
    ax.fill_between(sizes, test - test_sd, test + test_sd, color=PRIMARY, alpha=0.15, lw=0)
    ax.set(xlabel="Number of training samples", ylabel="Balanced accuracy")
    ax.set_title("Learning curve with uncertainty bands", pad=13, weight="bold")
    ax.set_ylim(0.55, 1.02)
    ax.grid(True, color=GRID, alpha=0.50, linewidth=0.6)
    ax.legend(loc="lower right", frameon=True, framealpha=0.9, fontsize=9)
    ax.text(0.03, 0.96, "The widening gap suggests variance; the plateau suggests limited benefit from more samples.", transform=ax.transAxes, va="top", fontsize=8.4, color="#667784")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
