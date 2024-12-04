import pandas as pd

with open(r'I:\Code\AOC\d21\test.txt') as file:
    board = [lines.rstrip() for lines in file]

data = pd.DataFrame([list(lines) for lines in board],columns=[i for i in range(max(map(len,board)))])

# print(board)

startx,starty = data.where(data == 'S').stack().index[0]
# print(startx,starty)

dir = {
    'east' : (0,1),
    'west' : (0,-1),
    'north' : (-1,0),
    'south' : (1,0)
}

next = []
temp = []
visited = []
end = 1
total = 0

def move(x,y):
    del temp[0]
    for d in dir:
        dx = int(dir[d][0])
        dy = int(dir[d][1])
        if x+dx < 0 or y+dy < 0 or x+dx > len(data) or y+dy > len(data.columns):
            end = 0
        newx = x + dx
        newy = y + dy
        if data[newx][newy] != '#':
            next.append([newx,newy])

temp.append([startx,starty])

while end:
    count = 0
    length = len(temp)
    for i in temp:
        if visited != i:
            move(*i)
        visited.append([i])
        # if end:
        #     break
        count += 1
        if count == length:
            temp = next
            next = []
            count = 0
    total += 1
print(total)