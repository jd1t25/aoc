# temp = [i+1 for i in range(9)]

with open(r'I:\Code\AOC\d11\1.txt','r') as file:
    board = [line.rstrip() for line in file]

galaxy = '#'
row_expands,col_expands = [],[]
first_time = 1

for idx,i in enumerate(board):
    if galaxy not in i:
        row_expands.append(idx)
        if first_time:
            space = i
            first_time = 0
    if idx < len(board[0]):
        col = [j[idx] for j in board]
        if galaxy not in col:
            col_expands.append(idx)

# print(col_expands)
# print(row_expands)

for idx,i in enumerate(row_expands):
    board.insert(i+1,space)

col_count = 0
for i in col_expands:
    for jdx,j in enumerate(board):
        j = j[:i+col_count]+'.'+j[i+col_count:]
        board[jdx] = j
    col_count += 1
    # print(string)

# print(len(board))
# print(len(board[0]))

loc = []

for idx,i in enumerate(board):
    if '#' in i:
        j = 0
        while j < len(i):
            if i[j] == '#':
                loc.append((idx,j))
            j += 1

i = 0
total = 0
# temp = []
pairs = [(i,j) for i in range(len(loc)) for j in range(i+1,len(loc))]

while i < len(pairs):
    x,y = pairs[i]
    x1,y1=loc[x][0],loc[x][1]
    x2,y2=loc[y][0],loc[y][1]
    steps = abs(int(x2)-int(x1))+abs(int(y2)-int(y1))
    # temp.append((x+1,y+1,x2,x1,y2,y1,steps))
    total += steps
    i += 1

print(total)

# open('output.txt','w').close()

# with open('output.txt','w+') as file:
#     for i in board:
#         file.write(i+'\n')

# file.close()

# temp2 = abs(temp[0][0]-temp[1][0])+abs(temp[0][1]-temp[1][1])
# print(temp2)

# temp = []

# i = 1
# j = 1

# while i in range(10):
#     for j in range(i+1,10):
#         temp.append([i,j])
#     i += 1

# print(len(temp))