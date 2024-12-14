import re

GRID_WIDTH = 101
GRID_HEIGHT = 103
SECONDS_ELAPSED = 100

f = open("input.txt", "r")
robots = [
    map(int, re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups())
    for line in f.readlines()
]

quadrant_up_left = 0
quadrant_up_right = 0
quadrant_down_left = 0
quadrant_down_right = 0
for robot in robots:
    p_x, p_y, v_x, v_y = robot
    final_x = (p_x + v_x * SECONDS_ELAPSED) % GRID_WIDTH
    final_y = (p_y + v_y * SECONDS_ELAPSED) % GRID_HEIGHT
    if final_x > GRID_WIDTH / 2:
        if final_y > GRID_HEIGHT / 2:
            quadrant_down_right += 1
        elif final_y < GRID_HEIGHT // 2:
            quadrant_up_right += 1
    elif final_x < GRID_WIDTH // 2:
        if final_y > GRID_HEIGHT / 2:
            quadrant_down_left += 1
        elif final_y < GRID_HEIGHT // 2:
            quadrant_up_left += 1

print(quadrant_up_left * quadrant_up_right * quadrant_down_left * quadrant_down_right)
