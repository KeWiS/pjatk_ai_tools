from board import Board


class Game:
    """
    Main class of the game.

    It initializes board and manages course of the game
    """

    def __init__(self):
        self._board = Board()
        """
        Overwritten method, calls board print
        """
        self._board.print_board()
        """
        Calculates possible moves in brute-force way.

        :return: list of possible move coordinates
        :rtype: list
        """
        """
        Calculates flipped pawns if move occurred on given position.

        It is calculated in brute-force way, similarly to possible_moves() method.

        :param position: position for which flipped pawns shall be calculated
        :type position: tuple
        :return: list of flipped pawns after move performed on given position
        :rtype: list
        """
        """
        Determines if game is over.

        Prints possible moves for every player to ease the game experience.

        :return: true - player has at least one possible move, false otherwise
        :rtype: bool
        """
        """
        Prints possible moves for current player

        :param possible_moves: list of possible moves
        :type possible_moves: list
        """
