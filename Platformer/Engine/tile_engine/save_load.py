# save_load.py

import pygame as pg
import os
import json
import logger

'''The module to manage read and write'''

def setup() -> str:
    '''This function sets up the environment to read-write'''
    save_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.platformer', 'Saves'))
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    return save_folder

# Encode and decode colors
def encode_color(color: pg.color.Color) -> tuple:
    '''pg.color -> tuple'''
    return (color.r, color.g, color.b, color.a)

def decode_color(tpl: tuple) -> pg.color.Color:
    '''tuple => pg.color'''
    return pg.color.Color(*tpl)

# Encode and decode surfaces
def encode_surface(surface: pg.surface.Surface) -> dict:
    '''Encode a surface'''
    height = surface.get_height()
    width = surface.get_width()
    pixels = []
    for x in range(width):
        for y in range(height):
            pixels.append(encode_color(surface.get_at((x, y))))
    encoded_data = {
        "height": height,
        "width": width,
        "pixels": pixels
    }
    return encoded_data

def decode_surface(surface_dict: dict) -> pg.surface.Surface:
    '''Decode a surface'''
    height = surface_dict["height"]
    width = surface_dict["width"]
    surface = pg.surface.Surface((width, height))
    surface.fill(pg.color.Color(0, 0, 0, 0))
    pixels = surface_dict["pixels"]
    idx = 0
    for x in range(width):
        for y in range(height):
            surface.set_at((x, y), decode_color(pixels[idx]))
            idx +=1
    return surface

def export(json_name: str, world_data: list, height: int, width: int) -> None:
    '''Export the world data'''
    encoded = {}
    temp = []
    for surface in world_data:
        temp.append(encode_surface(surface))
        encoded["h"] = height
        encoded["w"] = width
    encoded["data"] = temp
    folder = setup()
    json_file = os.path.abspath(os.path.join(folder, f'{json_name}.json'))
    if os.path.exists(json_file):
        raise FileExistsError('Cannot overwrite an existing file')
    try:
        with open(json_file, 'w') as file:
            json.dump(encoded, file)
    except Exception as e:
        logger.log(f'[Error!] An unexpected error occured while saving file {e}')
        return
    logger.log('[Info!] Exported!')

def _import(json_name: str) -> tuple[list, int, int]:
    '''import the world data'''
    folder = setup()
    json_file = os.path.abspath(os.path.join(folder, f'{json_name}.json'))
    encoded = {}
    try:
        with open(json_file, 'r') as file:
            encoded = json.load(file)
    except Exception as e:
        logger.log(f'[Error!] An unexpected error occured while loading file {e}')
        return [], 0, 0
    world_data = []
    for surface in encoded["data"]:
        world_data.append(decode_surface(surface))
    return world_data, encoded["h"], encoded["w"]