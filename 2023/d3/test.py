temp = []

with open(r'I:\Code\AOC\d3\test.txt','r') as f:
    for line in f:
        for i in line:
            if not (i.isdigit() or i == '.'):
                if i not in temp:
                    temp.append(i)

print(temp)