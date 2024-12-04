dic = {
    'red' : 12,
    'green': 13,
    'blue' : 14
}

t = []
total = 0
result = 1

with open(r"I:\Code\AOC\d2\1.txt", 'r') as line:
    for l in line:
        # if idx == 1:
        #     break
        temp = l.replace(":","").replace(",","").replace(";","").split()
        res = []
        brk = 0
        for idx,(key,val) in enumerate(dic.items()):
            index = 0
            while index < len(temp):
                if temp[index] == key:
                    res.append(int(temp[index-1]))
                index += 1
            result *= max(res)
            res = []
        total += int(result)
        result = 1
print(total)