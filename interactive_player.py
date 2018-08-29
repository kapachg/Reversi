from abstract_player import AbstractPlayer

class InteractivePlayer(AbstractPlayer):

    def __init__(self, color):
        self.color = color

    def get_move(self, ui, possible_moves):
        """
        Asks the user for its next move.
        :param ui: gets the current UI object for interaction with the user
        :param possible_moves: a list of the possible moves
        :return:

        a tuple of x,y (int, int) coordinates
        """
        return ui.user_move(self.color, possible_moves)