import pandas as pd
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

with open(r'I:\Code\AOC\d16\test.txt') as file:
    board = [lines.rstrip('\n') for lines in file]


df = pd.DataFrame([list(lines) for lines in board],columns=[i for i in range(max(map(len,board)))])

directions = ['east','west','north','south']

marked = []
light = []
# print(board)

dir = {
    'north': (-1,0),
    'south': (1,0) ,
    'east' : (0,1) ,
    'west' : (0,-1),
}


def mirror_back(direction):
    val = directions.index(direction)
    return ['south','north','east','west'][val]

def mirror_for(direction):
    val = directions.index(direction)
    return ['north','south','west','east'][val]

def splitters_horizontal(direction,x,y):
    if direction in ['east','west']:
        return direction
    else:
        light.append(['east',x,y])
        return 'west'

def splitters_vertical(direction,x,y):
    if direction in ['north','south']:
        return direction
    else:
        light.append(['north',x,y])
        return 'south'
        # with ProcessPoolExecutor() as exe:
        #     exe.submit(move,'north',x+dir['north'][0],y+dir['north'][1])
        #     exe.submit(move,'south',x+dir['south'][0],y+dir['south'][1])

def move(direction,x,y):
    # newx = x+dir[direction][0]
    # newy = y+dir[direction][1]
    # tile = df[newx][newy]
    newx,newy=x,y
    while 0 <= x+dir[direction][0] < len(df) or 0 <= y+dir[direction][1] < len(df.columns):
        # if :
            newx = newx+dir[direction][0]
            newy = newy+dir[direction][1]
            tile = df[newx][newy]
            marked.append([newx,newy])
            if tile in contrap.keys():
                direction = contrap[tile](direction,newx,newy)
                newx = newx+dir[direction][0]
                newy = newy+dir[direction][1]
                tile = df[newx][newy]
                
        # move(direction,x+dir['direction'][0],y+dir['direction'][1])
    
        # move(direction,newx,newy)
    # move(direction,x+dir['direction'][0],y+dir['direction'][1])

    # if direction == 'east':
    #     return 'north'
    # elif direction ==    
contrap = {
    '|' : splitters_vertical  ,
    '-' : splitters_horizontal,
    '/' : mirror_for,
    '\\' : mirror_back,
}



move('east',0,0)
if len(light) != 0 :
    for i in light:
        for item in i.split(','):
            move(item[0],item[1],item[2])