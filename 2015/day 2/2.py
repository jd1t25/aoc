with open(r'I:\Code\AOC\2015\day 2\1.txt','r') as file:
    board = [lines.strip() for lines in file]

# print(board)

def surface_area(measure):
    l,w,h = int(measure[0]),int(measure[1]),int(measure[2])
    perimeter = sorted([l,w,h])[0]*2 + sorted([l,w,h])[1]*2
    volume = l*w*h
    # extra = sorted([l,w,h])[0]*sorted([l,w,h])[1]
    return perimeter + volume


total = 0

for lines in board:
    total += surface_area(lines.split('x'))

print(total)