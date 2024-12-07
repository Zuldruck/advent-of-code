f = open("input.txt", "r")
equations = [(int(line.split(': ')[0]), list(map(int, line.split(': ')[1].split()))) for line in f.readlines()]

res = 0
for equation in equations:
    target = equation[0]
    operands = equation[1]
    for i in range(2**(len(operands) - 1)):
        binary = bin(i)[2:].zfill(len(operands) - 1)
        equationRes = operands[0]
        for operand, bit in zip(operands[1:], binary):
            if bit == '0':
                equationRes += operand
            else:
                equationRes *= operand
        if equationRes == target:
            res += target
            break

print(res)
