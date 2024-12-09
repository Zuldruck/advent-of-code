f = open("input.txt", "r")
grid = [line.strip() for line in f.readlines()]

def out_of_bounds(pos):
    return pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0])

antennas = {}

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.':
            if grid[i][j] not in antennas:
                antennas[grid[i][j]] = [(i, j)]
            else:
                antennas[grid[i][j]].append((i, j))

pairs = []

for key in antennas:
    for i in range(len(antennas[key])):
        for j in range(i + 1, len(antennas[key])):
            pairs.append((antennas[key][i], antennas[key][j]))

antiNodes = set()
for nodeA, nodeB in pairs:
    distanceFromAToB = (nodeB[0] - nodeA[0], nodeB[1] - nodeA[1])
    distanceFromBToA = (nodeA[0] - nodeB[0], nodeA[1] - nodeB[1])
    antiNodeA = (nodeB[0] + distanceFromAToB[0], nodeB[1] + distanceFromAToB[1])
    antiNodeB = (nodeA[0] + distanceFromBToA[0], nodeA[1] + distanceFromBToA[1])
    if not out_of_bounds(antiNodeA):
        antiNodes.add(antiNodeA)
    if not out_of_bounds(antiNodeB):
        antiNodes.add(antiNodeB)

print(len(antiNodes))
