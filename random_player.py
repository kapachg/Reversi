from abstract_player import AbstractPlayer
import random

class RandomPlayer(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, possible_moves):
        """
        Randomly choice a move from the list
        :param possible_moves:
        :return:

        a tuple of x,y (int, int) coordinates
        """
        return random.choice(possible_moves)