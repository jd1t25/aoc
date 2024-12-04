import pandas as pd
with open(r'I:\Code\AOC\d11\test.txt','r') as file:
    board = [line.rstrip() for line in file]

data = pd.DataFrame([list(lines) for lines in board],columns=[i for i in range(len(board[0]))])

# print(data)

def insert_row():
    nrow = []
    for i in range(len(data)):
        if not data[i].str.contains('#').any():
            nrow.append(i)
    print(nrow)

    for idx,i in enumerate(nrow):
        data.insert(i,len(data)+idx,'.')
    
    print(data)
    # data2 = pd.DataFrame(data,columns=[i for i in range(len(data))])
    # print(data2)


insert_row()
print(data[10][0])