f = open("input.txt", "r")
ram_bytes = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

startPos = (0, 0)
endPos = (70, 70)

def out_of_bounds(pos):
    return pos[0] < 0 or pos[0] > endPos[0] or pos[1] < 0 or pos[1] > endPos[1]

def heuristic(posA, posB):
    return abs(posA[0] - posB[0]) + abs(posA[1] - posB[1])

directions = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}

left = 1024
right = len(ram_bytes) - 1
first_blocking_end = None

while left <= right:
    corrupted_bytes_number = (left + right) // 2
    corrupted_bytes = set([(b_y, b_x) for b_x, b_y in ram_bytes[:corrupted_bytes_number]])
    openSet = set([startPos])
    cameFrom = {}
    gScore = {startPos: 0}
    fScore = {startPos: heuristic(startPos, endPos)}

    while len(openSet) > 0:
        current = min(openSet, key=lambda pos: fScore[pos])
        if current == endPos:
            break

        openSet.remove(current)
        for direction in directions:
            newPos = (current[0] + directions[direction][0], current[1] + directions[direction][1])
            if out_of_bounds(newPos) or newPos in corrupted_bytes:
                continue

            tentative_gScore = gScore[current] + 1
            if newPos not in gScore or tentative_gScore < gScore[newPos]:
                cameFrom[newPos] = current
                gScore[newPos] = tentative_gScore
                fScore[newPos] = tentative_gScore + heuristic(newPos, endPos)
                openSet.add(newPos)
    
    if endPos in gScore:
        left = corrupted_bytes_number + 1
    else:
        first_blocking_end = ram_bytes[corrupted_bytes_number - 1]
        right = corrupted_bytes_number - 1

print(first_blocking_end)

