from field import Field


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

    def print_board(self):
        """
        Prints the game board
        """
        for row in self.fields:
            row_str = ""
            for cell in row:
                row_str += cell.get_status() + " "

            print(row_str)
