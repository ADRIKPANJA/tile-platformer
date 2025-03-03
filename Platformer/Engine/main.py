# main.py

import tile_engine.tile
import yaml
import os
import pygame as pg
import event_handler
import default_world_gen as gen
import logger
from tile_engine import save_load
from Editor.editor import Editor
from tile_engine import asset_fetch

'''The mainloop of the game'''

pg.init()

yaml_location = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tile_engine', 'settings.yaml'))

logger.setup()
event_handler.setup()

if __name__ == "__main__":
    logger.log(f'[Info!] Game started on {os.name}')

# Global vars
global height, width
height: int = 600
width: int = 800

with open(yaml_location, 'r') as file:
    loaded_data = yaml.safe_load(file)
    height = loaded_data['Screen_Height']
    width = loaded_data['Screen_Width']

global screen
screen: pg.Surface

if loaded_data['Fullscreen'] and loaded_data["Hardware_Accel"]:
    screen = pg.display.set_mode((width, height), pg.FULLSCREEN | pg.HWSURFACE | pg.DOUBLEBUF)
    if __name__ == "__main__":
        logger.log('HW Accel enabled!')
elif loaded_data['Fullscreen']:
    screen = pg.display.set_mode((width, height), pg.FULLSCREEN)
elif loaded_data["Hardware_Accel"]:
    screen = pg.display.set_mode((width, height), pg.HWSURFACE | pg.DOUBLEBUF)
    if __name__ == "__main__":
        logger.log('HW Accel enabled!')
else:
    screen = pg.display.set_mode((width, height))

# Function to get the width and height
def get_dimensions() -> tuple[int, int]:
    '''Get the screen dimensions'''
    return screen.get_width(), screen.get_height()

global camX, camY
init_x, init_y = get_dimensions()
camX: float = init_x/2 + 32
camY: float = init_y/2 + 32

global cloneX, cloneY
cloneX, cloneY = get_dimensions()[0]//32 + 2, get_dimensions()[1]//32 + 2

global world_data
world_data, grid_height, grid_width = save_load._import('Test') # it works!

#world_data, grid_height, grid_width = gen.generate()
global tiles
tiles = tile_engine.tile.initialize_engine(cloneX=cloneX, cloneY=cloneY, world_data=world_data, grid_height=grid_height)

# Velocities of camera
global Xv, Yv
Xv: float = 0
Yv: float = 0

editor = Editor()
# Camera controller
def control_camera(dt) -> None:
    global camX, camY, Xv, Yv
    '''The function to control the camera based on key inputs.'''
    keys = pg.key.get_pressed()
    Xv = ((keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * 600 * dt) + (Xv * 0.8)
    Yv = ((keys[pg.K_UP] - keys[pg.K_DOWN]) * 600 * dt) + (Yv * 0.8)
    camX += Xv
    camY += Yv
    if camX < get_dimensions()[0]/2 + 32:
        camX = get_dimensions()[0]/2 + 32
    if camY < get_dimensions()[1]/2 + 32:
        camY = get_dimensions()[1]/2 + 32
    if camX > (grid_width * 32) - get_dimensions()[0]/2 + 32:
        camX = (grid_width * 32) - get_dimensions()[0]/2 + 32
    if camY > (grid_height * 32) - get_dimensions()[1]/2 + 32:
        camY = (grid_height * 32) - get_dimensions()[1]/2 + 32

def main(clock: pg.time.Clock) -> None:
    '''Mainloop'''
    global world_data, grid_height, grid_width, tiles, cloneX, cloneY
    while True:
        if pg.key.get_pressed()[pg.K_e]:
            save_load.export('Test', world_data, grid_height, grid_width)
        if pg.key.get_pressed()[pg.K_i]:
            world_data, grid_height, grid_width = save_load._import('Test') # it works!
            tiles = tile_engine.tile.initialize_engine(world_data, cloneX, cloneY, grid_height)
        if pg.key.get_pressed()[pg.K_g]:
            world_data, grid_height, grid_width = gen.generate()
            tiles = tile_engine.tile.initialize_engine(world_data, cloneX, cloneY, grid_height)
        if pg.key.get_pressed()[pg.K_x]:
            editor.toggle_edit_mode()
        fps = str(round(clock.get_fps()))
        txt = pg.font.Font(None, 60)
        suf = txt.render(fps, True, 'Black')
        dt = clock.tick(240) / 1000
        event_handler.events()
        control_camera(dt)
        tiles.update(camX, camY, cloneX, cloneY)
        editor.update(camX, camY, grid_height, world_data, pg.mouse.get_pressed()[0])
        screen.fill("white")
        tiles.draw(screen)
        screen.blit(suf, (10, 10))
        if editor.keymap.empty:
            screen.blit(asset_fetch.erasor, (10, 50))
        else:
            screen.blit(editor.keymap.current, (10, 50))
        pg.display.update()

if __name__ == "__main__":
    clock = pg.time.Clock()
    main(clock)