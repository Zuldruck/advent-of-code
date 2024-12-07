f = open("input.txt", "r")
equations = [(int(line.split(': ')[0]), list(map(int, line.split(': ')[1].split()))) for line in f.readlines()]

def rec(target, operands):
    if len(operands) == 1:
        return target == operands[0]
    
    return (
        rec(target - operands[-1], operands[:-1]) or
        rec(target / operands[-1], operands[:-1])
    )

res = 0
for equation in equations:
    target = equation[0]
    operands = equation[1]
    if rec(target, operands):
        res += target

print(res)
