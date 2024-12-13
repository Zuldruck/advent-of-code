import re

f = open("input.txt", "r")
machines = [
    map(int, re.search(r"A: X\+(\d+), Y\+(\d+)\n.+B: X\+(\d+), Y\+(\d+)\n.+: X=(\d+), Y=(\d+)", machine_text).groups())
    for machine_text in f.read().split("\n\n")
]

total_tokens = 0
for machine in machines:
    A_X, A_Y, B_X, B_Y, price_X, price_Y = machine
    for a in range(1, 100):
        found = False
        for b in range(1, 100):
            if A_X * a + B_X * b == price_X and A_Y * a + B_Y * b == price_Y:
                total_tokens += a * 3 + b
                found = True
                break
        if found:
            break

print(total_tokens)
