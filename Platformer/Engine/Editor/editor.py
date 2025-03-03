# editor.py

from . import find_tile, keymapper
import pygame as pg
import tile_engine.coordinate_translator as ct
import tile_engine.asset_fetch
import time

'''The editor class'''

def setup() -> None:
    '''Sets up the environment'''
    tile_engine.asset_fetch._import()

class Editor():
    '''The class for editor.'''
    def __init__(self) -> None:
        super().__init__()
        self.EDITOR = True
        self.pt = 0
        self.li = 0
        self.keymap = keymapper.Keymapper()
        self.chosen_brush = pg.surface.Surface((32, 32))

    def update(self, camX: float, camY: float, grid_height: int, world_data: list, mouse: bool) -> None:
        '''Update the editor'''
        self.chosen_brush = self.keymap.get_surface()
        if not (self.EDITOR and mouse):
            return
        ctime = time.time()
        mouseX, mouseY = ct.to_center_coordinate(pg.mouse.get_pos()[0] - 32, pg.mouse.get_pos()[1] + 32)
        tile, idx = find_tile.get_tile_at(mouseX + camX, mouseY + camY, grid_height, world_data)
        if self.li == idx:
            return
        if (ctime - self.pt) > 0.001:
            self.pt = ctime
            self.li = idx
            if tile == self.chosen_brush:
                brush = tile_engine.asset_fetch._1
            else:
                brush = self.chosen_brush
            try:
                world_data[idx] = brush
            except IndexError:
                return
    
    def toggle_edit_mode(self):
        self.EDITOR = not self.EDITOR