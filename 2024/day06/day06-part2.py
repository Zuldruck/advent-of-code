f = open("input.txt", "r")
lines = f.readlines()

grid = []
guardPos = (-1, -1)
for i in range(len(lines)):
    try:
        guardIdx = lines[i].index('^')
    except:
        guardIdx = -1
    if guardIdx != -1:
        guardPos = (i, guardIdx)
    grid.append(list(lines[i].strip()))

def out_of_bounds(pos):
    return pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0])

directions = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1),
}
rotateRightDirections = {
    'UP': 'RIGHT',
    'RIGHT': 'DOWN',
    'DOWN': 'LEFT',
    'LEFT': 'UP',
}

direction = 'UP'
visited = 0
alreadyVisited = {}
initialGuardPos = guardPos
while not out_of_bounds(guardPos):
    if guardPos not in alreadyVisited:
        visited += 1
    alreadyVisited[guardPos] = True
    newPos = (guardPos[0] + directions[direction][0], guardPos[1] + directions[direction][1])
    if out_of_bounds(newPos):
        guardPos = newPos
        continue
    if grid[newPos[0]][newPos[1]] == '#':
        direction = rotateRightDirections[direction]
        continue
    guardPos = newPos

paths = [(x, y) for (x, y) in alreadyVisited.keys()]
loopings = 0
for (i, j) in paths:
    alreadyVisitedWithDirection = {}
    direction = 'UP'
    guardPos = initialGuardPos
    grid[i][j] = '#'
    while not out_of_bounds(guardPos):
        guardPosWithDirection = (guardPos[0], guardPos[1], direction)
        if guardPosWithDirection in alreadyVisitedWithDirection:
            loopings += 1
            break
        alreadyVisitedWithDirection[guardPosWithDirection] = True
        newPos = (guardPos[0] + directions[direction][0], guardPos[1] + directions[direction][1])
        if out_of_bounds(newPos):
            guardPos = newPos
            break
        if grid[newPos[0]][newPos[1]] == '#':
            direction = rotateRightDirections[direction]
            continue
        guardPos = newPos
    grid[i][j] = '.'

print(loopings)

