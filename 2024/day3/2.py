import re

with open(r"./input.txt") as file:
    content = file.read()

# search = re.findall(r"\/mul\(\d{1,3},\d{1,3}\)\/", content)
# search = re.findall(r"mul\(\d{1,3},\d{1,3}\)", content)

# print(search)
#
# total = 0
# for string in search:
#     num = re.findall(r"\d+", string)
#     total += int(num[0]) * int(num[1])
#
# print(total)

total = 0
mulpattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

search = re.findall(mulpattern, content)

# print(search)
# dopattern = r"do\(\)"
# dontpattern = r"don't\(\)"
doval = 1
for x in search:
    if x == "don't()":
        doval = 0
    elif x == "do()":
        doval = 1
    else:
        if doval:
            intval = re.findall(r"\d+", x)
            total += int(intval[0]) * int(intval[1])


# for i, c in enumerate(content):
#     if c == "d":
#         arr = content[i : i + 7]
#         if re.findall(dopattern, arr):
#             doval = 1
#         elif re.findall(dontpattern, arr):
#             doval = 0
#         else:
#             doval = -1
#     if c == "m":
#         search = re.findall(mulpattern, content[i : i + 12])
#         if search and doval:
#             intval = re.findall(r"\d+", search[0])
#             total += int(intval[0]) * int(intval[1])
#
print(total)
