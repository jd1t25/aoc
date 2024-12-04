import re

with open(r'I:\Code\AOC\d15\1.txt') as file:
    board = [lines.rstrip('\n') for lines in file]

board = board[0].split(',')


count = {}

for string in board:
    total,equal = 0,0
    if '=' in string:
        equal = 1
    else:
        minus = 1
    string = re.split('=|-',string)
    hash = list(string[0])
    focal_length = string[1]
    for char in hash:
        total += ord(char)
        total *= 17
        total %= 256
    if equal:
        # count.update(total = [string[0],string[1]])
        if str(total) in count.keys():
            if string[0] in (item for sublist in count[str(total)] for item in sublist):
                for i in count[str(total)]:
                    if i[0] == string[0]:
                        i[1] = string[1]
                        break
            else:
                count[str(total)].append([string[0],string[1]])
        else:
            count[str(total)] = [[string[0],string[1]]]
    else:
        if str(total) in count.keys():
            # if string[0] in count[str(total)]:
            if string[0] in (item for sublist in count[str(total)] for item in sublist):
                for idx,item in enumerate(count[str(total)]):
                        if item[0] == string[0]:
                            count[str(total)].pop(idx)

    # total = 0
    #     total += ((total)*17)%256

# print(count)

power = 0

for k,v in count.items():
    slot = 1
    for i in v:
        power += slot*int(i[1])*(int(k)+1)
        slot += 1
    
print(power)