with open(r"I:\Code\AOC\2015\day6\test.txt", "r") as file:
    board = [lines.strip() for lines in file]

# print(board)

# main_lights = []
#
# for i in range(1000):
#     for j in range(1000):
#         main_lights[i][j] = 0

main_lights = [[0 for i in range(1000)] for j in range(1000)]


def on_off(cond, x, y):
    if cond == "on":
        main_lights[x][y] = 1
    else:
        main_lights[x][y] = 0


def coord(lines, length):
    if length == 4:
        start = lines.split()[1].split(",")
        stop = lines.split()[3].split(",")
        return start[0], start[1], stop[0], stop[1]
    start = lines.split()[2].split(",")
    stop = lines.split()[4].split(",")
    return int(start[0]), int(start[1]), int(stop[0]), int(stop[1])


def toggle(x, y):
    if main_lights[x][y] == 0:
        main_lights[x][y] = 1
    else:
        main_lights[x][y] = 0


def check(lines):
    startx, starty, stopx, stopy = coord(lines, len(lines.split()))
    if len(lines.split()) == 4:
        for i in range(int(startx), int(stopx)+1):
            for j in range(int(starty), int(stopy)+1):
                toggle(i, j)
    else:
        if lines.split()[1] == "on":
            for i in range(int(startx), int(stopx)+1):
                for j in range(int(starty), int(stopy)+1):
                    on_off("on", i, j)
        else:
            for i in range(int(startx), int(stopx)+1):
                for j in range(int(starty), int(stopy)+1):
                    on_off("off", i, j)


for line in board:
    string = line.split()
    # print(string)
    # print(len(string))
    check(line)

result = 0

for i in range(1000):
    total = main_lights[i].count(1)
    result += total

print(result)
# print(main_lights[0])
