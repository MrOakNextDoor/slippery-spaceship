#   Loading textures and sounds

#   Libraries
from typing import Tuple, Literal

import pygame as pg


#   Code
def load_stack(surf: pg.Surface, start_pos: pg.Vector2, 
               size: pg.Vector2) -> Tuple:
    #   size refers to the size of each layer

    return [surf.subsurface(round(start_pos + pg.Vector2(0, y)), size) 
            for y in range(round(start_pos.y), surf.get_height(), 
                            round(size.y))]