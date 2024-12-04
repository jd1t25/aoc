with open(r'I:\Code\AOC\2015\day 5\1.txt','r') as file:
    board = [lines.strip() for lines in file]

not_allowed = ['ab','cd','pq','xy']
vowels = ['a','e','i','o','u']

# board = board[0]
# print(board)
accepted = 0

for line in board:
    double = False
    strings = True
    vowel_count = 0
    for i in range(len(line)):
        if line[i] in vowels:
            vowel_count += 1
        if i < len(line)-1:
            if line[i] == line[i+1]:
                double = True
            if line[i]+line[i+1] in not_allowed:
                strings = False

    if vowel_count >= 3 and double and strings:
        accepted += 1

print(accepted)