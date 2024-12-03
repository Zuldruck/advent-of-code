import re

f = open("input.txt", "r")
memory = f.read()

matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", memory, re.MULTILINE)

res = 0
for match in matches:
    a, b = match.groups()
    res += int(a) * int(b)

print(res)
