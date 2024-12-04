with open(r'I:\Code\AOC\d6\1.txt','r') as f:
    board = [lines.rstrip() for lines in f]
temp = []
for line in board:
        temp2 = line.split()
        temp.append(temp2)   
# print(temp[0][1])
time = temp[0][1:]
dis = temp[1][1:]
# print(time,dis)

# race = []
# hold = []
total,speed = 1,1

r,h = 0,0

while r < len(time):
    count = 0
    h=0
    while h in range(int(time[r])):
        if min(h,abs(h-int(time[r]))) != 0: 
            if abs(h-int(time[r]))*h > int(dis[r]):
                count += 1
        h += 1
    total *= count
    r += 1

print(total)








# while r < len(time):
#     count = 0
#     h=0
#     while h in range(int(time[r])):
#         if min(h,abs(h-int(time[r]))) != 0: 
#             hold = abs(h-int(time[r]))*h
#             if hold > int(dis[r]):
#                 count += 1
#         h += 1
#     total *= count
#     r += 1