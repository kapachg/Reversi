from abstract_player import AbstractPlayer
import copy
import math

class SimplePlayer(AbstractPlayer):
    """ This player determines its next move by each move's score (ie - comparing disks' number)
    """

    def __init__(self, color):
        """
        Initializing the class with its color
        :param color: Disk.DARK or Disk.LIGHT
        """
        super().__init__(color)

    def get_move(self, board, rules, possible_moves, enemy_color):
        """
        Determine best score move from a list of possible moves

        :param board: the current board object, necessary for evaluating possible moves
        :param rules: the current rules object,  necessary for evaluating possible moves
        :param possible_moves: a list of tuples(int, int)
        :param enemy_color: Disk enum
        :return:

        chosen_move: a tuple of x,y (int, int) coordinates
        """
        max = -math.inf
        for move in possible_moves:
            score = self.evaluate_board(board, rules, move, enemy_color)
            if (score > max):
                chosen_move = move
                max = score
        return chosen_move

    def evaluate_board(self, board, rules, move, enemy_color):
        """ Returns number of disks minus number of opponent's disks

        :param board: the current board object, necessary for evaluating possible moves
        :param rules: the current rules object,  necessary for evaluating possible moves
        :param move: a tuple of x,y coordinates (int)
        :param enemy_color: Disk enum
        :return:

        score: an int
        """
        simulation = copy.deepcopy(board)

        res = rules.validate_move(simulation.current_state(), move, self.color, enemy_color)

        for direction in res[move]:
            i, j = direction
            x, y = move

            simulation.place_disk(x, y, self.color)
            x += i
            y += j
            while rules.check_board_limits(x, y) and board.current_state()[x][y] == enemy_color:
                simulation.place_disk(x, y, self.color)
                x += i
                y += j

        count = simulation.count_disks()
        return count[self.color] - count[enemy_color]