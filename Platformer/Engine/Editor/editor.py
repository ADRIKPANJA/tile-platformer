# editor.py

from . import find_tile
import pygame as pg
import logger
import tile_engine.coordinate_translator as ct
import tile_engine.asset_fetch

'''The editor class'''

def setup() -> None:
    '''Sets up the environment'''
    tile_engine.asset_fetch._import()

class Editor():
    '''The class for editor.'''
    def __init__(self) -> None:
        super().__init__()
        self.EDITOR = True

    def update(self, camX: float, camY: float, grid_height: int, world_data: list) -> None:
        '''Update the editor'''
        if self.EDITOR and pg.mouse.get_pressed()[0]:
            mouseX, mouseY = ct.to_center_coordinate(pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] + 32)
            _, idx = find_tile.get_tile_at(mouseX + camX, mouseY + camY, grid_height, world_data)
            try:
                world_data[idx] = tile_engine.asset_fetch._2
            except IndexError:
                return
    
    def toggle_edit_mode(self):
        self.EDITOR = not self.EDITOR