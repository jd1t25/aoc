with open(r'I:\Code\AOC\2015\day 3\1.txt','r') as file:
    board = [lines.strip() for lines in file]

char_dir = {
    '>' : 'east',
    '^' : 'north',
    'v' : 'south',
    '<' : 'west'
}

pos_dir = {
    'east' : (0,1),
    'west' : (0,-1),
    'north': (-1,0),
    'south': (1,0)
}

start = (0,0)

def move(pos):
    return pos_dir[char_dir[pos]]

curr_pos = start
coor = []
coor.extend([start])

for char in board[0]:
    next_pos = move(char)
    x,y = curr_pos
    newx,newy = next_pos
    curr_pos = (x+newx,y+newy)
    if curr_pos not in coor:
        coor.extend([curr_pos])

print(coor)
print(len(coor))
    