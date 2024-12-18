import re

f = open("input.txt", "r")
groups = re.search(r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: (.+)", f.read()).groups()
reg_a, reg_b, reg_c = map(int, groups[:3])
program = list(map(int, groups[3].split(",")))

pointer = 0
output = []
while pointer < len(program):
    combos = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: reg_a,
        5: reg_b,
        6: reg_c,
    }
    instruction = program[pointer]
    operand = program[pointer + 1]
    combo = combos[operand] if operand != 7 else None
    jump = None
    if instruction == 0:
        reg_a = int(reg_a / (2 ** combo))
    elif instruction == 1:
        reg_b ^= operand
    elif instruction == 2:
        reg_b = combo % 8
    elif instruction == 3 and reg_a != 0:
        jump = operand
    elif instruction == 4:
        reg_b ^= reg_c
    elif instruction == 5:
        output.append(str(combo % 8))
    elif instruction == 6:
        reg_b = int(reg_a / (2 ** combo))
    elif instruction == 7:
        reg_c = int(reg_a / (2 ** combo))
    pointer = jump if jump is not None else pointer + 2

print('reg_a:', reg_a)
print('reg_b:', reg_b)
print('reg_c:', reg_c)
print(output)
print(",".join(output))
