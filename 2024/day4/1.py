# print(input)
# print(len(input[0]))
# print(input[0][11])

# def loop_index(idx:int) -> int:
#     if idx


def forward(idx: int) -> int:
    result = []
    for i in range(XMAS_LEN):
        result.append(input[0][(idx + i) % LEN])
    if "".join(result) == WORD:
        return 1
    else:
        return 0


def backward(idx: int) -> int:
    result = []
    for i in range(XMAS_LEN):
        result.append(input[0][(idx - i)])
    if "".join(result) == WORD[::-1]:
        return 1
    else:
        return 0


def vertical(row: int, j: int) -> int:
    result = []
    for i in range(XMAS_LEN):
        result.append(input[(row + i) % len(input)][j])
    if "".join(result) == WORD:
        return 1
    else:
        return 0


def vertical_backward(row: int, j: int) -> int:
    result = []
    for i in range(XMAS_LEN):
        result.append(input[(row - i)][j])
    if "".join(result) == WORD:
        return 1
    else:
        return 0


def diagonal(row: int, col: int) -> int:
    result = []
    ans = 0
    # top left
    for i in range(XMAS_LEN):
        result.append(input[(row - i) % ROWLEN][(col - i) % LEN])
    if "".join(result) == WORD:
        ans += 1

    # top right
    for i in range(XMAS_LEN):
        result.append(input[(row + i) % ROWLEN][(col + i) % LEN])
    if "".join(result) == WORD:
        ans += 1

    # bottom left
    for i in range(XMAS_LEN):
        result.append(input[(row + i) % ROWLEN][(col - i) % LEN])
    if "".join(result) == WORD:
        ans += 1

    # bottom right
    for i in range(XMAS_LEN):
        result.append(input[(row + i) % ROWLEN][(col + i) % LEN])
    if "".join(result) == WORD:
        ans += 1

    return ans


if __name__ == "__main__":
    with open(r"./test.txt") as file:
        input = [line.strip() for line in file]
        # input = [list(line.strip()) for line in file]

    LEN = len(input[0])
    ROWLEN = len(input)
    WORD = "XMAS"
    XMAS_LEN = len(WORD)

    total = 0
    for i, word in enumerate(input):
        for row in range(len(word)):
            total += forward(i)
            total += backward(i)
            total += vertical_backward(row, i)
            total += vertical(row, i)
            total += diagonal(row, i)

    print(total)
