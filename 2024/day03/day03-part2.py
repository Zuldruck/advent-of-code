import re

f = open("input.txt", "r")
memory = f.read()

matches = re.finditer(r"(?:mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\))", memory, re.MULTILINE)

res = 0
do = True
for match in matches:
    a, b, do_instruction, dont_instruction = match.groups()
    if do_instruction:
        do = True
    if dont_instruction:
        do = False
    if a is not None and b is not None and do:
        res += int(a) * int(b)

print(res)
