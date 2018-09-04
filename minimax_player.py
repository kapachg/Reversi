from abstract_player import AbstractPlayer
from math import inf
import copy
from rules import Rules
from disk import Disk
import random


class Player06(AbstractPlayer):

    def __init__(self, color):
        super().__init__(color)
        self.rules = Rules()
        self.evaluate_board()

    def minimax(self, board, depth=2, maximizer=True):
        if (depth == 0) or self.endofgame(board):
#           print(f"value = {self.calculate_value((board))}")
            return self.calculate_value(board)
        if (maximizer):
            func = max
            value = -inf
            color = self.color
        else:
            func = min
            value = inf
            color = self.rules.other_color(self.color)

        moves = self.rules.possible_moves(board, color)
        if len(moves) == 0:
            next_board = copy.deepcopy(board)
            value = func(value, self.minimax(next_board, depth-1, not maximizer))
            return value
#            value = inf * (-1,1)[is_bool]
        # no moves = deep_copy and minimax(not maximizer)

        for move in moves:
#            print(f"move = {move}")
            next_board = copy.deepcopy(board)
            self.rules.update_board(next_board, move, moves[move], color)
            value = func(value, self.minimax(next_board, depth-1, not maximizer))
#            print(f"{func.__name__}imizer value: {value}")
            return value

    def calculate_value(self, board):
        val = 0
        if (self.endofgame(board)):
            if self.color == self.rules.winner(board):
                return inf
            elif self.color == Disk.NONE:
                return 0
            else:
                return -inf
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == self.color):
                    sign = 1
                elif (board[i][j] == Disk.NONE):
                    sign = 0
                else:
                    sign = -1

                disk = self.rules.coordinates_to_user(i,j)
#                val += self.move_priority[disk] * sign
                try:
                    val += self.move_priority[disk] * sign
                except:
                    try:
                        val += self.move_count[disk] * sign
                    except:
                        val += sign * 100000
 #                       print(f"Disk: {disk} [{i,j}], val so far: {val}")
        #print(f"calval = {val}")
        return val


    # This method is not effecient by itself, when applying real value it should be
    # integrated into calculate_value (because the possible_moves are already calculated)
    def endofgame(self, board):
        self_moves = self.rules.possible_moves(board, self.color)
        if not self_moves:
            if not self.rules.pass_turn_when_no_moves:
                return True
            else:
                other_moves = self.rules.possible_moves(board, self.rules.other_color(self.color))
                if not other_moves:
                    return True
        return False


    def evaluate_board(self):
        import re
#        return
        #BUFFER = 8192
        pattern = r"[a-z]\d"
        moves_file = "book.game"
#        print("open file")
        try:
            with open(moves_file, "r") as f:
                for data in f:
                    moves = re.findall(pattern, data)
                    for i,move in enumerate(moves):
                        try:
                            self.move_count[move] = self.move_count.get(move, 0) + 1
                        except:
                            self.move_count = {}
                            self.move_count[move] = 1
                        try:
                            self.move_priority[move] = self.move_priority.get(move, 0) + len(moves)-i
                        except:
                            self.move_priority = {}
                            self.move_priority[move] = len(moves)
        except:
            print("File Error")
#        print("close file")



    def get_move(self, board, possible_moves):
        max_val = -inf
#        print(f"possible moves: {possible_moves}")
        for move in possible_moves:
            print(f"move = {move}")
            next_board = copy.deepcopy(board)
            score = self.minimax(next_board, depth=3)   # evaluate_board(board, rules, move, enemy_color)
            if (score >= max_val):
                chosen_move = move
                max_val = score
                print(f"chosen move, score = {score}")
            else:
                print(f"arbitrary move, score = {score}")
                chosen_move = random.choice(possible_moves)
#        print(f"chosen move {chosen_move}")
        return chosen_move


if (__name__ == "__main__"):
    s = Player06(Disk.LIGHT)
    s.evaluate_board()
    print(s.move_count)
    print(s.move_priority)