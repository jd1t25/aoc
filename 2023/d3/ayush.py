with open(r'1.txt','r') as f:
    board = [lines.rstrip('\n') for lines in f]

print(board)
# arr = [i.split() for i in board]
# temp = [i for j in arr for i in j]
# # arr = [j for i in board for j in i.split() ]

# print(arr)
# print(temp)

arrs=[]

for row in board:
    arr = []
    for column in row:
        arr.append(column)
    arrs.append(arr)
len_row = len(arrs)
len_col = len(arr)

# print(arrs)
    

def dfs(boards,i,j):
    if i < 0 or j < 0:
        return False
    if i >= len_row or j >= len_col:
        return False

    if boards[i][j] == '.':
        return False
    
    if not boards[i][j].isdigit():
        return True
    boards[i][j] = '.'
    #print("i : {} , j : {}".format(i,j))
    return dfs(boards,i,j+1) or \
        dfs(boards,i+1,j+1) or \
        dfs(boards,i+1,j) or \
        dfs(boards,i-1,j+1) or \
        dfs(boards,i,j-1) or \
        dfs(boards,i-1,j-1) or \
        dfs(boards,i-1,j) or \
        dfs(boards,i+1,j-1)
    
sum = 0
for i in range(0,len_row):
    for j in range(0,len_col):
        if arrs[i][j].isdigit():
            number = ""
            for k in range(j,len_col):
                if not arrs[i][k].isdigit():
                    break
                number += arrs[i][k]

            if dfs(arrs,i,j):
                
                sum += int(number)

print(sum)