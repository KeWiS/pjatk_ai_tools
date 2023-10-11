from field import Field
from field_status import FieldStatus


class Board:
    """
    Game board

    Contains 8x8 fields.

    Each field can be on of three states

    1 -> "B", 2 -> "W", 0 -> "|"

    Latter meaning empty field
    """

    BORDER_LETTERS = "ABCDEFGH"
    LETTER_BORDER = "   " + "  ".join(BORDER_LETTERS) + "  "
    BORDER_NUMBERS = "87654321"

    def __init__(self):
        self._fields = [[Field() for j in range(8)] for i in range(8)]
        self._set_initial_board_state()

    def _set_initial_board_state(self):
        """
        Sets initial game state

        White pawns are at coordinates D5 and E4

        Black pawns are at coordinates D4 and E3
        """
        self._fields[3][3].set_status(FieldStatus.WHITE)
        self._fields[4][4].set_status(FieldStatus.WHITE)
        self._fields[3][4].set_status(FieldStatus.BLACK)
        self._fields[4][3].set_status(FieldStatus.BLACK)

    def print_board(self):
        """
        Prints the game board with the coordinate borders
        """
        print(self.LETTER_BORDER)

        i = 8
        for row in self._fields:
            row_str = str(i) + "  "
            for cell in row:
                row_str += FieldStatus.map_field_status_to_string(cell.get_status()) + "  "

            print(row_str + str(i))
            i -= 1

        print(self.LETTER_BORDER)

    def get_field_string(self, x_cord: int, y_cord: int):
        """
        Calculates field string based on integer coordinates

        :param x_cord: Letter coordinate, range a-h
        :type x_cord: int
        :param y_cord: Digit coordinate, range 8-1
        :type y_cord: int
        :return: String of the field coded in coord type, eg. 5B, 2C
        :rtype: str
        """
        return self.BORDER_LETTERS[x_cord] + self.BORDER_NUMBERS[y_cord]

    def get_field_status(self, x_cord: int, y_cord: int):
        """
        Returns FieldStatus of field with given coordinates

        :param x_cord: Letter coordinate, range a-h
        :type x_cord: int
        :param y_cord: Digit coordinate, range 8-1
        :type y_cord: int
        :return: Field status of field with given coordinates
        :rtype: FieldStatus
        """
        return self._fields[y_cord][x_cord].get_status()

    def set_field_status(self, x_cord: int, y_cord: int, status: FieldStatus):
        self._fields[y_cord][x_cord].set_status(status)

    def get_field_coordinates(self, coordinates_str: str):
        """
        

        :param coordinates_str: 
        :type coordinates_str: str
        :return: numpy nd array with two coordinates
        :rtype: numpy nd array
        """
        return (self.BORDER_LETTERS.index(coordinates_str[0]), self.BORDER_NUMBERS.index(coordinates_str[1]))
