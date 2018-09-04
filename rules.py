from disk import Disk
from board import Board
import copy

class Rules:

    def __init__(self):
        self.pass_turn_when_no_moves = True

    @staticmethod
    def other_color(color):
        if (color == Disk.LIGHT):
            return Disk.DARK
        if (color == Disk.DARK):
            return Disk.LIGHT

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

    def validate_move(self, board, move, current_disk):
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
        self.other_disk = self.other_color(current_disk)


   #     print(self.x, self.y, self.ROWS, self.COLS, self.current_disk, self.other_disk)

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

    def possible_moves(self, board, color):
        """
        Returns a dictionary of current player possible moves as keys and the directions of the flipping disks as values
        """

        moves = {}
        for x in range(len(board)):
            for y in range(len(board[0])):
                move = self.validate_move(board, (x, y), color)
                if (move):
                    moves.update(move)
        return moves

    def update_board(self, board, move, directions, color):
        """
        Returns an updated board after get_move from the user
        """

#        new_board = copy.deepcopy(board)
        #print(new_board)
        for direction in directions:
            i, j = direction
            x, y = move
            board[x][y] = color
            x += i
            y += j
            while self.check_board_limits(x, y) and board[x][y] == self.other_color(color):
                board[x][y] = color
                x += i
                y += j

    #    return board

    def winner(self, board):
        """ Returns the winner of the game

        :param board: current board object

        Returns:
        Disk.enum with maximum disks or "draw" if number of disks if equal
        """

        light = dark = 0
        for line in board:
            light += line.count(Disk.LIGHT)
            dark += line.count(Disk.DARK)
        print(f"Light disks: {light} Dark disks: {dark}")
        if (light > dark):
            return Disk.LIGHT
        elif (dark > light):
            return Disk.DARK
        else:
            return "draw"

    @staticmethod
    def coordinates_to_matrix(col, row, transpose=False):
        """

        :param col: column letter (single str)
        :param row: row number (converted to int)
        :param transpose: whether to transpose columns with rows, boolean
        :return:
        (int, int) a tuple of x,y coordinates [0..SIZE] (which is opposite from the human format)
        """
        x = int(row)-1
        y = ord(col)-ord('a')
        if (transpose):
            x, y = y, x
        return x, y

    @staticmethod
    def coordinates_to_user(x, y, transpose=False):
        """

        :param x: int index
        :param y: int index
        :param transpose: whether to transpose columns with rows, boolean
        :return:
        a tuple of two single character str in the format of col, row (which is opposite from the format of the matrix)
        """
        col = chr(y+ord('a'))
        row = x+1
        if (transpose):
            col, row = row, col
        return col + str(row)


if (__name__ == "__main__"):
    r = Rules()
    b = Board()

    disk = r.coordinates_to_user(4, 7)
    print(disk, len(disk), type(disk))

    for x in range(8):
        for y in range(8):
            if r.validate_move(b.current_state(),(x,y), Disk.DARK):
               # pass
         #       print(r.validate_move(b.current_state(), (x, y)))
                print(x,y)

    #v = r.validate_move(b.current_state(),(2,2))
    #print(v)