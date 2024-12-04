with open(r'I:\Code\AOC\d4\1.txt','r') as f:
    cards = [line.strip()[8:] for line in f]
    
# print(cards)

wins,draws = [],[]
copy = []

for card in cards:
    card_split = card.split('|')
    wins.append(card_split[0])
    draws.append(card_split[1])

# print(wins)
# print(draws)

dic = {}
    
def append_dic(idx,num):
    repeat = dic[idx-1]
    for r in range(repeat):
        for n in range(num):
            if idx+n in dic:
                dic[idx+n] += 1
            else:
                dic[idx+n] = 1


for i in range(len(wins)):
    win_split = wins[i].split()
    draws_split = draws[i].split()
    # if i == 2:
    #     break
    total = sum([num in draws_split for num in win_split])
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
    append_dic(i+1,total)

# print(total)
# print(dic)
    
result = sum([v for v in dic.values()])
print(result)