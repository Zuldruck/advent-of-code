f = open("input.txt", "r")
grid, moves = f.read().split('\n\n')
grid = [list(row) for row in grid.split('\n')]
moves = "".join(moves.split('\n'))

robotPos = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            robotPos = (i, j)
            break
    if robotPos != (0, 0):
        break

directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

def movePos(pos, direction):
    return (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

def moveBoxes(nextPos, move):
    if grid[nextPos[0]][nextPos[1]] != "O":
        return
    direction = directions[move]
    boxPos = nextPos
    while grid[boxPos[0]][boxPos[1]] == "O":
        nextBoxPos = (boxPos[0] + direction[0], boxPos[1] + direction[1])
        boxPos = nextBoxPos
    if grid[boxPos[0]][boxPos[1]] != ".":
        return
    grid[nextPos[0]][nextPos[1]] = "."
    grid[boxPos[0]][boxPos[1]] = "O"

for move in moves:
    nextPos = movePos(robotPos, move)
    moveBoxes(nextPos, move)
    if grid[nextPos[0]][nextPos[1]] != ".":
        continue
    grid[robotPos[0]][robotPos[1]] = "."
    grid[nextPos[0]][nextPos[1]] = "@"
    robotPos = nextPos

gpsSum = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "O":
            gpsSum += 100 * i + j

print(gpsSum)