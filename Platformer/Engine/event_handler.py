# event_handler.py

import sys, pygame

'''Module to handle events'''

def events() -> None:
    '''Handle the events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()