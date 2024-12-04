with open (r'I:\Code\AOC\d25\test.txt','r') as file:
    board = [lines.strip() for lines in file]

# print(board)

dic = {}

# for line in board:
#     left = line.split(':')[0]
#     right = line.split(':')[1]

left = [line.split(':')[0] for line in board]
right = [line.split(':')[1] for line in board]

# print(left)
# print(right)
# print([i.split() for i in right])

for node in left:
    dic[node] = 1

# print(dic)

for nodes in right:
    for node in nodes.split():
        if node in dic.keys():
            dic[node] += 1
        else:
            dic[node] = 1

print(dic)

maxval = max(dic.values())
print(maxval)

have = [k for k,v in dic.items() if v != maxval]
remove = [k for k,v in dic.items() if v == maxval]
# print(have)
# print(remove)

# # for idx,k in enumerate(right):
# #     # for v in k.split(':')[1]:
# #     temp = k.split()
# #     # temp = [i.split() for i in temp1]
# #     if remove[0] in temp:
# #         temp.remove(remove[0])
# #         board[k] = ''.join(temp)
# #         break

# for idx,string in enumerate(right):
#     if remove[0] in string:
#         right[idx] = right[idx].replace(remove[0],'')
#         break
# print(right)

# one,two = [],[]

# for line in board:
#     for left in line.split(':')[0]:
    
