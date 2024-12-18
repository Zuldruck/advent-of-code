f = open("input.txt", "r")
maze = [list(line.strip()) for line in f.readlines()]

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

startPos = (0, 0)
endPos = (0, 0)

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            startPos = (i, j)
        elif maze[i][j] == "E":
            endPos = (i, j)

openSet = set([startPos])
cameFrom = {}
gScore = {startPos: 0}
fScore = {startPos: heuristic(startPos, endPos)}

while len(openSet) > 0:
    current = min(openSet, key=lambda pos: fScore[pos])
    if current == endPos:
        break

    openSet.remove(current)
    currentGScore = gScore[current]
    for direction in directions:
        newPos = (current[0] + directions[direction][0], current[1] + directions[direction][1])
        if out_of_bounds(newPos) or maze[newPos[0]][newPos[1]] == "#" or newPos == cameFrom.get(current, None):
            continue

        angle = False
        if current in cameFrom and cameFrom[current][0] != newPos[0] and cameFrom[current][1] != newPos[1]:
            angle = True

        tentative_gScore = currentGScore + 1
        if angle:
            tentative_gScore += 1000
        if current == startPos and direction == "UP":
            tentative_gScore += 1000
        
        if newPos not in gScore or tentative_gScore < gScore[newPos]:
            if angle:
                gScore[current] = currentGScore + 1000
            cameFrom[newPos] = current
            gScore[newPos] = tentative_gScore
            fScore[newPos] = tentative_gScore + heuristic(newPos, endPos)
            openSet.add(newPos)

print(gScore[endPos])

current = endPos
visited = set()
while current in cameFrom:
    visited.add(current)
    current = cameFrom[current]

for i in range(len(maze)):
    for j in range(len(maze[0])):
        print("O" if (i, j) in visited else maze[i][j], end="")
    print()
