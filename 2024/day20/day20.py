import math

f = open("input.txt", "r")
maze = [list(line.strip()) for line in f.readlines()]

start_pos = (0, 0)
end_pos = (0, 0)

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            start_pos = (i, j)
        elif maze[i][j] == "E":
            end_pos = (i, j)

def out_of_bounds(pos):
    return pos[0] < 0 or pos[0] >= len(maze) or pos[1] < 0 or pos[1] >= len(maze[0])

def heuristic(posA, posB):
    return abs(posA[0] - posB[0]) + abs(posA[1] - posB[1])

directions = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}

def is_border(pos):
    border = False
    for direction in directions:
        new_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
        if out_of_bounds(new_pos):
            border = True
            break
    return border

def is_worth_exploring(pos, maze):
    around_blocked = 0
    for direction in directions:
        new_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
        around_blocked += 1 if maze[new_pos[0]][new_pos[1]] == "#" else 0
    return around_blocked < 3

def get_course_time(maze, max_time = math.inf):
    open_set = set([start_pos])
    came_from = {}
    g_score = {start_pos: 0}
    f_score = {start_pos: heuristic(start_pos, end_pos)}

    while len(open_set) > 0:
        current = min(open_set, key=lambda pos: f_score[pos])
        if current == end_pos:
            break

        open_set.remove(current)
        for direction in directions:
            newPos = (current[0] + directions[direction][0], current[1] + directions[direction][1])
            tentative_g_score = g_score[current] + 1
            if out_of_bounds(newPos) or maze[newPos[0]][newPos[1]] == "#" or tentative_g_score >= max_time:
                continue

            if newPos not in g_score or tentative_g_score < g_score[newPos]:
                came_from[newPos] = current
                g_score[newPos] = tentative_g_score
                f_score[newPos] = tentative_g_score + heuristic(newPos, end_pos)
                open_set.add(newPos)

    return g_score[end_pos] if end_pos in g_score else math.inf

normal_course_time = get_course_time(maze)
more_than_100_cheats = 0

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] != '#' or is_border((i, j)) or not is_worth_exploring((i, j), maze):
            continue
        maze[i][j] = '.'
        cheating_time = get_course_time(maze, normal_course_time)
        diff = normal_course_time - cheating_time
        if diff >= 100:
            more_than_100_cheats += 1
        maze[i][j] = '#'

print(more_than_100_cheats)
