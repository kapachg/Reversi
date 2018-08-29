from disk import Disk
from board import Board

class Rules:

    def __init__(self):
        self.pass_turn_when_no_moves = True

    def check_board_limits(self, x, y):
        """
        :param x: int
        :param y: int

        :return:
        bool, whether x,y within matrix boundaries
        """

        return (x >= 0) and (x < self.ROWS) and (y >= 0) and (y < self.COLS)

    def eat_in_direction(self, x1, y1, i, j):
        """
        Checks whether the direction will result in disk flipping

        :param x1: int (matrix-coordinate)
        :param y1: int (matrix-coordinate)
        :param i: int (-1..1)
        :param j: int (-1..1)
        :return:
        False if direction will not flip disks
        If direction flip disks, then the result is a tuple of two int (-1..1,-1..1) which indicates the direction
        """
        while self.check_board_limits(x1, y1):
            if self.board[x1][y1] == Disk.NONE:
                return False
            if self.board[x1][y1] == self.current_disk:
                return (i,j)
            x1 += i
            y1 += j
        return False

    def validate_move(self, board, move, current_disk, other_disk):
        """ Check if a move is valid

        :param board: current board state (not object). Return the matrix of Disks as a 2D tuple,
                    last item [-1] is the size of the board as a tuple (int, int)
        :param move: a tuple of x,y (int, int) coordinates
        :param current_disk: Current player's color (Disk Enum)
        :param other_disk: Other player's color (Disk Enum)
        :return:
        False if invalid
        Dictionary of move as a key and the flipping directions list as value {move : [directions]}
        """
        self.x, self.y = move
        self.board = board

        self.ROWS = len(board) #[-1][0]
        self.COLS = len(board[0]) #[-1][1]

        self.current_disk = current_disk
        self.other_disk = other_disk

        # Is the position occupied?
        if (self.board[self.x][self.y] != Disk.NONE):
            return False

        # Is the new position adjust to other player disk? If yes - will it flip it?
        # Return the correct direction(s)

        eat_enemy = {}
        for i in range(-1,2):                      # Direction of 1st axis
            for j in range(-1,2):                   # Direction of 2nd axis
                if self.check_board_limits(self.x+i,self.y+j) and self.board[self.x+i][self.y+j] == self.other_disk:
                    tmp = self.eat_in_direction(self.x+i, self.y+j, i, j)
                    if (tmp):
                        eat_enemy[(self.x,self.y)] = eat_enemy.get((self.x,self.y), []) + [tmp]
        return eat_enemy

    def possible_moves(self, board, p1_color, p2_color):
        """
        Returns a dictionary of current player possible moves as keys and the directions of the flipping disks as values
        """

        moves = {}
        for x in range(len(board)):
            for y in range(len(board[0])):
                move = self.validate_move(board, (x, y), p1_color, p2_color)
                if (move):
                    moves.update(move)
        return moves

    def update_board(self, board, move):
        """
        Updates the board after get_move from the user
        """

        for direction in self.moves[self.chosen_move]:
            i, j = direction
            x, y = move
            self.board.place_disk(x, y, self.p1.color)
            x += i
            y += j
            while self.rules.check_board_limits(x, y) and self.board.current_state()[x][y] == self.p2.color:
                #print(x,y,i,j)
                self.board.place_disk(x, y, self.p1.color)
                x += i
                y += j

    def winner(self, board):
        """ Returns the winner of the game

        :param board: current board object

        Returns:
        Disk.enum with maximum disks or "draw" if number of disks if equal
        """
        light = board.count_disks()[Disk.LIGHT]
        dark = board.count_disks()[Disk.DARK]
        print(f"Light disks: {light} Dark disks: {dark}")
        if (light > dark):
            return Disk.LIGHT
        elif (dark > light):
            return Disk.DARK
        else:
            return "draw"



if (__name__ == "__main__"):
    r = Rules()
    b = Board()

    for x in range(8):
        for y in range(8):
            if r.validate_move(b.current_state(),(x,y)):
               # pass
         #       print(r.validate_move(b.current_state(), (x, y)))
                print(x,y)

    #v = r.validate_move(b.current_state(),(2,2))
    #print(v)