with open(r'I:\Code\AOC\2015\day 5\1.txt','r') as file:
    board = [lines.strip() for lines in file]

# not_allowed = ['ab','cd','pq','xy']
# vowels = ['a','e','i','o','u']

# board = board[0]
# print(board)
accepted = 0


def check1(line):
    for i in range(len(line)):
        if i < len(line)-2:
            # temp1 = line[i]
            # temp2 = line[i+2]
            if line[i] == line[i+2]:
                return True
    return False
                
def check2(line):
    for i in range(len(line)):
        for j in range(i+2,len(line)-1):
            # temp1 = line[i]+line[i+1]
            # temp2 = line[j]+line[j+1]
            if line[i]+line[i+1] == line[j]+line[j+1]:
                return True
    return False


for line in board:
    # double = False
    # twice = False
    end1 = check1(line)
    end2 = check2(line)
    if end1 and end2:
        accepted += 1


# for line in board:
#     # double = False
#     # twice = False
# line = board[0]
# end1 = check1(line)
# end2 = check2(line) 
print(accepted)