from enum import Enum


class CleanlinessLevel(Enum):
    CLEAN = 0
    DIRTY = 1

    @staticmethod
    def map_cleanliness_to_string(status):
        if status == CleanlinessLevel.CLEAN:
            return "C"
        elif status == CleanlinessLevel.DIRTY:
            return "D"
