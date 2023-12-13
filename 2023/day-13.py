def getRowDifference(row1, row2):
  difference = 0
  for i in range(len(row1)):
    if row1[i] != row2[i]:
      difference += 1
  return difference

def findReflectionRow(pattern):
  for i in range(1, len(pattern)):
    reflection = True
    smudge = False
    for x in range(min(i, len(pattern) - i)):
      if pattern[i - x - 1] != pattern[i + x]:
        difference = getRowDifference(pattern[i - x - 1], pattern[i + x])
        if not allowSmudge or smudge or difference > 1:
          reflection = False
          break
        smudge = True
    if reflection and (not allowSmudge or smudge):
      return i
  return 0

def findReflectionCol(pattern):
  for j in range(1, len(pattern[0])):
    reflection = True
    smudge = False
    for x in range(min(j, len(pattern[0]) - j)):
      for i in range(len(pattern)):
        if pattern[i][j - x - 1] != pattern[i][j + x]:
          if not allowSmudge or smudge:
            reflection = False
            break
          smudge = True
      if not reflection:
        break
    if reflection and (not allowSmudge or smudge):
      return j
  return 0

with open('input.txt') as file:
  patterns = [pattern.split('\n') for pattern in file.read().split('\n\n')]
  
  # PART 1
  allowSmudge = False
  print(sum([findReflectionCol(pattern) for pattern in patterns]) + sum([findReflectionRow(pattern) * 100 for pattern in patterns]))

  # PART 2
  allowSmudge = True
  print(sum([findReflectionCol(pattern) for pattern in patterns]) + sum([findReflectionRow(pattern) * 100 for pattern in patterns]))
