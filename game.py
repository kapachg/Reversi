from board import Board
from ui import UI
from disk import Disk
from interactive_player import InteractivePlayer
from random_player import RandomPlayer
#from simple_player import SimplePlayer
from rules import Rules


class Game:
    def __init__(self):
        """
        Initializing the game objects.
        p1 is always the current player
        p2 is always the other player
        """

        self.board = Board()
        #self.p1 = SimplePlayer(Disk.DARK)
        #self.p1 = InteractivePlayer(Disk.DARK)
        #self.p2 = InteractivePlayer(Disk.LIGHT)
        self.p1 = RandomPlayer(Disk.DARK)
        self.p2 = RandomPlayer(Disk.LIGHT)
        self.rules = Rules()
        self.ui = UI()



    def update_board(self):
        """
        Updates the board after get_move from the user
        """

        for direction in self.moves[self.chosen_move]:
            i, j = direction
            #print(i,j)
            x, y = self.chosen_move
            self.board.place_disk(x, y, self.p1.color)
            x += i
            y += j
            while self.rules.check_board_limits(x, y) and self.board.current_state()[x][y] == self.p2.color:
                #print(x,y,i,j)
                self.board.place_disk(x, y, self.p1.color)
                x += i
                y += j

    def quit_game(self):
        """
        A function for quitting the game, returns the type of the winner, unless it's a draw and then "draw" is returned
        """

        winner = self.rules.winner(self.board)
        if self.p1.color == winner:
            return type(self.p1)
        elif self.p2.color == winner:
            return type(self.p2)
        else:
            return "draw"
        #print(winner)
        #return winner

    def start_game(self):
        """
        Starts a new game
        """

        self.ui.print_board(self.board.current_state())

        while (True):
            self.moves = self.rules.possible_moves(self.board.current_state(), self.p1.color, self.p2.color)

            # If there are no available moves, pass the turn
            if not self.moves and self.rules.pass_turn_when_no_moves:
                game.p1, game.p2 = game.p2, game.p1

                # If other player also don't have available moves, quit the game
                if not self.moves:
                    return self.quit_game()

            self.chosen_move = self.p1.get_move(self.board.current_state(), list(self.moves.keys()))

            if not isinstance(self.p1, InteractivePlayer):
                print(f"Player {self.p1} {type(self.p1)}:")
                self.ui.show_available_moves(list(self.moves.keys()))
                print (Board.coordinates_to_user(*self.chosen_move))

            # Apply and display chosen move
            self.update_board()
            self.ui.print_board(self.board.current_state())
           # print(f"Light disk: {self.board.count_disks()[Disk.LIGHT]} Dark disk: {self.board.count_disks()[Disk.DARK]}")

            # Switch player
            self.p1, self.p2 = self.p2, self.p1

          #  input(f"Next turn of {self.p1}")






if (__name__ == "__main__"):
    player = {}
    for i in range(10):
        game = Game()
        winner = game.start_game()
        player[winner] = player.get(winner, 0) + 1
    print(player)