"""Legacy-compatible color tokens for the scientific visualization templates.

The original templates used a restrained blue/teal, warm red/orange and neutral
gray visual language, with viridis/magma/RdBu_r-style maps for continuous data.
The original 33 templates are restored directly; newly added templates use these
same legacy-compatible tokens.
"""

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


def categorical(n: int) -> list[str]:
    """Return a deterministic categorical cycle, repeating only after eight groups."""
    return [QUALITATIVE[i % len(QUALITATIVE)] for i in range(n)]
