import re

GRID_WIDTH = 101
GRID_HEIGHT = 103
SECONDS_ELAPSED = 100

f = open("input.txt", "r")
robots = [
    map(int, re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups())
    for line in f.readlines()
]

grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
for second in range(10000):
    if second % 101 == 28:
        print("Second", second)
    new_robots = []
    for robot in robots:
        p_x, p_y, v_x, v_y = robot
        grid[p_y][p_x] -= 1
        next_x = (p_x + v_x) % GRID_WIDTH
        next_y = (p_y + v_y) % GRID_HEIGHT
        grid[next_y][next_x] += 1
        new_robots.append((next_x, next_y, v_x, v_y))
    robots = new_robots

    if second % 101 != 28:
        continue
    for row in grid:
        print("".join(["#" if x > 0 else "." for x in row]))
    print()


# THIS WAS A TROLL DAY, WE NEEDED TO FIND A CHRISTMAS TREE PATTERN IN THE GRID
# I PRINTED THE GRID EVERY 101 SECONDS FROM 28 BECAUSE I SAW A PATTERN COMING
# EVERY 101 SECONDS
