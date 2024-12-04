with open(r'I:\Code\AOC\d13\1.txt') as file:
    board = file.read()

board = board.split('\n\n')
    # board = [lines.rstrip('\n') for lines in file]

# print(board)
# frame = []

def check(frame):
    row = 0
    next_row = row+1
    row_count = 0
    end = 0
    row_mirror = 1
    first = 1
    while next_row < len(frame) and row >= 0:
        if frame[row] == frame[next_row]:
            if first:
                row_mirror = row+1
                first = 0
            row_count += 1
            row -= 1
            next_row += 1
            end = 1
            
        else:
            if end:
                break
            row += 1
            next_row = row+1
    
    # row_patterns = [i.count('#') for i in frame]

    col_length = [k[:1] for k in frame]

    # print(row_patterns,col_count)
    
    column = []
    s = ""

    for k in range(len(frame[0])):
        for j in range(len(col_length)):
            s += (list(frame[j])[k])
        column.append(s)
        s= ""

    col = 0
    next_col = col+1
    col_count = 0
    end = 0
    first = 1
    col_mirror = 0
    while next_col < len(column)-1 and col >= 0:
        if column[col] == column[next_col]:
            if first:
                col_mirror = col
                first = 0
            col_count += 1
            col -= 1
            next_col += 1
            end = 1
            
        else:
            if end:
                break
            col += 1
            next_col = col+1

    return (row_count,row_mirror,col_count,col_mirror)

total = 0

# for idx,i in enumerate(board):
#     frame.append(i)
    # if i == '':
    #     rc,rm,cc,cm = check(frame)
    #     if rc>cc:
    #         total += (rm+1)*100
    #     else:
    #         total += cm+1
    # print(i)

for idx,i in enumerate(board):
    frame = i.split('\n')
    rc,rm,cc,cm = check(frame)
    if rc>cc:
        total += rm*100
    else:
        total += cm+1
    # print(frame)

print(total)
