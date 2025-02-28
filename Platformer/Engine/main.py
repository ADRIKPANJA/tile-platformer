# main.py

import tile_engine.tile
import yaml
import os
import pygame as pg
import event_handler
from tile_engine import coordinate_translator as ct

'''The mainloop of the game'''

pg.init()

global tiles
tiles = tile_engine.tile.initialize_engine()

yaml_location = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tile_engine', 'settings.yaml'))

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
init_x, init_y = (-get_dimensions()[0]/2, -get_dimensions()[1]/2)
camX: float = init_x
camY: float = init_y

# Camera controller
def control_camera() -> None:
    global camX, camY
    '''The function to control the camera based on key inputs.'''
    keys = pg.key.get_pressed()
    camX += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * 5
    camY += (keys[pg.K_UP] - keys[pg.K_DOWN]) * 5
def main() -> None:
    '''Mainloop'''
    while True:
        global tiles
        cloneX, cloneY = get_dimensions()[0]/32, get_dimensions()[1]/32
        event_handler.events()
        control_camera()
        tiles.update(camX, camY, cloneX + 1, cloneY + 1) # offsets by 1 to reduce edge flickering
        screen.fill("white")
        tiles.draw(screen)
        pg.display.update()
        pg.time.Clock().tick(60)

if __name__ == "__main__":
    main()