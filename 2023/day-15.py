import re

def getSequenceHash(sequence):
  _hash = 0
  for c in sequence:
    _hash += ord(c)
    _hash = (_hash * 17) % 256
  return _hash

def findIndexOf(lenses, label):
  for i in range(len(lenses)):
    if lenses[i]['label'] == label:
      return i
  return None

def removeLens(lenses, label):
  for i in range(len(lenses)):
    if lenses[i]['label'] == label:
      del lenses[i]
      break

with open('input.txt') as file:
  steps = file.read().strip().split(',')
  
  # PART 1
  res = sum([getSequenceHash(step) for step in steps])
  print(res)

  # PART 2
  boxes = [[] for _ in range(256)]
  for step in steps:
    splittedStep = re.split('-|=', step)
    label = splittedStep[0]
    focalLength = splittedStep[1] if len(splittedStep) > 1 and splittedStep[1] != '' else None
    box = boxes[getSequenceHash(label)]
    if focalLength is not None:
      labelIndex = findIndexOf(box, label)
      if labelIndex is None: box.append({ 'focalLength': int(focalLength), 'label': label })
      else: box[labelIndex]['focalLength'] = int(focalLength)
    else:
      removeLens(box, label)
  print(sum([sum([(1 + boxIdx) * (1 + lensIdx) * lens['focalLength'] for lensIdx, lens in enumerate(box)]) for boxIdx, box in enumerate(boxes)]))
