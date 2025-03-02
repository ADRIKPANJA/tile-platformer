# event_handler.py

import sys, pygame, logger
from tile_engine import save_load

'''Module to handle events'''

def setup():
    logger.setup()

def events() -> None:
    '''Handle the events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            logger.log('Game session finished')
            sys.exit()