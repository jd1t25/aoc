import pandas as pd

with open(r'I:\Code\AOC\d14\test.txt', 'r') as file:
    board = [lines.rstrip('\n') for lines in file]


df = pd.DataFrame([list(line) for line in board],columns=[f'{i}' for i in range(max(map(len,board)))])

def pos(mirrors):
    i = 0
    mirrors = list(mirrors)
    while i < len(mirrors):
        j = i
        count = 0
        while mirrors[i] != '#':
            if mirrors[i] == 'O':
                count += 1
                mirrors[i] = '.'
            i += 1
            if i >= len(mirrors):
                break
        for k in range(j,j+count):
            mirrors[k] = 'O'
        i += 1
    return mirrors


def neg(mirrors):
    i = len(mirrors)-1
    mirrors = list(mirrors)
    while i > 0:
        j = i
        count = 0
        while mirrors[i] != '#':
            if mirrors[i] == 'O':
                count += 1
                mirrors[i] = '.'
            i -= 1
            if i < 0:
                break
        if count != 0:
            for k in range(j,j-count,-1):
                mirrors[k] = 'O'
        i -= 1
    return mirrors

# def east(mirrors):
#     i = 0
#     # mirrors = list(mirrors)
#     while i < len(mirrors):
#         j = i
#         count = 0
#         while mirrors[i] != '#':
#             if mirrors[i] == 'O':
#                 count += 1
#                 mirrors[i] = '.'
#             i += 1
#             if i >= len(mirrors):
#                 break
#         for k in range(j,j+count):
#             mirrors[k] = 'O'
#         i += 1
#     return mirrors
for i in range(1000000000):
    for k in range(len(df)):
        df.iloc[:,k] = pos(list(df.iloc[:,k]))
        # print(df.iloc[k,:])
    # print(df)
    for k in range(len(df)):
        df.iloc[k] = pos(list(df.iloc[k]))
    # print(df)
    for k in range(len(df)):
        df.iloc[:,k] = neg(list(df.iloc[:,k]))
    # print(df)
    for k in range(len(df)):
        df.iloc[k] = neg(list(df.iloc[k]))
    # print(df.iloc[k,:])
# print(df)
# for i in range(len(df.columns)):
# df.iloc[:,0] = north(df.iloc[:,0])
# print(df.iloc[:,0])
# print(df)

total =  0
rows = len(df)

for i in range(len(df)):
    count = list(df.iloc[i]).count('O')
    total += (rows-i)*count

print(total)
# print(list(df.iloc[:,0]))