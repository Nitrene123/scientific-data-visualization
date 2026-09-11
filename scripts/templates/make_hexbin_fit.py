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
    out = ROOT / "outputs" / "hexbin_fit_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(20260911)
    x = rng.normal(0, 1.0, 4200)
    y = 0.62 * x + 0.22 * x**2 + rng.normal(0, 0.72, x.size)
    coefficients = np.polyfit(x, y, 2)
    grid = np.linspace(x.min(), x.max(), 300)
    fig, ax = plt.subplots(figsize=(7.8, 6.4))
    hb = ax.hexbin(x, y, gridsize=38, mincnt=1, cmap="magma", bins="log", linewidths=0.15)
    ax.plot(grid, np.polyval(coefficients, grid), color="#2b83ba", lw=2.5, label="Quadratic fit")
    ax.axhline(0, color="#555555", lw=0.8, ls="--")
    cb = fig.colorbar(hb, ax=ax, pad=0.02)
    cb.set_label("log10(count)")
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    ax.set_title("Hexbin density with fitted trend", pad=14, weight="bold")
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
