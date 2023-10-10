from field import Field
from field_status import FieldStatus


class Board:
    """
    Game board

    Contains 8x8 fields.

    Each field can be on of three states

    "B", "W", "E"

     Methods:
        print_board():
            Prints the board in readable format
    """

    def __init__(self):
        self.fields = [[Field() for j in range(8)] for i in range(8)]
        self._set_initial_board_state()

    def _set_initial_board_state(self):
        self.fields[3][3].set_status(FieldStatus.WHITE)
        self.fields[4][4].set_status(FieldStatus.WHITE)
        self.fields[3][4].set_status(FieldStatus.BLACK)
        self.fields[4][3].set_status(FieldStatus.BLACK)

    def print_board(self):
        """
        Prints the game board
        """
        for row in self.fields:
            row_str = ""
            for cell in row:
                row_str += cell.get_status() + "  "

            print(row_str)
