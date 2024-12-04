from itertools import product

dot = '.'
hash = '#'

with open(r'I:\Code\AOC\d12\test.txt') as file:
    board = [lines.rstrip() for lines in file]


def check(spring,group):
    
    new_spring = (spring+'?')*5
    new_group = group*5

    spring = new_spring
    group = new_group

    question_count = spring.count('?')
    combination = ([''.join(x) for x in product('#.',repeat=question_count)])
    

    count = 0
    for combi in combination:
        i = 0
        string = list(spring)
        for j,char in enumerate(string):
            if char == '?':
                string[j] = combi[i]
                i += 1
        string = ''.join(string)   
        only_spring = list(filter(None,string.split('.')))
        only_spring_count = [int(i.count('#')) for i in only_spring]
        if only_spring_count == group:
            count += 1
    return count

total = 0

for idx in range(len(board)):
    lines = board[idx]
    springs = lines.split()[0]
    group = [int(i) for i in lines.split()[1].split(',')]
    total += check(springs,group)

print(total)




