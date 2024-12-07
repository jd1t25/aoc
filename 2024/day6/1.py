with open(r'day6\input.txt') as file:
    input = [list(line.strip()) for line in file]

# print(input)

rotate = ['u','r','d','l']

def rot90(idx:int) -> int:
    return rotate[idx % 4]

def find_location(inp:list) -> tuple[int,int]:
    for row,string in enumerate(inp):
        if '^' in string:
            pos = string.index('^')
            # print(type(pos))
            input[row][pos] = 'o'
            return row,pos

row,col = find_location(input)
# print(row,col)
r=0
distinct = 0
while True:
    if 0 < row >= len(input)-1 or 0 < col >= len(input)-1:
        break
    if input[row][col] == '.':
        input[row][col] = 'o'
        distinct += 1
    # if input[row+1][col+1] == '#':
    #     # break
    #     r += 1

    if rot90(r) == 'u':
        if input[row-1][col] == '#':
            # print(row,col)
            r += 1
        else:
            row -= 1
    if rot90(r) == 'd':
        if input[row+1][col] == '#':
            # print(row,col)
            r += 1
        else:
            row += 1
    if rot90(r) == 'l':
        if input[row][col-1] == '#':
            # print(row,col)
            r += 1
        else:
            col -= 1
    if rot90(r) == 'r':
        if input[row][col+1] == '#':
            # print(row,col)
            r += 1
        else:
            col += 1
    
print(distinct + 2)
