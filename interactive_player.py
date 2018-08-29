from abstract_player import AbstractPlayer
from ui import UI

class InteractivePlayer(AbstractPlayer):

    def __init__(self, color):
        self.color = color
        self.ui = UI()

    def get_move(self, board, possible_moves):
        """Chooses an action from the given actions

        :param board: The current board state. It is a matrix whose cells are of the enum type Disk.
        :param possible_moves: A list of possible moves. Each move is a tuple of coordinates (x, y).
        :return: The desired move in the list of possible moves (a tuple).
        """

        return self.ui.user_move(self.color, possible_moves)