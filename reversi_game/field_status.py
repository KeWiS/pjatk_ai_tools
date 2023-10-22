from enum import Enum


class FieldStatus(Enum):
    """
    Enumeration for baord field status

     EMPTY: 0 -> "|" - Empty field

     BLACK: 1 -> "B" - Field occupied by black pawn

     WHITE: 2 -> "W" - Field occupied by white pawn
    """
    EMPTY = 0
    BLACK = 1
    WHITE = 2

    @staticmethod
    def map_field_status_value_to_string(value: int):
        """
        Maps field status value to readable string corresponding to the field status

        Needed for example to print board

        :param value: Field status value to be mapped
        :type value: int
        :return: String corresponding to the field status
        :rtype: str
        """
        if value == FieldStatus.EMPTY.value:
            return "|"
        elif value == FieldStatus.WHITE.value:
            return "W"
        elif value == FieldStatus.BLACK.value:
            return "B"

    @staticmethod
    def map_field_status_to_string(status):
        """
        Maps field status enum to readable string corresponding to the field status

        Needed for example to print board

        :param status: Field status to be mapped
        :type status: FieldStatus
        :return: String corresponding to the field status
        :rtype: str
        """
        if status == FieldStatus.EMPTY:
            return "|"
        elif status == FieldStatus.WHITE:
            return "W"
        elif status == FieldStatus.BLACK:
            return "B"
