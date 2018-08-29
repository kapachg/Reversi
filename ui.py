from disk import Disk
from board import Board
from sys import exit

show_disk = {
    Disk.NONE : ' ',
    Disk.DARK : 'x',
    Disk.LIGHT : '0'
}

class UI:
    """ This class responsible for interaction with the user via the console"""
    def __init__(self):
        pass

    def print_board(self, board):
        """
        Print the board to the screen
        :param board: gets the board current_state (ie, including the board size)
        :return: output to the screen. No return value.
        """
        COLS = len(board[0])
        ROWS = len(board)

        l = [' '+chr(i)+' |' for i in range(ord('a'), ord('a')+COLS)]
        print(' '*2 + '|' + ''.join(l))
        print('-'*2 + '+' + ('-' * 3 + '+')*COLS)
        for row in range(ROWS):
            print(f" {row+1}|",end='')
            for item in board[row]:
                print(f" {show_disk[item]} |",end='')
            print()
            print('-' * 2 + '+' + ('-' * 3 + '+') * COLS)
        print()

    def show_available_moves(self, possible_moves):
        """ Print to the screen the list of possible moves as human coordinates

        :param possible_moves: a list of tuples(int, int)
        """
        print("Available moves: ")
        for coordinates in possible_moves:
            print(Board.coordinates_to_user(*coordinates), end=' ')
        print()

    def user_move(self, color, possible_moves):
        """ Ask the user for its next move

        :param color: the current player's color (Disk)
        :param possible_moves: a list of tuples(int, int)
        :return:
        a tuple of matrix coordinates (int, int)
        """
        print(f"Player {show_disk[color]}: ")
        self.show_available_moves(possible_moves)
        move = input("Please enter your chosen move: ")
        while (len(move) != 2 or Board.coordinates_to_matrix(move[0], move[1]) not in possible_moves):
            move = input("Please enter your chosen move: ")
            if move == "exit":
                exit()

        #print(move)
        print()
        return Board.coordinates_to_matrix(move[0], move[1])



if (__name__ == "__main__"):
    UI = UI()
    b = Board()
    UI.print_board(b.current_state())