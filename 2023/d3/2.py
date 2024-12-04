with open(r'I:\Code\AOC\d3\1.txt','r') as file:
    board = [lines.strip() for lines in file]

# print(board)

dir = [(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(0,1),(0,-1),(1,1)]

sym=[]

def symbol(board):
    for lines in board:
        line = lines.split('.')
        for x in line:
            if not x.isalnum():
                if x not in sym:
                    if len(x) > 1:
                        sym.append(''.join([i for i in x if not i.isdigit()]))
                    else:
                        sym.append(x)
    sym.remove('')

neg = []
sums = []
less = []

def check(num,row,index):
    for idx,i in enumerate(num):
        end = 0
        for d in dir:
            x,y = d
            newx = row+x
            newy = idx + index + y
            # if 0 <= newx < len(board) and 0 <= newy < len(board[0]):
            # if 0 <= newy < len(board[0]):
            if newx < 0:
                newx = len(board) - 1 + x
            if newy < 0:
                newy = len(board[0]) - 1 + y
            if newx > len(board)-1:
                newx = 0 + x
            if newy > len(board)-1:
                newy = 0 + y
            string = board[newx][newy]
            if string in sym:
                # if board[row][index-1] == '-':
                #     return -1
                # else:
                return 1
    return 0

def main(board):
    for row,string in enumerate(board):
        temp2 = string
        for x in sym:
            # if x in string:
                temp = temp2.replace(x,'.')
                temp2 = temp
        nums =  temp.split('.')
        nums = list(filter(None,nums))
        if nums:
            for num in nums:
                idx = string.index(num)
                number_found=check(num,row,idx)
                # if number_found == -1:
                #     neg.append(num)
                if number_found:
                    sums.append(num)
                # if len(num) < 3:
                #     less.append(num)
            # print(sums)
        # nums = [i for i in nums if i not in sym]
        

symbol(board)
main(board)
print(sums)
# print(neg)
# print(less)
# # print(sym)
sums = [int(i) for i in sums]
# neg = [int(i) for i in neg]

# total = sum(sums) - sum(neg)

print(sum(sums))
# print(total)