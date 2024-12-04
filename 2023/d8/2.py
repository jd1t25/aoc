with open(r'I:\Code\AOC\d8\1.txt', 'r') as file:
    board = file.readlines()    

board = [f.replace('\n','') for f in board]

turns = [*board[0]]
board = board[2:]

board = [i.split(' = ') for i in board]
board = dict(board)
# board = [i.replace('=','').replace('(','').replace(')','').replace(',','').split() for i in board[2:]]
# board = [i.split(' ') for i in board[2:]]
# print(board)
# print(turns)

dic = {
    'L': 1,
    'R': 2
}
# print(dic['L'])
# temp = board['AAA']
# print(temp)
# print(board['AAA'][board['AAA'].index(', ')+2:board['AAA'].index(')')])

def left_right(node,turn):
    next_node = board[node]
    if turn == 'L':
        left_node = next_node[next_node.index('(')+1:next_node.index(',')]
        return left_node
    else:
        right_node = next_node[next_node.index(', ')+2:next_node.index(')')]
        return right_node
    # return (node[0],node[1],node[2])

count = 0
end = 0
index = []

for idx,i in enumerate(list(board)):
    if i[2] == 'A':
        index.append(idx)

temp = list(board)
next_node = [list(board)[i] for i in index]
j=0
new_node = []
while True:
    
    for jdx,turn in enumerate(turns):
        # if jdx > 268:
        #     end = 1
        #     break
        end = []
        node = next_node
        for i in node:
            new_node.append(left_right(i,turn))
        count += 1
        next_node = new_node
        new_node = []
        if count == 1000000:
            print('yes')
        for i in next_node:
            if i[2] == 'Z':
                end.append(i)
        if len(end) == len(next_node):
            break
        # index += 1
    if len(end) == len(next_node):
        break
print(count)


