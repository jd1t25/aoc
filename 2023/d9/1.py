with open(r'I:\Code\AOC\d9\1.txt', 'r') as file:
    board = [line.rstrip('\n') for line in file]

# temp = board[0].split()
# print(temp[::-1][0:2])

extrapolate = []
counts = []



for line in board:
    line = line.split()
    diff = []
    diff.extend([line])
    count = 1
    while True:
        next_diff = []
        for i in range(len(diff[-1])-1):
            next_diff.append(int(line[i])-int(line[i+1]))
        line = next_diff
        diff.extend([line])
        count += 1
        if len(set(line)) == 1:
            break
    new_value = 0
    for i in range(count):
        new_value += int(diff[i][0])
    extrapolate.append(new_value)

total = 0
for i in extrapolate:
    total += i

print(total)


    #     diff = []
    #     for i in range(len(line[-1])-1):
    #         diff.extend([abs(int(line[i])-int(line[i+1]))])
    #     count += 1
    #     line.append(diff)
    #     temp = set(diff)
    #     if len(set(diff)) == 1:
    #         break
    # counts.append(count)
    # new_value = 0
    # for idx,i in counts:
        # new += 
    # diff = []


# print(counts)