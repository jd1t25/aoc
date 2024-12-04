import hashlib

with open(r'I:\Code\AOC\2015\day 4\1.txt','r') as file:
    main = file.readline()


# print(board)
i = 0
board = main

while True:
    board += str(i)
    result = hashlib.md5(board.encode())
    result = result.hexdigest()
    if result[:6] == '000000':
        break
    board = main
    i += 1
    # print(result)

print(i)