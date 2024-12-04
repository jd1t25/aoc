with open(r"./text.txt") as file:
    input = [line.strip() for line in file]
    input = [list(map(int, line.split())) for line in input]


# print(input)
def changing(a: int, b: int) -> int:
    if a > b:
        return 0
    elif a < b:
        return 1
    else:
        return -1


def check(inp: list):
    change = changing(inp[0], inp[1])
    if change == -1:
        return [0, 0]
    for i in range(len(inp) - 1):
        if abs(inp[i] - inp[i + 1]) > 3 or abs(inp[i] - inp[i + 1]) < 1:
            return [0, i]
        if change:
            if inp[i] > inp[i + 1]:
                return [0, i]
        else:
            if inp[i] < inp[i + 1]:
                return [0, i]
    return [1, 0]


total = 0
for arr in input:
    val = check(arr)
    if val[0] != 1:
        arr.pop(val[1])
        val = check(arr)

    total += val[0]

print(total)
