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

curr_pos1 = start
curr_pos2 = start
coor = []
coor.extend([start])

for idx,char in enumerate(board[0]):
    if idx % 2 == 0:
        next_pos = move(char)
        x,y = curr_pos1
        newx,newy = next_pos
        curr_pos1 = (x+newx,y+newy)
        if curr_pos1 not in coor:
            coor.extend([curr_pos1])
    else:
        next_pos = move(char)
        x,y = curr_pos2
        newx,newy = next_pos
        curr_pos2 = (x+newx,y+newy)
        if curr_pos2 not in coor:
            coor.extend([curr_pos2])

# print(coor)
print(len(coor))
    