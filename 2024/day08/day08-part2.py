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
    antiNodes.add(nodeA)
    antiNodes.add(nodeB)
    originalNodeA = nodeA
    originalNodeB = nodeB
    nodeACopy = nodeA
    nodeBCopy = nodeB
    while not out_of_bounds(nodeACopy) and not out_of_bounds(nodeBCopy):
        distanceFromAToB = (nodeBCopy[0] - nodeACopy[0], nodeBCopy[1] - nodeACopy[1])
        antiNodeA = (nodeBCopy[0] + distanceFromAToB[0], nodeBCopy[1] + distanceFromAToB[1])
        if not out_of_bounds(antiNodeA):
            antiNodes.add(antiNodeA)
        nodeACopy = nodeBCopy
        nodeBCopy = antiNodeA
    nodeACopy = originalNodeA
    nodeBCopy = originalNodeB
    while not out_of_bounds(nodeACopy) and not out_of_bounds(nodeBCopy):
        distanceFromBToA = (nodeACopy[0] - nodeBCopy[0], nodeACopy[1] - nodeBCopy[1])
        antiNodeB = (nodeACopy[0] + distanceFromBToA[0], nodeACopy[1] + distanceFromBToA[1])
        if not out_of_bounds(antiNodeB):
            antiNodes.add(antiNodeB)
        nodeBCopy = nodeACopy
        nodeACopy = antiNodeB

print(len(antiNodes))
