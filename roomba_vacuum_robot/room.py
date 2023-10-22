from tile import Tile
from cleanliness_level import CleanlinessLevel


class Room:
    def __init__(self):
        self._tiles = [[Tile() for j in range(6)] for i in range(9)]

    def print_room(self):
        for row in self._tiles:
            row_str = ""
            for tile in row:
                row_str += CleanlinessLevel.map_cleanliness_to_string(tile.get_cleanliness()) + "  "

            print(row_str)
