# coordinate_translator.py

"""The module to translate coordinates from center based to pygame based"""

def from_center_coordinate(x: float, y: float) -> tuple[int, int]:
    '''Translate'''
    import main
    main
    width, height = main.get_dimensions()
    return x + (width / 2), -y + (height / 2)

def to_center_coordinate(x: float, y: float) -> tuple[int, int]:
    '''Translate'''
    import main
    main
    width, height = main.get_dimensions()
    return x - (width / 2), -(y - (height / 2))