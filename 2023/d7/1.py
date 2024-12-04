from collections import Counter

with open(r'I:\Code\AOC\d7\1.txt','r') as file:
    board = [f.replace('\n','') for f in file]
# board = [f.split(' ') for f in board]
# print(board)
dic = {str(k):v for k,v in enumerate(range(1,9),2)}
dic.update({'T':9,'J':10,'Q':11,'K':12,'A':13})

# print(dic)

card_ranking = {
    (1,1): 0,
    (2,1): 1,
    (2,2): 2,
    (3,1): 3,
    (3,2): 4,
    (4,1): 5,
    (5,): 6
 
}
cards = [x.split(' ')[0] for x in board]
# print(cards)

bid = [x.split(' ')[1].replace('\n','') for x in board]
# print(bid)

board = {k:v for k,v in zip(cards,bid)}
# print(board)
ranks = [[] for i in range(7)]

def card_type(card):
    counted = Counter(card)
    # count = counted.most_common(1)
    # if len(counted) == 1:
    #     counter = 1
    # else:
    #     counter = 2
    two_most_common, count = zip(*counted.most_common(2))
    # print(counted)
    # two_most_common = [int(f) for f in two_most_common]
    return (count)

for idx,card in enumerate(board.keys()):
    print(card)
    card_id = card_ranking[card_type(card)]
    if not card_id == -1:
        if not len(ranks[card_id]):
            ranks[card_id].append(card)
        else:
            i = 0
            card1 = [*card]
            while i < len(ranks[card_id]):
                card2 = [*ranks[card_id][i]]
                sym = 0
                for j,k in zip(card1,card2):
                    card1_join = ''.join(card1)
                    if dic[j] > dic[k]:
                        ranks[card_id].insert(i+1,card1_join)
                        sym = 1
                        break
                    elif dic[j] < dic[k]:
                        ranks[card_id].insert(i,card1_join)
                        sym = 1
                        break
                if sym:
                    break
                i += 1
            
            # ranks[card_id].append(''.join(card2))

                    
print(ranks)
total = 0
multiply = 1
for i in ranks:
    for j in i:
        total += multiply*int(board[j])
        multiply += 1

print(total)
                         
# def card_type(card):
#     for idx,i in enumerate(card):
#         for j in card[idx:]:
#             if i == j:
#                 count.append(i)
# # print([f.rsplit() for f in board])




                    
        
            

# test = [1,2,3,4,5]
# temp =  []

# for f in test:
#     temp.extend([f])

# print(temp)
# cnt = [(i,board.count(i)) for i in set(board)]
# print(cnt)

# print(set(board))
# 