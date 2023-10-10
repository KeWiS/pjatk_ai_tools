from field_status import FieldStatus


class Field:
    """
    Board field

    Can be on of three states
    
    FieldStatus: 1 -> "B", 2 -> "W", 0 -> "|"

    Latter meaning empty field
    """

    def __init__(self):
        self._status = FieldStatus.EMPTY

    def get_status(self):
        return self._status.value

    def set_status(self, status: FieldStatus):
        self._status = status
