def expandUniverse(grid):
  rowsPositionToAdd = [idx for idx, row in enumerate(grid) if not '#' in row]
  columnsPositionToAdd = []

  for y in range(len(grid[0])):
    noGalaxy = True
    for x in range(len(grid)):
      if grid[x][y] == '#':
        noGalaxy = False
        break
    if noGalaxy:
      columnsPositionToAdd.append(y)
  
  # Add empty rows and columns where needed
  addedRows = 0
  for row in rowsPositionToAdd:
    grid.insert(row + addedRows, '.' * len(grid[0]))
    addedRows += 1
  for x in range(len(grid)):
    addedChars = 0
    for column in columnsPositionToAdd:
      grid[x] = grid[x][:column + addedChars] + '.' + grid[x][column + addedChars:]
      addedChars += 1
  
  return grid

def galaxiesPositions(grid):
  galaxiesPositions = []
  for x in range(len(grid)):
    for y in range(len(grid[0])):
      if grid[x][y] == '#':
        galaxiesPositions.append((x, y))
  return galaxiesPositions

with open('input.txt') as file:
  grid = file.read().split('\n')

  # PART 1
  grid = expandUniverse(grid)
  galaxiesPositions = galaxiesPositions(grid)

  s = 0
  for i in range(len(galaxiesPositions)):
    for j in range(i + 1, len(galaxiesPositions)):
      distance = abs(galaxiesPositions[i][0] - galaxiesPositions[j][0]) + abs(galaxiesPositions[i][1] - galaxiesPositions[j][1])
      s += distance
  
  print(s)

