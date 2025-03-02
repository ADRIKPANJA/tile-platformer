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

def events() -> bool:
    global let, ltp
    '''Handle the events'''
    mouse = False
    ct = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            logger.log('Game session finished')
            sys.exit()
        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN) and pygame.mouse.get_pressed()[0]:
            mouse = True
            mp = pygame.mouse.get_pos()
            if (ct - let) > 0.1 and mp != ltp:
                let = ct
                ltp = mp
                return True
    return False