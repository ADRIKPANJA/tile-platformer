# main.py

import tile_engine.tile
import yaml
import os
import pygame as pg
import event_handler
import default_world_gen as gen
from datetime import datetime

'''The mainloop of the game'''

pg.init()

yaml_location = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tile_engine', 'settings.yaml'))

if __name__ == "__main__":
    log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.platformer', 'Logs'))
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file_location = os.path.abspath(os.path.join(log_dir, f'log_{datetime.now().strftime("%d%m%Y%H%M%S")}.log'))

    with open(log_file_location, 'a') as file_log:
        print(f'[Info!] Game started on {os.name}', file=file_log)

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

if loaded_data['Fullscreen']:
    screen = pg.display.set_mode((width, height), pg.FULLSCREEN)
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

world_data, grid_height, grid_width = gen.generate()
global tiles
tiles = tile_engine.tile.initialize_engine(cloneX=cloneX, cloneY=cloneY, world_data=world_data, grid_height=grid_height)

# Velocities of camera
global Xv, Yv
Xv: float = 0
Yv: float = 0

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

def main() -> None:
    '''Mainloop'''
    while True:
        dt = pg.time.Clock().tick(240) / 1000
        global cloneX, cloneY
        event_handler.events()
        control_camera(dt)
        tiles.update(camX, camY, cloneX, cloneY)
        screen.fill("white")
        tiles.draw(screen)
        pg.display.update()

if __name__ == "__main__":
    main()