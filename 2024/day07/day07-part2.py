f = open("input.txt", "r")
equations = [(int(line.split(': ')[0]), list(map(int, line.split(': ')[1].split()))) for line in f.readlines()]

def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

res = 0
operators = ['+', '*', '||']
for equation in equations:
    target = equation[0]
    operands = equation[1]
    for i in range(3**(len(operands) - 1)):
        ternaryStr = ternary(i).zfill(len(operands) - 1)
        equationRes = operands[0]
        for operand, op in zip(operands[1:], ternaryStr):
            if op == '0':
                equationRes += operand
            elif op == '1':
                equationRes *= operand
            else:
                equationRes = int(str(equationRes) + str(operand))
        if equationRes == target:
            res += target
            break

print(res)
