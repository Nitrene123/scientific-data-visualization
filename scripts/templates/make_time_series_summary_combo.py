from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from palette import GRID, apply_paper_style, series_style


def save(fig: plt.Figure) -> None:
    out = ROOT / "outputs" / "time_series_summary_combo_replica"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=300, bbox_inches="tight")
    fig.savefig(out.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(out.with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def integrate_rate(rate: np.ndarray, time: np.ndarray) -> float:
    """Integrate a rate over time with the trapezoidal rule."""
    return float(np.sum((rate[:-1] + rate[1:]) * np.diff(time) / 2))


def main() -> None:
    mpl.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    apply_paper_style()

    # Deterministic illustrative rates; each total below is calculated from
    # these same curves, so the panels remain quantitatively linked.
    time = np.linspace(0, 10, 101)
    operating_profile = (
        5.55
        + 0.34 * np.sin(2 * np.pi * time / 4.4)
        + 0.16 * np.sin(2 * np.pi * time / 1.45)
        + 0.24 * (1 + np.tanh((time - 5.7) * 1.5)) / 2
    )
    rates = {
        "Controller A": operating_profile,
        "Controller B": operating_profile
        * (0.91 + 0.018 * np.sin(2 * np.pi * time / 5.0 + 0.4)),
        "Controller C": operating_profile
        * (0.73 + 0.025 * np.cos(2 * np.pi * time / 6.0)),
    }
    totals = {name: integrate_rate(rate, time) for name, rate in rates.items()}
    baseline = totals["Controller A"]

    fig, (ax_rate, ax_total) = plt.subplots(
        2,
        1,
        figsize=(8.0, 6.5),
        gridspec_kw={"height_ratios": [1.65, 1.15]},
    )
    fig.suptitle(
        "Hydrogen consumption rate and integrated total",
        x=0.085,
        y=0.985,
        ha="left",
        fontsize=12,
        fontweight="bold",
    )

    for index, (name, rate) in enumerate(rates.items()):
        style = series_style(index)
        ax_rate.plot(
            time,
            rate,
            color=style["color"],
            marker=style["marker"],
            markevery=12,
            markersize=3.3,
            linewidth=1.9,
            label=name,
        )

    all_rates = np.concatenate(list(rates.values()))
    ax_rate.set_ylim(max(0, all_rates.min() - 0.24), all_rates.max() + 0.48)
    ax_rate.set_xlim(time.min(), time.max())
    ax_rate.set_title("A  Rate over operating time", loc="left", pad=8, fontsize=9.5)
    ax_rate.set_xlabel("Operating time (h)")
    ax_rate.set_ylabel("H$_2$ consumption rate (g h$^{-1}$)")
    ax_rate.grid(axis="y", color=GRID, alpha=0.55, linewidth=0.6)
    ax_rate.grid(axis="x", visible=False)
    ax_rate.legend(loc="upper right", ncol=3, fontsize=7.8, handlelength=1.8)

    names = list(rates)
    colors = [series_style(i)["color"] for i in range(len(names))]
    values = [totals[name] for name in names]
    bars = ax_total.bar(
        names,
        values,
        width=0.58,
        color=colors,
        edgecolor="white",
        linewidth=0.8,
        zorder=3,
    )
    for index, (bar, name, value) in enumerate(zip(bars, names, values)):
        change = (value - baseline) / baseline * 100
        comparison = "reference" if index == 0 else f"{change:+.1f}% vs A"
        ax_total.annotate(
            f"{value:.1f} g\n{comparison}",
            xy=(bar.get_x() + bar.get_width() / 2, value),
            xytext=(0, 6),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=7.7,
            linespacing=1.25,
        )

    ax_total.set_ylim(0, max(values) * 1.28)
    ax_total.set_title("B  Integrated H$_2$ consumption", loc="left", pad=8, fontsize=9.5)
    ax_total.set_xlabel("Controller")
    ax_total.set_ylabel("Total H$_2$ consumption (g)")
    ax_total.grid(axis="y", color=GRID, alpha=0.55, linewidth=0.6, zorder=0)
    ax_total.grid(axis="x", visible=False)
    ax_total.set_axisbelow(True)

    fig.tight_layout(rect=(0.02, 0.015, 0.99, 0.95), h_pad=1.35)
    save(fig)


if __name__ == "__main__":
    main()
