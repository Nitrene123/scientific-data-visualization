from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def project(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    return b + 0.5 * c, (np.sqrt(3) / 2) * c


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "ternary_composition_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans"})
    rng = np.random.default_rng(20260911)
    raw = rng.dirichlet([3.5, 2.5, 4.0], 150)
    x, y = project(raw[:, 0], raw[:, 1], raw[:, 2])
    fig, ax = plt.subplots(figsize=(7.4, 6.6))
    triangle = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2], [0, 0]])
    ax.plot(triangle[:, 0], triangle[:, 1], color="#333333", lw=1.6)
    ax.scatter(x, y, c=raw[:, 0], cmap="viridis", s=42, alpha=0.78, edgecolor="white", linewidth=0.45)
    for frac in [0.2, 0.4, 0.6, 0.8]:
        ax.plot([frac, frac + (1 - frac) / 2], [0, (1 - frac) * np.sqrt(3) / 2], color="#dddddd", lw=0.7)
        ax.plot([frac / 2, 1 - frac / 2], [frac * np.sqrt(3) / 2, frac * np.sqrt(3) / 2], color="#dddddd", lw=0.7)
    ax.text(-0.04, -0.055, "Component A", ha="left", va="top", fontsize=11)
    ax.text(1.04, -0.055, "Component B", ha="right", va="top", fontsize=11)
    ax.text(0.5, np.sqrt(3) / 2 + 0.07, "Component C", ha="center", fontsize=11)
    ax.set_xlim(-0.12, 1.12)
    ax.set_ylim(-0.12, 0.99)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Ternary composition plot", pad=20, weight="bold")
    cb = fig.colorbar(ax.collections[0], ax=ax, fraction=0.046, pad=0.03)
    cb.set_label("Fraction of component A")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
