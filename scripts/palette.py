"""Shared Nature Communications-inspired style tokens for scibox templates.

The categorical cycle follows the recurring model colors in the supplied paper:
red, blue, green, orange, and purple. Plot-specific continuous maps remain
semantic: sequential for ordered values and diverging around a meaningful center.
"""

import matplotlib as mpl
from cycler import cycler
from matplotlib.colors import LinearSegmentedColormap

INK = "#222222"
MUTED = "#555555"
GRID = "#D9D9D9"
PANEL = "#F3F3F3"
WHITE = "#FFFFFF"
PRIMARY = "#1F77B4"      # blue
SECONDARY = "#2CA02C"    # green
HIGHLIGHT = "#D62728"    # red
GOLD = "#FF7F0E"         # orange
SKY = "#17BECF"          # cyan
PURPLE = "#9467BD"
YELLOW = "#BCBD22"
BLACK = "#111111"
NEUTRAL = "#7F7F7F"

# Ordered to match the reference paper's recurring forecast-model encoding.
QUALITATIVE = [HIGHLIGHT, PRIMARY, SECONDARY, GOLD, PURPLE, "#8C564B", "#E377C2", NEUTRAL, YELLOW, SKY]
QUALITATIVE_MARKERS = ["o", "s", "^", "D", "v", "P", "X", "<", ">", "h"]
SEQUENTIAL = "viridis"
SEQUENTIAL_SAFE = "magma"
DIVERGING = "RdBu_r"

MODEL_COLORS = {
    "Cross-Unet": HIGHLIGHT,
    "Cross-Former": PRIMARY,
    "Transformer": SECONDARY,
    "TimeFilter": GOLD,
    "TimeMixer": PURPLE,
    "Ground truth": BLACK,
}
MODEL_MARKERS = {
    "Cross-Unet": "o",
    "Cross-Former": "s",
    "Transformer": "^",
    "TimeFilter": "D",
    "TimeMixer": "v",
    "Ground truth": "o",
}


def apply_paper_style() -> None:
    """Apply the shared publication style while preserving semantic colormaps."""
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"],
            "font.size": 8.5,
            "axes.labelsize": 9,
            "axes.titlesize": 9.5,
            "axes.titleweight": "bold",
            "axes.labelcolor": INK,
            "axes.edgecolor": INK,
            "axes.linewidth": 0.8,
            "axes.facecolor": WHITE,
            "figure.facecolor": WHITE,
            "savefig.facecolor": WHITE,
            "xtick.color": INK,
            "ytick.color": INK,
            "xtick.labelsize": 7.5,
            "ytick.labelsize": 7.5,
            "xtick.major.size": 3,
            "ytick.major.size": 3,
            "xtick.major.width": 0.75,
            "ytick.major.width": 0.75,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "grid.color": GRID,
            "grid.linestyle": "--",
            "grid.linewidth": 0.65,
            "grid.alpha": 0.8,
            "axes.axisbelow": True,
            "axes.prop_cycle": cycler(color=QUALITATIVE),
            "lines.linewidth": 1.6,
            "lines.markersize": 4,
            "lines.markeredgewidth": 0.65,
            "legend.fontsize": 8,
            "legend.frameon": False,
            "legend.handlelength": 1.7,
            "legend.labelspacing": 0.35,
            "legend.borderaxespad": 0.4,
            "patch.linewidth": 0.65,
            "image.cmap": SEQUENTIAL,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "savefig.dpi": 300,
        }
    )

# Dedicated continuous scale for 3D response surfaces, bar matrices, volumes,
# and vector-field magnitudes. It follows the existing scibox 3D examples and
# stays independent from the paper-inspired categorical cycle.
THREED = LinearSegmentedColormap.from_list(
    "scientific_3d",
    [
        "#DCEFE7",
        "#78C3A5",
        "#15958B",
        "#0D6F7B",
        "#F0D466",
        "#F29A4C",
        "#C95543",
    ],
    N=256,
)


def categorical(n: int) -> list[str]:
    """Return a deterministic categorical cycle, repeating only after ten groups."""
    return [QUALITATIVE[i % len(QUALITATIVE)] for i in range(n)]


def series_style(index: int) -> dict[str, str]:
    """Return a stable paper-inspired color and marker pair for a series."""
    position = index % len(QUALITATIVE)
    return {"color": QUALITATIVE[position], "marker": QUALITATIVE_MARKERS[position]}
