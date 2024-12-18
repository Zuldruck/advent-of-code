f = open("input.txt", "r")
grid, moves = f.read().split('\n\n')

def widerRow(row):
    newRow = []
    for char in row:
        if char == "O":
            newRow.append("[")
            newRow.append("]")
        elif char == "@":
            newRow.append("@")
            newRow.append(".")
        else:
            newRow.append(char)
            newRow.append(char)
    return newRow

grid = [
    widerRow(row)
    for row in grid.split('\n')
]
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

# pos is the leftmost char of the box
def canBoxMoveInDirection(boxPos, direction, boxes):
    if direction == directions["^"] or direction == directions["v"]:
        # Direction is up or down
        nextDirectionPos = (boxPos[0] + direction[0], boxPos[1] + direction[1])
        boxes.add(boxPos)
        if grid[nextDirectionPos[0]][nextDirectionPos[1]] == "." and grid[nextDirectionPos[0]][nextDirectionPos[1] + 1] == ".":
            return True
        if grid[nextDirectionPos[0]][nextDirectionPos[1]] == "#" or grid[nextDirectionPos[0]][nextDirectionPos[1] + 1] == "#":
            return False
        adjacentBoxesDirection = {
            directions["^"]: [(-1, 0), (-1, 1)],
            directions["v"]: [(1, 0), (1, 1)],
        }
        for adjacentBoxDirection in adjacentBoxesDirection[direction]:
            adjacentBoxPos = (boxPos[0] + adjacentBoxDirection[0], boxPos[1] + adjacentBoxDirection[1])
            if grid[adjacentBoxPos[0]][adjacentBoxPos[1]] == "]":
                adjacentBoxPos = (adjacentBoxPos[0], adjacentBoxPos[1] - 1)
            if grid[adjacentBoxPos[0]][adjacentBoxPos[1]] == "[" and grid[adjacentBoxPos[0]][adjacentBoxPos[1] + 1] == "]":
                if not canBoxMoveInDirection(adjacentBoxPos, direction, boxes):
                    return False
                boxes.add(adjacentBoxPos)
        return True
    
    # Direction is left or right
    nextDirectionPos = {
        directions["<"]: (boxPos[0], boxPos[1] - 1),
        directions[">"]: (boxPos[0], boxPos[1] + 2),
    }
    boxes.add(boxPos)
    if grid[nextDirectionPos[direction][0]][nextDirectionPos[direction][1]] == ".":
        return True
    if grid[nextDirectionPos[direction][0]][nextDirectionPos[direction][1]] == "#":
        return False
    adjacentDirectionBoxPos = {
        directions["<"]: (boxPos[0], boxPos[1] - 2),
        directions[">"]: (boxPos[0], boxPos[1] + 2),
    }
    adjacentBoxPos = adjacentDirectionBoxPos[direction]
    boxes.add(adjacentBoxPos)
    return canBoxMoveInDirection(adjacentBoxPos, direction, boxes)


def moveBoxes(nextPos, move):
    if grid[nextPos[0]][nextPos[1]] not in ["[", "]"]:
        return
    direction = directions[move]
    boxPos = nextPos if grid[nextPos[0]][nextPos[1]] == "[" else (nextPos[0], nextPos[1] - 1)
    boxes = set()
    if not canBoxMoveInDirection(boxPos, direction, boxes):
        return
    for box in boxes:
        grid[box[0]][box[1]] = "."
        grid[box[0]][box[1] + 1] = "."
    for box in boxes:
        grid[box[0] + direction[0]][box[1] + direction[1]] = "["
        grid[box[0] + direction[0]][box[1] + direction[1] + 1] = "]"

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
        if grid[i][j] == "[":
            gpsSum += 100 * i + j

print(gpsSum)