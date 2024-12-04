with open(r"./input.txt") as file:
    input = [line.strip() for line in file]
    input = [list(map(int, line.split())) for line in input]


# print(input)


# def check(inp: list) -> int:
#     # good = False
#     for j in range(len(inp)):
#         xs = inp[:j] + inp[j + 1 :]
#         change = True if xs == sorted(xs) or xs == sorted(xs, reverse=True) else False
#         ok = True
#         for i in range(len(xs) - 1):
#             diff = abs(inp[i] - inp[i + 1])
#             if not 1 < diff < 3:
#                 ok = False
#         if ok and change:
#             good = True

total = 0
for inp in input:
    good = False
    for j in range(len(inp)):
        xs = inp[:j] + inp[j + 1 :]
        change = True if xs == sorted(xs) or xs == sorted(xs, reverse=True) else False
        ok = True
        for i in range(len(xs) - 1):
            diff = abs(xs[i] - xs[i + 1])
            if not 1 <= diff <= 3:
                ok = False
        if ok and change:
            good = True
    if good:
        # print(inp)
        total += 1

print(total)
