from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

from palette import GRID, HIGHLIGHT, PRIMARY, SECONDARY


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "ohlc_candlestick_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    n = 34
    open_price = 100 + np.cumsum(rng.normal(0.15, 1.15, n))
    close_price = open_price + rng.normal(0.08, 1.10, n)
    high = np.maximum(open_price, close_price) + rng.uniform(0.25, 1.15, n)
    low = np.minimum(open_price, close_price) - rng.uniform(0.25, 1.00, n)
    fig, ax = plt.subplots(figsize=(8.7, 5.5))
    for i, (op, cp, hi, lo) in enumerate(zip(open_price, close_price, high, low)):
        rising = cp >= op
        color = SECONDARY if rising else HIGHLIGHT
        ax.vlines(i, lo, hi, color=color, lw=1.0, zorder=2)
        bottom, height = min(op, cp), max(abs(cp - op), 0.06)
        ax.add_patch(Rectangle((i - 0.32, bottom), 0.64, height, facecolor=color, edgecolor=color, alpha=0.88, zorder=3))
    ax.plot(np.arange(n), close_price, color=PRIMARY, lw=0.8, alpha=0.45, label="Close trend")
    ax.set_xlabel("Trading day")
    ax.set_ylabel("Price (unit)")
    ax.set_title("OHLC / candlestick price chart", pad=13, weight="bold")
    ax.set_xticks(np.arange(0, n, 5))
    ax.grid(True, axis="y", color=GRID, alpha=0.55, linewidth=0.6)
    ax.legend(loc="upper left", frameon=True, framealpha=0.9, fontsize=8.7)
    ax.text(0.98, 0.04, "Green = close ≥ open · orange = close < open", transform=ax.transAxes, ha="right", va="bottom", fontsize=8.5, color="#1F2933")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
