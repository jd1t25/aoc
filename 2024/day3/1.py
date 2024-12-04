import re

with open(r"./input.txt") as file:
    content = file.read()

# search = re.findall(r"\/mul\(\d{1,3},\d{1,3}\)\/", content)
search = re.findall(r"mul\(\d{1,3},\d{1,3}\)", content)

# print(search)

total = 0
for string in search:
    num = re.findall(r"\d+", string)
    total += int(num[0]) * int(num[1])

print(total)
