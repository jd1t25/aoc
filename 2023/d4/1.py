win_num=[]
appear_num = []
total = 0
dic = {}

with open(r'I:\Code\AOC\d4\test.txt','r') as f:
    cards = [line.strip('\n')[8:] for line in f]
    cards = [line.split(" ") for line in cards]

for i,card in enumerate(cards):
    if i == 3:
        break
    idx = 0
    while card[idx] != "|":
        if card[idx] == "":
            idx += 1
            pass
        win_num.append(card[idx])
        idx += 1
    idx += 1
    while idx < len(card):
        if card[idx] == '':
            idx += 1
            pass
        appear_num.append(card[idx])
        idx += 1
    count = 0
    for num in appear_num:
        if num in win_num:
            count += 1
    if i not in dic:
        dic[i+1] = 1
    else:
        dic[i+1] += 1
    idx = 1
    while idx <= count:
        if i+idx+1 not in dic:
            dic[i+idx+1] = 0
        dic[i+idx+1] += 1
        idx += 1
    # if i not in dic:
    #     dic[i+1] = 0
    # dic[i+1] += count
    # idx = 1
    # while idx <= count:
    #     if i+idx+1 not in dic:
    #         dic[idx+1+i] = 0
    #     dic[idx+1+i] += 1
    #     idx += 1 
    # idx = i+1
    # temp = 0
    # while temp < count:
    #     if i+idx+1 not in dic:
    #         dic[idx+1+temp] = 0
    #     dic[idx+1+temp] += 1
    #     idx += 1
    # total += count
    win_num = []
    appear_num = []
    
    

print(total)
# print(win_num)
# print(appear_num)
# print(cards)


    # char2 = [line.split(" ") for line in cards]
    # for line in cards:
    #     char.extend([line.split(" ")])
    # for i in f:
    #     # cards.append(i.strip('\n')[8:])
    #     cards.append(i.strip('\n'))
    # print(char2)
        