with open(r'I:\Code\AOC\d19\1.txt','r') as file:
    board = [lines.rstrip('\n') for lines in file]

empty_string = board.index('')

workflow = board[:empty_string]
ratings = board[empty_string+1:]

# print(workflow)
# print(ratings)



dic = {}

for i in workflow:
    k = i[:i.index('{')]
    v = i[i.index('{')+1:i.index('}')]
    dic[k] = v

# print(dic)
# print(ratings)

accepted = []
# rejected = []

def get_string(stringr):
    stringr = stringr.split('=')
    return stringr[0],stringr[1]

def check(call):
    val = dic[call].split(',')
    cond = val[:len(val)-1]
    next = val[-1]
    idx = 1
    for c in cond:
        main_cond = c.split(':')
        if '<' in main_cond[0]:
            less = main_cond[0].split('<')
            if int(rating[less[0]]) < int(less[1]):
                if main_cond[1] == 'A':
                    idx = 0
                    accepted.append(list(rating.values()))
                elif main_cond[1] != 'R':
                    idx = 0
                    check(main_cond[1])
        elif '>' in main_cond[0]:
            less = main_cond[0].split('>')
            if int(rating[less[0]]) > int(less[1]):
                # check(main_cond[1])
                if main_cond[1] == 'A':
                    idx = 0
                    accepted.append(list(rating.values()))
                elif main_cond[1] != 'R':
                    idx = 0
                    check(main_cond[1])
    if idx:
        if next == 'A':
            accepted.append(list(rating.values()))
        elif next != 'R':
            check(next)


for r in ratings:
    rating = {
    'x' : '',
    'm' : '',
    'a' : '',
    's' : ''
    }
    string = r.replace('{','').replace('}','').split(',')
    for c in string:
        char,val = get_string(c)
        rating[char] = val
    check('in')

# print(accepted)
total = 0

for i in accepted:
    for val in i:
        total += int(val)

print(total)