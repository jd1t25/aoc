with open(r'I:\Code\AOC\d10\1.txt','r') as file:
    board = [lines.rstrip('\n') for lines in file]

# count = 0
start_pos = [(idx,i.index('S')) for idx,i in enumerate(board) if 'S' in i ][0]
# print(start_pos)

new_board = []

for i in board:
    new_board.append(list(i))

board = new_board
# print(board)

# tiles = {
#     '|': (1,0),
#     '-': (0,1),
#     'L': (0,1),
#     'J': (0,-1),
#     '7': (0,-1),
#     'F': (0,1)
# }

tiles = {
    '|': ('north','south'),
    '-': ('east','west'),
    'L': ('north','east'),
    'J': ('north','west'),
    '7': ('south','west'),
    'F': ('south','east')
}

dir = {
    'north' : (-1,0),
    'south' : (1,0),
    'east'  : (0,1),
    'west'  : (0,-1)
}


def check(start_pos):
    row,col = start_pos
    connected_pos = []
    try:
        for k,v in dir.items():
            opp_dir = swap(k)
            # if opp_dir in 
            # if board[row+dir[opp_dir][0]][col+dir[opp_dir][1]]:
            sym = board[row+v[0]][col+v[1]]
            if sym != '.' and any([row+v[0],col+v[1]]) > 0:
                if opp_dir in tiles[sym]:
                    connected_pos.append(k)
    except IndexError:
        pass

    # try:
    #     if new_board[(row-1)][col] in {'|','J'}:
    #         new_pos.append([row-1,col])
    #     if new_board[row][(col-1)] in {'-','F'}:
    #         new_pos.append([row,col-1])
    #     if new_board[row][(col+1)] in {'J','7','-'}:
    #         new_pos.append([row,col+1])
    #     if new_board[(row+1)][col] in {'|','L','J'}:
    #         new_pos.append([row+1,col])
    # except IndexError:
    #     pass
    return connected_pos

def swap(direction):
    if direction == 'north':
        direction = 'south'
    elif direction == 'south':
        direction = 'north'
    elif direction == 'east':
        direction = 'west'
    elif direction == 'west':
        direction = 'east'
    return direction

def other(direction,sym):
    direction = swap(direction)
    pos = tiles[sym][0]
    return tiles[sym][1] if pos == direction else tiles[sym][0]


next_to_start_pos = check(start_pos)
# print(next_to_start_pos)
complete = 0
for direction in next_to_start_pos:
    row,col = start_pos[0],start_pos[1]
    next_pos_x = row + dir[direction][0]
    next_pos_y = col + dir[direction][1]
    i = direction
    count = 1
    # while board[next_pos_x][next_pos_y] != '.':
    while True:
        if board[next_pos_x][next_pos_y] == '.':
            break
        next_to_next_pos = board[next_pos_x][next_pos_y]
        next_pos = other(i,next_to_next_pos)
        # print(next_pos)
        next_pos_x = next_pos_x + dir[next_pos][0]
        next_pos_y = next_pos_y + dir[next_pos][1]
        i = next_pos
        count += 1
        if (next_pos_x,next_pos_y) == start_pos:
            complete = 1
            break
    if complete:
        break

print(count // 2)

        # row,col = i[0],i[1]
        # curr_pos = board[row][col]
        # while (row,col) != start_pos:
        #     next_pos = tiles[curr_pos]
        #     curr_pos = (next_pos[0]+row,next_pos[1]+col)
        #     curr_pos = board[curr_pos[0]][curr_pos[1]]
    # break

# col = len(board)
# row = len(board[0])

# while True:


# i,j = 0,0

# start_pos = [(i,j) for i,val1 in ]



# print(col)
# print(row)

# print(board)