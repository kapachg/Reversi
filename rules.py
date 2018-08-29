from disk import Disk
from board import Board

class Rules:

    def __init__(self):
        pass

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
        Dictionary of mvoe as a key and the flipping directions list as value {move : [directions]}
        """
        self.x, self.y = move
        self.board = board

        self.ROWS = board[-1][0]
        self.COLS = board[-1][1]

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


    def no_moves(self, game):
        """
        Determine what to do if player has no move, pass the turn by default
        :param game: the game object
        """
        game.p1, game.p2 = game.p2, game.p1


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