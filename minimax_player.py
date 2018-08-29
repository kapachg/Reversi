from abstract_player import AbstractPlayer
from math import inf
import random
import copy
from rules import Rules


class Player06(AbstractPlayer):

    def __init__(self):
        super().__init__(self, color)
        if self.color == Disk.DARK:
            self.other_color = Disk.LIGHT
        else:
            self.other_color = Disk.DARK
        self.rules = Rules()

    def minimax(self, board, depth=2, maximizer=True):


        simulation = copy.deepcopy(board)
        moves = rules.possible_moves(simulation, self.color, self.other_color)
        for move in moves:



        if (depth == 0) or (node.endofgame):
            return self.calculate_value(node)
        if maximizer:
            value = -inf
            for child in node:
                value = max(value, minimax(child, depth-1, False))
            return value
        else:
            value = inf
            for child in node:
                value = min(value, minimax(child, depth-1, True))
            return value

    def calculate_value(self, board):
        if self.endofgame(board):
            return inf
        return random.randrange(10,1001, 10)


    # This method is not effecient by itself, when applying real value it should be
    # integrated into calculate_value (because the possible_moves are already calculated)
    def endofgame(self, board):
        self_moves = self.rules.possible_moves(board, self.color, other_color)
        if not self_moves:
            if not self.rules.pass_turn_when_no_moves:
                return True
            else:
                other_moves = self.rules.possible_moves(board, other_color, self.color)
                if not other_moves:
                    return True
        return False




    def get_move(self, board, possible_moves):
        max = -math.inf
        for move in possible_moves:
            score = self.minimax(depth=2)   # evaluate_board(board, rules, move, enemy_color)
            if (score > max):
                chosen_move = move
                max = score
        return chosen_move