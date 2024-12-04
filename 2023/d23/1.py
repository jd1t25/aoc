import pandas as pd

with open(r'I:\Code\AOC\d23\1.txt', 'r') as file:
    board = [lines.strip() for lines in file]

wallx,wally = [],[]
# wallx = pd.DataFrame()

for idx,pos in enumerate(board):
    split = pos.split('~')
    x1,y1,z1=split[0].split(',')
    x2,y2,z2=split[1].split(',')
    tempx=[]
    for i in range(max(int(x1),int(x2))):
        tempx.append(idx)
    wallx.insert(idx,tempx)
    wallx.insert(idx,[idx,x2])
    # wally.insert(idx,[idx,y1])
    # wally.insert(idx,[idx,y2])
wallx[0][0] = 0
print(wallx)
# print(wally)