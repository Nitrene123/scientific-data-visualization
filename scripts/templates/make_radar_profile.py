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
    out = ROOT / "outputs" / "radar_profile_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    mpl.rcParams.update({"font.family": "DejaVu Sans"})
    labels = ["Accuracy", "Speed", "Robustness", "Interpretability", "Scalability", "Fairness"]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    angles = np.concatenate([angles, angles[:1]])
    profiles = [("Method A", [0.82, 0.62, 0.78, 0.72, 0.65, 0.76], "#4e79a7"), ("Method B", [0.68, 0.90, 0.66, 0.58, 0.86, 0.63], "#e15759"), ("Method C", [0.74, 0.76, 0.86, 0.84, 0.72, 0.80], "#59a14f")]
    fig, ax = plt.subplots(figsize=(7.1, 7.1), subplot_kw={"projection": "polar"})
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    for name, values, color in profiles:
        closed = np.array(values + values[:1])
        ax.plot(angles, closed, color=color, lw=2.2, label=name)
        ax.fill(angles, closed, color=color, alpha=0.11)
    ax.set_xticks(angles[:-1], labels)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2", "0.4", "0.6", "0.8", "1.0"])
    ax.set_ylim(0, 1)
    ax.set_title("Radar profile across evaluation criteria", pad=26, weight="bold")
    ax.legend(frameon=False, loc="upper right", bbox_to_anchor=(1.25, 1.12))
    fig.tight_layout()
    save(fig)


if __name__ == "__main__":
    main()
