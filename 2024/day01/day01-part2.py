f = open("input.txt", "r")
lines = f.readlines()
sides = [[int(side) for side in line.split()] for line in lines]
left_side, right_side = list(zip(*sides))

right_occurences = {}

for right in right_side:
    if right not in right_occurences:
        right_occurences[right] = 1
    else:
        right_occurences[right] += 1

print(right_occurences)

factors = [left * right_occurences[left] for left in left_side if left in right_occurences]

print(sum(factors))