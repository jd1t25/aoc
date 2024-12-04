time,dis = "",""
distance = 0
with open(r'I:\Code\AOC\d6\1.txt','r') as f:
    for line in f:
        for i in line.rstrip('\n').split():
            if i.isdigit():
                if distance:
                    dis += str(i)
                else:
                    time += str(i)
            if i == "Distance:":
                distance = 1
# print(time,dis)

# time = len(time)
# dis = len(dis)
total = 1

count = 0
h=0
while h in range(int(time)):
    if min(h,abs(h-int(time))) != 0: 
        if abs(h-int(time))*h > int(dis):
            count += 1
    h += 1
total *= count

print(total)