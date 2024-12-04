with open(r'day1\input.txt') as file:
    input = [line.strip() for line in file]

left,right = [],[]

for l in input:
    l = l.split()
    left.append(int(l[0]))
    right.append(int(l[1]))

# print(left,right)
# left = set(left)

hashright = dict()

for num in right:
    if num in hashright:
        hashright[num] += 1
    else:
        hashright[num] = 1

total = 0

for num in left:
    if num in hashright:
        total += num*hashright[num]

print(total)