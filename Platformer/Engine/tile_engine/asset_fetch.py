# asset_fetch.py

import os
import pygame as pg

"""The module to fetch the assets. Get the assets by accessing this module's attributes."""

# Declare Global Vars
global _1, _2
_1: pg.Surface
_2: pg.Surface

# Import the images
def __import() -> tuple[str, str]:
    '''This function imports the assets do not use this, use the _import() method instead.'''
    base_path = os.path.abspath(os.path.dirname(__file__))
    _1_path = os.path.abspath(os.path.join(base_path), '..', 'Assets', 'Tiles', '1.svg')
    _2_path = os.path.abspath(os.path.join(base_path), '..', 'Assets', 'Tiles', '2.svg')
    return _1_path, _2_path

# Function to import all the assets
def _import() -> None:
    '''This function imports the assets'''
    global _1, _2
    temp1, temp2 = __import()
    _1, _2 = pg.image.load(temp1), pg.image.load(temp2)