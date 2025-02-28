# tile.py

import pygame as pg
from . import asset_fetch
from . import coordinate_translator as ct

'''The main engine required for the game to run'''

def initialize_engine() -> pg.sprite.Group:
    '''The function initializes the engine, without this function executed, the tile engine will fail'''
    asset_fetch._import()
    tiles = pg.sprite.Group()
    tile_x, tile_y = 10 * -16, 0
    for x in range(0, 10):
        tile_y = 10 * -16
        for y in range(0, 10):
            tiles.add(Tile(tile_x, tile_y))
            tile_y += 32
        tile_x += 32
    return tiles

class Tile(pg.sprite.Sprite):
    '''A single tile of the game'''
    def __init__(self, tile_x: int, tile_y: int) -> None:
        '''Initialize the tile'''
        super().__init__()
        self.image = asset_fetch._2
        self.rect = self.image.get_rect()
        self.tile_x, self.tile_y = tile_x, tile_y
        self.rect.center = (self.tile_x, self.tile_y)

    def update(self, cameraX: float, cameraY: float) -> None: # Float is required as there will be motion smoothing in camera movements
        '''Update the tile'''
        self.rect.center = ct.from_center_coordinate(self.tile_x - cameraX, self.tile_y - cameraY)