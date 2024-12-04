import pandas as pd

with open(r'I:\Code\AOC\d14\1.txt', 'r') as file:
    board = [lines.rstrip('\n') for lines in file]


df = pd.DataFrame([list(line) for line in board],columns=[f'{i}' for i in range(max(map(len,board)))])


def convert(mirrors):
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


for i in range(len(df.columns)):
    df.iloc[:,i] = convert(df.iloc[:,i])

# print(df)

total =  0
rows = len(df)

for i in range(len(df)):
    count = list(df.iloc[i]).count('O')
    total += (rows-i)*count

print(total)
# print(list(df.iloc[:,0]))