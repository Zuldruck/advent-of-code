def isSymbol(c):
  return not c.isdigit() and c != '.'

aroundCharMatrix = [
  [-1, 0], # Up
  [-1, 1], # Up-Right
  [0, 1], # Right
  [1, 1], # Down-Right
  [1, 0], # Down
  [1, -1], # Down-Left
  [0, -1], # Left
  [-1, -1] # Up-Left
]

with open('input.txt') as file:
  lines = file.readlines()
  lines = list(map(lambda x: x.strip(), lines))

  partNumbersSum = 0
  adjacentStarNumbers = [[[] for _ in range(len(lines[i]))] for i in range(len(lines))]
  for i in range(len(lines)):
    j = 0
    while j < len(lines[i]):
      n = 0
      isPartNumber = False
      isNumber = False
      symbols = []
      while j < len(lines[i]) and lines[i][j].isdigit():
        isNumber = True
        for k in range(len(aroundCharMatrix)):
          if i + aroundCharMatrix[k][0] >= 0 and i + aroundCharMatrix[k][0] < len(lines) and j + aroundCharMatrix[k][1] >= 0 and j + aroundCharMatrix[k][1] < len(lines[i]):
            if isSymbol(lines[i + aroundCharMatrix[k][0]][j + aroundCharMatrix[k][1]]):
              symbols.append((i + aroundCharMatrix[k][0], j + aroundCharMatrix[k][1], lines[i + aroundCharMatrix[k][0]][j + aroundCharMatrix[k][1]]))
              isPartNumber = True
              break
        n = n * 10 + int(lines[i][j])
        j += 1
      
      if not isNumber:
        j += 1

      if isPartNumber:
        # PART 1
        partNumbersSum += n

        # PART 2
        for k in range(len(symbols)):
          if symbols[k][2] == '*':
            adjacentStarNumbers[symbols[k][0]][symbols[k][1]].append(n)
            break
  
  # PART 2
  gearsSum = 0
  for i in range(len(adjacentStarNumbers)):
    for j in range(len(adjacentStarNumbers[i])):
      if len(adjacentStarNumbers[i][j]) == 2:
        print(adjacentStarNumbers[i][j])
        gearsSum += adjacentStarNumbers[i][j][0] * adjacentStarNumbers[i][j][1]

  print(gearsSum)
  print(partNumbersSum)
