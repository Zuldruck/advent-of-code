def galaxiesPositions(grid):
  galaxiesPositions = []
  for x in range(len(grid)):
    for y in range(len(grid[0])):
      if grid[x][y] == '#':
        galaxiesPositions.append((x, y))
  return galaxiesPositions

def countEmptyRowsAndColsBetweenPositions(grid, pos1, pos2):
  x1, y1 = pos1
  x2, y2 = pos2

  emptyRows = 0
  emptyCols = 0

  smallestX = min(x1, x2)
  biggestX = max(x1, x2)
  for x in range(smallestX + 1, biggestX):
    if not '#' in grid[x]:
      emptyRows += 1
  
  smallestY = min(y1, y2)
  biggestY = max(y1, y2)
  for y in range(smallestY + 1, biggestY):
    noGalaxy = True
    for x in range(len(grid)):
      if grid[x][y] == '#':
        noGalaxy = False
        break
    if noGalaxy:
      emptyCols += 1
  
  return emptyRows, emptyCols

with open('input.txt') as file:
  grid = file.read().split('\n')

  # PART 1
  multiplier = 2

  # PART 2
  multiplier = 1000000

  galaxiesPositions = galaxiesPositions(grid)

  s = 0
  for i in range(len(galaxiesPositions)):
    for j in range(i + 1, len(galaxiesPositions)):
      emptyRows, emptyCols = countEmptyRowsAndColsBetweenPositions(grid, galaxiesPositions[i], galaxiesPositions[j])
      distance = abs(galaxiesPositions[i][0] - galaxiesPositions[j][0]) + abs(galaxiesPositions[i][1] - galaxiesPositions[j][1]) + (emptyRows * (multiplier - 1)) + (emptyCols * (multiplier - 1))
      s += distance
  
  print(s)

