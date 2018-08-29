from abstract_player import AbstractPlayer
import random

class RandomPlayer(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board, possible_moves):
        """Chooses an action from the given actions

        :param board: The current board state. It is a matrix whose cells are of the enum type Disk.
        :param possible_moves: A list of possible moves. Each move is a tuple of coordinates (x, y).
        :return: The desired move in the list of possible moves (a tuple).
        """

        return random.choice(possible_moves)