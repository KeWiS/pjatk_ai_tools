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
        """
        :return: Field status of the field
        :rtype: FieldStatus
        """
        return self._status

    def set_status(self, status: FieldStatus):
        """
        Changes field status of the field for the one given as argument

        :param status: Field status to be changed
        :type status: FieldStatus
        """
        self._status = status
