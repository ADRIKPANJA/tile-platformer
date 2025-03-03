# event_handler.py

import sys, pygame, logger
from tile_engine import save_load
import time

'''Module to handle events'''

def setup():
    logger.setup()
    global let, ltp
    let = 0
    ltp = None

def events() -> None:
    global let, ltp
    '''Handle the events'''
    mouse = False
    ct = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            logger.log('Game session finished')
            sys.exit()