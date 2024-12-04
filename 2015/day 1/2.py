with open(r'I:\Code\AOC\2015\day 1\1.txt','r') as file:
    board = [lines for lines in file]

level = 0

for idx,char in enumerate(board[0]):
    if char == '(':
        level += 1
    else:
        level -= 1
    if level == -1:
        print(idx+1)
        break