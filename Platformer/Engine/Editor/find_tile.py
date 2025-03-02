# find_tile.py

import tile_engine.coordinate_translator 
import pygame as pg
import tile_engine.asset_fetch

'''The module to find tiles and return its surface value'''

# asset_fetch._1 is an empty tile

def get_tile_at(x: int, y: int, grid_height: int, world_data: list) -> tuple[pg.surface.Surface, int]:
    '''Get the tile data at x and y'''
    grid_x = int(x) // 32
    grid_y = int(y) // 32
    idx = grid_y + grid_x * grid_height
    try:
        return world_data[idx], idx
    except IndexError:
        tile_engine.asset_fetch._import()
        return tile_engine.asset_fetch._1, idx