#   All the objects in the game

#   Libraries
from typing import List

import pygame as pg

import assets


#   Code
class SpriteStack(pg.sprite.Sprite):
    def __init__(self, pos: pg.Vector2, size: pg.Vector2, angle: float=0.0, 
                 spread: int=0):
        
        self.image = None
        self.rect = None

        self.pos = pos
        self.size = size
        self.angle = angle
        self.spread = 1

        self.stacks = []
        self.load_stack()

    def load_stack(self, surf: pg.Surface, start_pos: pg.Vector2, 
                   size: pg.Vector2):
        self.stacks = assets.load_stack(surf, start_pos, size)

    def update(self):
        self.image = self.draw_stack()
        self.rect = None
    
    def draw_stack(self) -> pg.Surface:
        #   draws the stack on one surface

        img = pg.transform.scale(
            pg.transform.rotate(self.stacks[0], self.angle), self.size)
        img = pg.Surface((img.get_width(), img.get_height() * self.spread))
        img.fblits()
        #   TODO: Finish draw_stack

        return img