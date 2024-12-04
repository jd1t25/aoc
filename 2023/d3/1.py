# symbols = ['*','#','+','$','@','/','!','=','%','^','&']
symbols = ['*', '&', '/', '@', '=', '+', '#', '$', '%', '-']
cycle = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
inp = []
# temp = ""
# count=total= 0
# num = ""
# num1 = 0
# temp1 = []
# row_count=col_count=0
# sym = 0
num_found = 0

with open(r'I:\Code\AOC\d3\test.txt','r') as f:
    board = [lines.rstrip('\n') for lines in f]

# print(board[8][5])

def remove_sym(strings):
    for sym in symbols:
        for i in range(len(strings)):
            strings[i] = strings[i].replace(sym,'')
    strings = list(filter(None,strings))
    return strings

for idx,lines in enumerate(board):
    # if idx == 5:
    #     break
    split = lines.split('.')
    split = list(filter(None,split))
    split = remove_sym(split)
    for num in split:
        if num not in symbols:
            index = lines.find(num)
            for i in range(len(num)):
                for c in cycle:
                    cx,cy = c[0],c[1]
                    # if idx == 0:
                    #     if idx+cx < 0:
                    #         continue
                    # if idx == len(board):
                    #     if idx+cx == 0:
                    #         continue
                    # if i == 0:
                    #     if index+i+cy < 0:
                    #         continue
                    # if i == len(board):
                    #     if index+i+cy == 0:
                    #         continue
                    # try:
                    newx = idx+cx
                    newy = i+cy+index
                    if 0<=newx<len(board[0]) and 0<=newy<len(board): 
                        if board[newx][newy] in symbols:
                            inp.append(num)
                            num_found = 1
                            break
                    # except IndexError:
                    #     continue
                if num_found:
                    break
            # if num_found:
            #         break
        num_found = 0
    
print(inp)

temp = [int(x) for x in inp]
total = sum(temp)
print(total)