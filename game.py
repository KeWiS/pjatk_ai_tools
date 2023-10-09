from board import Board


class Game:
    """
    Main class of the game.

    It initializes board and manages course of the game
    """

    def __init__(self):
        self._board = Board()
        self._board.print_board()
