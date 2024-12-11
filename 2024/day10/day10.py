f = open("input.txt", "r")
grid = [list(map(int,line.strip())) for line in f.readlines()]

def out_of_bounds(pos):
    return pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0])

directions = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "RIGHT": (0, 1),
    "LEFT": (0, -1),
}

def get_trailhead_score(pos, previous_pos, visited):
    if out_of_bounds(pos) or pos in visited:
        return 0
    visited.add(pos)
    cellHeight = grid[pos[0]][pos[1]]
    if cellHeight == 9:
        return 1
    score = 0
    for direction in directions:
        nextCellPos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
        if out_of_bounds(nextCellPos) or nextCellPos == previous_pos:
            continue
        nextCellHeight = grid[nextCellPos[0]][nextCellPos[1]]
        if nextCellHeight == cellHeight + 1:
            score += get_trailhead_score((pos[0] + directions[direction][0], pos[1] + directions[direction][1]), pos, visited)
    return score

s = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            s += get_trailhead_score((i, j), (-1, -1), set())

print(s)
