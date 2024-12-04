with open(r'I:\Code\AOC\2015\day 1\1.txt','r') as file:
    board = [lines for lines in file]

count = board[0].count('(') - board[0].count(')')
print(count)
