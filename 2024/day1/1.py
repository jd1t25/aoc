with open(f'day1\input.txt') as file:
    input = [line.strip() for line in file]

left,right = [],[]

for l in input:
    l = l.split()
    left.append(int(l[0]))
    right.append(int(l[1]))

# print(left,right)
left = sorted(left)
right = sorted(right)

total = []

for l,r in zip(left,right):
    minus = abs(l-r)
    total.append(minus)

# print(total)
print(sum(total))