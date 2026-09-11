"""Legacy-compatible color tokens for the scientific visualization templates.

The original templates used a restrained blue/teal, warm red/orange and neutral
gray visual language, with viridis/magma/RdBu_r-style maps for continuous data.
The original 33 templates are restored directly; newly added templates use these
same legacy-compatible tokens.
"""

from matplotlib.colors import LinearSegmentedColormap

INK = "#263238"
MUTED = "#667784"
GRID = "#B8C2C9"
PANEL = "#F4F7F8"
WHITE = "#FFFFFF"
PRIMARY = "#2A7F9E"
SECONDARY = "#3F9D54"
HIGHLIGHT = "#C65D3B"
GOLD = "#C47B4B"
SKY = "#8CB8C6"
PURPLE = "#9A4BB3"
YELLOW = "#FDAE61"
BLACK = "#222222"
NEUTRAL = "#BDBDBD"

QUALITATIVE = ["#2D214C", "#8F3032", "#C47B4B", "#3C8849", "#242585", PRIMARY, SKY, NEUTRAL]
SEQUENTIAL = "viridis"
SEQUENTIAL_SAFE = "magma"
DIVERGING = "RdBu_r"

# Dedicated continuous scale for 3D response surfaces, bar matrices, volumes,
# and vector-field magnitudes. It follows the reference visual language:
# pale mint/teal at low values, yellow at the middle, and warm orange/red at
# high values. Categorical 3D scatter plots should keep using QUALITATIVE.
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
    """Return a deterministic categorical cycle, repeating only after eight groups."""
    return [QUALITATIVE[i % len(QUALITATIVE)] for i in range(n)]
