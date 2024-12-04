with open(r'I:\Code\AOC\2015\day 2\test.txt','r') as file:
    board = [lines.strip() for lines in file]

# print(board)

def surface_area(measure):
    l,w,h = int(measure[0]),int(measure[1]),int(measure[2])
    surface = (2*l*w)+(2*w*h)+(2*l*h)
    extra = sorted([l,w,h])[0]*sorted([l,w,h])[1]
    return surface + extra


total = 0

for lines in board:
    total += surface_area(lines.split('x'))

print(total)