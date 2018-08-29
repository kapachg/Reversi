
for line in board[max(0 , x -1): x +2]:
    is_valid = other_disk in line[max(0 , y -1): y +2]

return is_valid

# Is the other disk bounded?

if not is_valid:
    return False  # is_valid

x, y = move
bounds = []
b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = None

for j in range(COLS):
    if ( y +j < COLS and board[x][ y +j] == other_disk):
        b1 = (x, y+ j)
    if (y - j >= 0 and board[x][y - j] == other_disk):
        b2 = (x, y - j)
for i in range(ROWS):
    if (x + i < ROWS and board[x + i][y] == other_disk):
        b3 = (x + i, y)
    if (x - i >= 0 and board[x - i][y] == other_disk):
        b4 = (x - i, y)
for i, j in zip(range(ROWS, COLS)):
    if (y + j < COLS and x + i < ROWS and board[x + i][y + j] == other_disk):
        b5 = (x + i, y + j)
    if (y - j >= 0 and x - i >= 0 and board[x - i][y - j] == other_disk):
        b6 = (x - i, y - j)
    if (x + i < ROWS and y - j >= 0 and board[x + i][y - j] == other_disk):
        b7 = (x + i, y - j)
    if (x - i >= 0 and y + j < COLS and board[x - i][y + j] == other_disk):
        b8 = (x - i, y + j)

bounds = [b for b in (b1, b2, b3, b4, b5, b6, b7, b8) if b]
return bounds

# bounds = []
# first diagonal
# d1 = x   # delta of one direction
#   for i in range(x):
#      if (current_disk == board[i][y-x+i]):
#         bound = (i,y-x+i)
#        break

# second diagonal
# for i in range(x+1,COLS,-1):
#    if (current_disk == board[i][])


d2 = 8 - y  # delta of other direciton

line = board[x]

if current_disk in line:
    return True

for line in board[:-1]:
    if current_disk == line[y]:
        return True

return is_valid











eat_enemy = {}
for i in range(-1, 2):  # Direction of 1st axis
    for j in range(-1, 2):  # Direction of 2nd axis
        if self.check_board_limits(self.x + i, self.y + j) and board[self.x + i][self.y + j] == self.other_disk:
            tmp = self.eat_in_direction(self.x, self.y, i, j)
            if (tmp):
                eat_enemy[(self.x, self.y)] = eat_enemy.get((self.x, self.y), []) + [tmp]
return eat_enemy