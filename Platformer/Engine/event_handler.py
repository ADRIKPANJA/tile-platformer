# event_handler.py

import sys, pygame, logger
from tile_engine import save_load

'''Module to handle events'''

def setup():
    logger.setup()

def events(world_data: list, grid_height: int, grid_width: int) -> None:
    '''Handle the events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            logger.log('Game session finished')
            save_load.export('Test', world_data, grid_height, grid_width)
            sys.exit()