# keymapper.py

import pygame as pg
from tile_engine import asset_fetch

'''This is the module for editor to manage tile keymaps.'''

def setup() -> None:
    '''Setup'''
    asset_fetch._import()

class Keymapper():
    '''A class to manage keymapper'''
    def __init__(self):
        super().__init__()
        self.varmap = {
            "1": asset_fetch._1,
            "2": asset_fetch._2,
            "3": asset_fetch._3
        }
        self.keymap = [
            pg.K_1,
            pg.K_1,
            pg.K_1
        ]
        self.idx = 0
        self.last_press = 0
        self.current = asset_fetch._1
        self.empty = True
    
    def get_surface(self) -> pg.surface.Surface:
        '''Get the surface according to the specified keymaps'''
        ctime = pg.time.get_ticks()
        for _ in range(len(self.keymap)):
            self.idx = (self.idx + 1) % len(self.keymap)
            if (pg.key.get_pressed()[self.keymap[self.idx]]) and (ctime - self.last_press) > 200:
                self.last_press = ctime
                print(self.varmap[str(self.idx + 1)], self.idx + 1)
                self.current = self.varmap[str(self.idx + 1)]
                return self.current
        if self.current is self.varmap["1"]:
            self.empty = True
        else:
            self.empty = False
        return self.current