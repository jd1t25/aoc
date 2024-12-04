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
    if i == 'AAA':
        index.append(idx)
        break

next_node = list(board)[index]
j=0
while True:
    for jdx,turn in enumerate(turns):
        if jdx > 268:
            end = 1
            break
        node = next_node
        next_node = left_right(node,turn)
        count += 1
        if next_node == 'ZZZ':
            end = 1
            break
        # index += 1
    if end:
        break

print(count)


