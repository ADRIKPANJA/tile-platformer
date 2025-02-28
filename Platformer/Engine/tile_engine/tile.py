# tile.py

import pygame as pg
from . import asset_fetch
from . import coordinate_translator as ct

'''The main engine required for the game to run'''

def initialize_engine(world_data: list, cloneX: int, cloneY: int, grid_height: int) -> pg.sprite.Group:
    '''The function initializes the engine, without this function executed, the tile engine will fail'''
    asset_fetch._import()
    tiles = pg.sprite.Group()
    idx = 0
    tile_x, tile_y = 48, 0
    for x in range(cloneX):
        tile_y = 48
        for y in range(cloneY):
            tiles.add(Tile(tile_x, tile_y, idx, world_data, grid_height))
            tile_y += 32
            idx += 1
        tile_x += 32
        idx += (grid_height - cloneY)
    return tiles

class Tile(pg.sprite.Sprite):
    '''A single tile of the game'''
    def __init__(self, tile_x: int, tile_y: int, idx: int, world_data: list, grid_height: int) -> None:
        '''Initialize the tile'''
        super().__init__()
        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.tile_x, self.tile_y = tile_x, tile_y
        self.rect.center = (self.tile_x, self.tile_y)
        self.idx = idx
        self.world_data = world_data
        self.grid_height = grid_height

    def update(self, cameraX: float, cameraY: float, cloneX: float, cloneY: float) -> None: # Float is required as there will be motion smoothing in camera movements
        '''Update the tile'''
        if abs(self.tile_x - cameraX) > cloneX * 15.9:
            if self.tile_x < cameraX:
                self.tile_x += cloneX * 32
                self.idx += cloneX * self.grid_height
            else:
                self.tile_x -= cloneX * 32
                self.idx -= cloneX * self.grid_height
        if abs(self.tile_y - cameraY) > cloneY * 15.9:
            if self.tile_y < cameraY:
                self.tile_y += cloneY * 32
                self.idx += cloneY
            else:
                self.tile_y -= cloneY * 32
                self.idx -= cloneY
        self.rect.center = ct.from_center_coordinate(self.tile_x - cameraX, self.tile_y - cameraY)
        try:
            self.image = self.world_data[self.idx]
        except IndexError:
            self.image = asset_fetch._1