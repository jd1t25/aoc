with open(r"I:\Code\AOC\d10\test4.txt",'r') as file:
    board = [list(lines.rstrip()) for lines in file]


# print(len(board[0]))
sym = ['S','|','F','-','J','7','L']



# for idx,i in enumerate(board):
#     f,b = 0,-1
#     j = ""
#     k = ""
#     while f < len(i) and i[f] not in sym:
#         i[f] = 'O'
#         f += 1
#         # j += 'O'
#         # f += 1
#     if f != len(i):
#         while b < len(i) and i[b] not in sym:
#             # k += 'O'
#             i[b] = 'O'
#             b -= 1
    
    # board[idx] = j + board[idx][f+idx-1:b+1] + k
    # print(len(board[0]))

for i in range(len(board[0])):
    col = [j[i] for j in board]
    f,b = 0,-1
    # if len(set(col)) != 1:
    while f < len(col):
        if col[f] in sym:
            break
        elif col[f] != 'O':
            col[f] = 'O'
        f += 1
    if f != len(col):
        while abs(b)+1 < len(col):
            if col[b] in sym:
                break
            elif col[b] != 'O':
                col[b] = 'O'
            b -= 1
    for k in range(len(board)):
        board[k][i] = col[k]

for i in board:
    not_loop = [idx for idx,char in enumerate(i) if char == 'O']
    if len(not_loop) not in [0,len(i)]:
        for index in not_loop:
            f,b = 1,-1
            while index+f < len(i):
                if i[index+f] == 'O' or i[index+f] in sym:
                    break
                else:
                    i[index+f] = 'O'
                f += 1
            while index-b > 0:
                if i[index+b] == 'O' or i[index+b] in sym:
                    break
                else:
                    i[index+b] = 'O'
                b -= 1


# print(board)
board = [''.join(f) for f in board]

counts = [i.count('.') for i in board]
print(counts)
print(sum(counts))
# for line in board:
#     if len(set(line)) != 1:
#         not_loop = [idx for idx,i in enumerate(line) if i == 'O']
#         new_line = ""
#         for index in not_loop:
#             f,b = 0,-1
#             forward,backward = "",""
#             while index+f < len(line):
#                 if line[index+f] in sym:
#                     break
#             forward += line[index+f]
#             f += 1
#             while index-b < len(line):
#                 if line[index-b] in sym:
#                     break
#             backward += line[index-b]
            


# for i in range(len(board)):
    
# print(board)

# print(col)
with open('gfg.txt', 'w+') as f:
     
    # write elements of list
    for items in board:
        f.write('%s\n' %items)
f.close()
# print(temp)