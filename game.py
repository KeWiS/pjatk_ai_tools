import numpy as np
from easyAI import TwoPlayerGame

from board import Board
from field_status import FieldStatus


class Game(TwoPlayerGame):
    """
    Main class of the game.

    It initializes board and manages course of the game
    """

    POSSIBLE_MOVE_DIRECTIONS = [
        np.array([x, y]) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x != 0 or y != 0)
    ]

    BOARD_SCORING = np.array(
        [
            [9, 3, 3, 3, 3, 3, 3, 9],
            [3, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 3],
            [9, 3, 3, 3, 3, 3, 3, 9],
        ]
    )

    def __init__(self, players):
        self.players = players
        self.current_player = 1
        self._board = Board()

    def show(self):
        """
        Overwritten method, calls board print
        """
        self._board.print_board()

    def possible_moves(self):
        """
        Calculates possible moves in brute-force way.

        :return: list of possible move coordinates
        :rtype: list
        """
        return [
            self._board.get_field_string(x, y)
            for x in range(8)
            for y in range(8)
            if (self._board.get_field_status(x, y) == FieldStatus.EMPTY) and (self._flipped_pawns((x, y)) != [])
        ]

    def _flipped_pawns(self, position: tuple):
        """
        Calculates flipped pawns if move occurred on given position.

        It is calculated in brute-force way, similarly to possible_moves() method.

        :param position: position for which flipped pawns shall be calculated
        :type position: tuple
        :return: list of flipped pawns after move performed on given position
        :rtype: list
        """
        flipped_pawns = []

        for possible_direction in self.POSSIBLE_MOVE_DIRECTIONS:
            altered_position = position + possible_direction
            struck_pawns = []
            while (0 <= altered_position[0] <= 7) and (0 <= altered_position[1] <= 7):
                target_field_value = self._board.get_field_status(altered_position[0], altered_position[1]).value
                if target_field_value == 3 - self.current_player:
                    struck_pawns.append(+altered_position)
                elif target_field_value == self.current_player:
                    flipped_pawns += struck_pawns
                    break
                else:
                    break
                altered_position += possible_direction

        return flipped_pawns

    def make_move(self, move):
        flipped = self._flipped_pawns(self._board.get_field_coordinates(move))
        move_x = self._board.get_field_coordinates(move)[0]
        move_y = self._board.get_field_coordinates(move)[1]
        self._board.set_field_status(move_x, move_y, FieldStatus(self.current_player))
        for x, y in flipped:
            self._board.set_field_status(x, y, FieldStatus(self.current_player))

    def is_over(self):
        """
        Determines if game is over.

        Prints possible moves for every player to ease the game experience.

        :return: true - player has at least one possible move, false otherwise
        :rtype: bool
        """
        possible_moves = self.possible_moves()
        self._print_possible_moves_for_current_player(possible_moves)
        return possible_moves == []

    def scoring(self):
        if np.sum(self._board == 0) > 32:
            player = (self._board == self.current_player).astype(int)
            opponent = (self._board == 2).astype(int)
            return ((player - opponent) * self.BOARD_SCORING).sum()
        else:
            no_pieces_player = np.sum(self._board == self.current_player)
            no_pieces_opponent = np.sum(self._board == 2)
            return no_pieces_player - no_pieces_opponent

    def _print_possible_moves_for_current_player(self, possible_moves):
        """
        Prints possible moves for current player

        :param possible_moves: list of possible moves
        :type possible_moves: list
        """
        print("Possible moves for player " + FieldStatus.map_field_status_value_to_string(self.current_player))
        print(possible_moves)
