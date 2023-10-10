from enum import Enum


class FieldStatus(Enum):
    """
    Enumeration for baord field status

     EMPTY: "E" - Empty field

     WHITE: "W" - Field occupied by white pawn

     BLACK: "B" - Field occupied by black pawn
    """
    EMPTY = "|"
    WHITE = "W"
    BLACK = "B"
