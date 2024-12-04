import pandas as pd

with open(r'I:\Code\AOC\d13\1.txt', 'r') as file:
    board = file.read()

temp = board.split("\n\n")

print(temp)
#     board = [lines.rstrip() for lines in file]

# board = [[*line] for line in board]

# # print(board)

# with open('output.txt','w+') as output:
#     for i in board:
#         for j in i:
#             output.write(str(j) + ' ')
#         output.write('\n')
#     # count = file.readline()

# output.close()

# with open(r'I:\Code\AOC\d13\1.txt', 'r') as file:
#     board = file.readlines()
    
# for x in board:
#     print(list(x.rstrip('\n'))[1])

# print([x.split() for x in board])
    
# df = pd.read_csv(r"I:\Code\AOC\d13\1.txt", delimiter=" ",header=None)

# print(df)