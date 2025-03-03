# asset_fetch.py

import os
import pygame as pg

"""The module to fetch the assets. Get the assets by accessing this module's attributes."""

# Declare Global Vars
global _1, _2, _3, erasor
_1: pg.Surface
_2: pg.Surface
_3: pg.Surface
erasor: pg.Surface

# Import the images
def __import() -> tuple[str, str]:
    '''This function imports the assets do not use this, use the _import() method instead.'''
    base_path = os.path.abspath(os.path.dirname(__file__))
    _1_path = os.path.abspath(os.path.join(base_path, '..', '..', 'Assets', 'Tiles', '1.svg'))
    _2_path = os.path.abspath(os.path.join(base_path, '..', '..', 'Assets', 'Tiles', '2.svg'))
    _3_path = os.path.abspath(os.path.join(base_path, '..', '..', 'Assets', 'Tiles', '3.svg'))
    erasor_path = os.path.abspath(os.path.join(base_path, '..', '..', 'Assets', 'Icons', 'erasor.png'))
    return _1_path, _2_path, _3_path, erasor_path

# Function to import all the assets
def _import() -> None:
    '''This function imports the assets'''
    global _1, _2, _3, erasor
    temp1, temp2, temp3, temp4 = __import()
    _1, _2, _3, erasor = pg.image.load(temp1), pg.image.load(temp2), pg.image.load(temp3), pg.image.load(temp4)