from typing import Tuple

import numpy as np #type: ignore

# Tile graphics structured type compatible w/ Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32), #unicode typepoint
        ("fg", "3B"), # 3 unsigned bytes for the RBG colors
        ("bg", "3B"), 
    ]
)

# Tile structure used for static defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool_), # returns True if this tile can be walked on
        ("transparent", np.bool_), # returns True if this tile doesn't block FOV
        ("dark", graphic_dt), # graphics for when this tile is not in view
        ("light", graphic_dt), #graphics for when the tile is in view
    ]
)

def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)
    
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)


floor = new_tile(
    walkable=True, 
    transparent=True, 
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)),
)
wall = new_tile(
    walkable=False,
    transparent=False, 
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)),
)