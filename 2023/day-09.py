def getDifferences(line):
  differences = []
  for i in range(len(line) - 1):
    differences.append(line[i + 1] - line[i])
  return differences

def nextValue(line):
  if len(line) == 0:
    return 0
  if len(line) == 1:
    return line[0]
  allZeros = True
  for n in line:
    if n != 0:
      allZeros = False
      break
  if allZeros:
    return 0
  differences = getDifferences(line)
  return line[-1] + nextValue(differences)

def prevValue(line):
  if len(line) == 0:
    return 0
  if len(line) == 1:
    return line[0]
  allZeros = True
  for n in line:
    if n != 0:
      allZeros = False
      break
  if allZeros:
    return 0
  differences = getDifferences(line)
  return line[0] - prevValue(differences)

with open('input.txt') as file:
  lines = file.read().split('\n')
  lines = [[int(x) for x in line.split(' ')] for line in lines]

  # PART 1
  print(sum([nextValue(line) for line in lines]))

  # PART 2
  print(sum([prevValue(line) for line in lines]))
