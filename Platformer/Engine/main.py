# main.py

import tile_engine.tile
import yaml
import os
import pygame as pg
import event_handler

'''The mainloop of the game'''

pg.init()

tiles = tile_engine.tile.initialize_engine()

yaml_location = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tile_engine', 'settings.yaml'))

# Global vars
global height, width
height: int
width: int

with open(yaml_location, 'r') as file:
    loaded_data = yaml.safe_load(file)
    height = loaded_data['Screen_Height']
    width = loaded_data['Screen_Width']

global screen
screen: pg.Surface

if loaded_data['Resizable']:
    screen = pg.display.set_mode((width, height), pg.RESIZABLE)
else:
    screen = pg.display.set_mode((width, height))

# Function to get the width and height
def get_dimensions() -> tuple[int, int]:
    '''Get the screen dimensions'''
    global width, height
    return width, height

def main() -> None:
    '''Mainloop'''
    while True:
        event_handler.events()
        tiles.update(0, 0)
        screen.fill("white")
        tiles.draw(screen)
        pg.display.update()
        pg.time.Clock().tick(60)

if __name__ == "__main__":
    main()