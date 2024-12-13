import re

f = open("input.txt", "r")
machines = [
    map(int, re.search(r"A: X\+(\d+), Y\+(\d+)\n.+B: X\+(\d+), Y\+(\d+)\n.+: X=(\d+), Y=(\d+)", machine_text).groups())
    for machine_text in f.read().split("\n\n")
]

total_tokens = 0
for machine in machines:
    A_X, A_Y, B_X, B_Y, price_X, price_Y = machine
    price_X = price_X + 10000000000000
    price_Y = price_Y + 10000000000000
    b = (price_Y * A_X - A_Y * price_X) / (-A_Y * B_X + B_Y * A_X)
    a = (price_X - B_X * b) / A_X
    if a.is_integer() and b.is_integer():
        a = int(a)
        b = int(b)
        total_tokens += a * 3 + b

print(total_tokens)
