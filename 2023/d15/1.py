with open(r'I:\Code\AOC\d15\1.txt') as file:
    board = [lines.rstrip('\n') for lines in file]

board = board[0].split(',')

total = 0
count = []

# board = ['HASH']

for string in board:
    hash = list(string)
    for char in hash:
        total += ord(char)
        total *= 17
        total %= 256
    count.append(total)
    total = 0
        # total += ((total)*17)%256

print(sum(count))