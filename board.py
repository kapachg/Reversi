from disk import Disk

class Board():
    """ This class stores the board itself as a 2D matrix.
    Contains the following methods:
    current_state(): present the current board and its size
    place_disk: place a disk in the board
    coordinates_to_matrix(col, row, transpose=False): A static method to convert human coordinates (a..h,1..8) to matrix [8][8]
    coordinates_to_user(x, y, transpose=False): A static method to convert matrix coordinates[8][8] to human coordinates (a..h,1..8)
    count_disks(): count each player's disks

    the dimensions of the board are stores in the following constants:
    NUMBER_OF_COLS
    NUMBER_OF_ROWS
    """
    NUMBER_OF_COLS = 8
    NUMBER_OF_ROWS = 8
    SIZE = (NUMBER_OF_COLS, NUMBER_OF_ROWS)

    def __init__(self):
        """
        Initializing the matrix with empty spaces and 4 disks in the middle
        """
        self.matrix = [[Disk.NONE for x in range(Board.SIZE[0])] for y in range(Board.SIZE[1])]
        init_array = (('d','4',Disk.LIGHT), ('e','5',Disk.LIGHT), ('d','5',Disk.DARK), ('e','4',Disk.DARK))
        for item in init_array:
            self.place_disk(*self.coordinates_to_matrix(item[0], item[1]), item[2])

    def current_state(self):
        """
        Return the matrix of Disks as a 2D tuple
        last item [-1] is the size of the board as a tuple (int, int)
        """
        return tuple([tuple(i) for i in self.matrix] + [Board.SIZE])

    def place_disk(self, x, y, disk):
        self.matrix[x][y] = disk

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

    def count_disks(self):
        """
        Returns a dictionary of each color and the number of its disks on the board {Disk,int}
        """
        light = dark = 0
        for line in self.matrix:
            light += line.count(Disk.LIGHT)
            dark += line.count(Disk.DARK)
        return {Disk.DARK : dark, Disk.LIGHT : light}

if (__name__ == "__main__"):
    b = Board()
    #print(b.matrix)
   # b.current_state()[0] = "ds"
#    print(b.current_state())
#    print(b.current_state()[0])
#    print(b.current_state()[-1][0])
    cols = b.current_state()[-1][0]
    rows = b.current_state()[-1][1]

    print(b.current_state())

    print("(x,y)")
    for x in range(cols):
        for y in range(rows):
#            print(f"({x},{y}) {b.current_state()[x][y]}",end=' ')
            print(f"({b.coordinates_to_user(x,y)}) {b.current_state()[x][y]}",end=' ')
        print()