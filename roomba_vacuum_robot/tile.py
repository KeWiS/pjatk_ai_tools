import random

from cleanliness_level import CleanlinessLevel


class Tile:
    def __init__(self):
        self._cleanliness = random.choice(list(CleanlinessLevel))

    def get_cleanliness(self):
        return self._cleanliness
