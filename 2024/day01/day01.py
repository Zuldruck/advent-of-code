f = open("input.txt", "r")
lines = f.readlines()
sides = [[int(side) for side in line.split()] for line in lines]
left_side, right_side = list(zip(*sides))
sorted_left_side = sorted(left_side)
sorted_right_side = sorted(right_side)
sorted_side_by_side = zip(sorted_left_side, sorted_right_side)
distances = [abs(left - right) for (left, right) in sorted_side_by_side]
print(sum(distances))