# default_world_gen.py

from tile_engine import asset_fetch

'''Module to generate the default level'''

def generate() -> tuple[list, int, int]:
    '''Generate'''
    asset_fetch._import()
    world_data = []
    grid_height = 50
    grid_width = 50
    def wall():
        for i in range(grid_height):
            world_data.append(asset_fetch._2)
    def column():
        world_data.append(asset_fetch._2)
        for i in range(grid_height - 2):
            world_data.append(asset_fetch._1)
        world_data.append(asset_fetch._2)
    wall()
    for i in range(grid_width - 2):
         column()
    wall()
    print(world_data)
    return world_data, grid_height, grid_width