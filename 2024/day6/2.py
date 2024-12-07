with open(r'day6\test.txt') as file:
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

def out(inp:list):
    file1 = open(r'./out.txt',"w")
    for line in inp:
        file1.writelines("{}\n",format(line))
    file1.close()

row,col = find_location(input)
# print(row,col)
r=0
count = 0
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
    if input[row][col] == 'o':
        count+= 1

    if rot90(r) == 'u':
        if input[row-1][col] == '#':
            # print(row,col)
            r += 1
        else:
            row -= 1
    if rot90(r) == 'd':
        if input[row+1][col] == '#':
            # print(row,col)
            count += 1
            r += 1
        else:
            row += 1
    if rot90(r) == 'l':
        if input[row][col-1] == '#':
            # print(row,col)
            count += 1
            r += 1
        else:
            col -= 1
    if rot90(r) == 'r':
        if input[row][col+1] == '#':
            # print(row,col)
            count += 1
            r += 1
        else:
            col += 1
    out(input)
    
print(distinct + 2)
print(count)
