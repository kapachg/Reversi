from disk import Disk

class Board():
    """ This class stores the board itself as a 2D matrix.
    Contains the following methods:
    current_state(): present the current board and its size
    place_disk: place a disk in the board
    coordinates_to_matrix(col, row, transpose=False): A static method to convert human coordinates (a..h,1..8) to matrix [8][8]
    coordinates_to_user(x, y, transpose=False): A static method to convert matrix coordinates[8][8] to human coordinates (a..h,1..8)
    count_disks(): count each player's disks
    """

    def __init__(self, rows=8, cols=8):
        """
        Initializing the matrix with empty spaces and 4 disks in the middle

        :param
        rows - number of rows (int)
        cols - number of columns (int)
        """
        self.rows = rows
        self.cols = cols
        self.matrix = [[Disk.NONE for x in range(rows)] for y in range(cols)]
        init_array = (('d','4',Disk.LIGHT), ('e','5',Disk.LIGHT), ('d','5',Disk.DARK), ('e','4',Disk.DARK))
     #   init_array = (('a', '2', Disk.LIGHT), ('b', '5', Disk.LIGHT), ('d', '5', Disk.DARK), ('e', '4', Disk.DARK))
        for item in init_array:
            self.place_disk(*self.coordinates_to_matrix(item[0], item[1]), item[2])

    def current_state(self):
        """
        Return the matrix of Disks as a 2D tuple
        last item [-1] is the size of the board as a tuple (int, int)
        """
        return self.matrix
        #return tuple([tuple(i) for i in self.matrix]) # + [(self.rows, self.cols)])

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
    for x in range(rows):
        for y in range(cols):
#            print(f"({x},{y}) {b.current_state()[x][y]}",end=' ')
            print(f"({b.coordinates_to_user(x,y)}) {b.current_state()[x][y]}",end=' ')
        print()

    print(len(b.matrix), len(b.matrix[0]))