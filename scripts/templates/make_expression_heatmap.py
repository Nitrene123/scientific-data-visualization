from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "expression_heatmap_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none", "pdf.fonttype": 42})
    rng = np.random.default_rng(20260911)
    n_features, n_samples = 28, 18
    base = rng.normal(0, 0.55, (n_features, n_samples))
    base[:8, 9:] += 1.25
    base[8:16, :9] -= 0.85
    order = np.argsort(base.mean(axis=1))
    matrix = base[order]
    fig, ax = plt.subplots(figsize=(8.2, 7.1))
    image = ax.imshow(matrix, aspect="auto", cmap="RdBu_r", vmin=-2.3, vmax=2.3, interpolation="nearest")
    ax.set_xticks(np.arange(n_samples), [f"S{i+1}" for i in range(n_samples)], rotation=60, ha="right", fontsize=8)
    ax.set_yticks(np.arange(n_features), [f"Gene {i+1}" for i in order], fontsize=8)
    ax.set_xlabel("Samples")
    ax.set_ylabel("Features (ordered by mean signal)")
    ax.set_title("Clustered expression heatmap", pad=14, weight="bold")
    ax.axvline(8.5, color="white", lw=2.2)
    ax.text(4, -1.7, "Control", ha="center", va="bottom", fontsize=9, color="#333333")
    ax.text(13.5, -1.7, "Treatment", ha="center", va="bottom", fontsize=9, color="#333333")
    cb = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    cb.set_label("z-score")
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
