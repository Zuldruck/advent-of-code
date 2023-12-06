import re

def pairwise(iterable):
  a = iter(iterable)
  return zip(a, a)

# Split ranges if they overlap a mappingLine
def splitRanges(ranges, mapping):
  splitted = True
  while splitted:
    newRanges = []
    splitted = False
    for (rangeStart, rangeEnd) in ranges:
      splittedRange = False
      for mappingLine in mapping:
        [_, sourceStart, length] = mappingLine
        if (rangeStart >= sourceStart and rangeEnd < sourceStart + length) \
        or (rangeStart < sourceStart and rangeEnd < sourceStart) \
        or (rangeStart >= sourceStart + length and rangeEnd >= sourceStart + length):
          # print('case 1')
          pass
        elif rangeStart < sourceStart and rangeEnd >= sourceStart + length:
          # print('case 2')
          newRanges.append((rangeStart, sourceStart - 1))
          newRanges.append((sourceStart, sourceStart + length - 1))
          newRanges.append((sourceStart + length, rangeEnd))
          splitted = True
          splittedRange = True
          break
        elif rangeStart < sourceStart and rangeEnd >= sourceStart:
          # print('case 3')
          newRanges.append((rangeStart, sourceStart - 1))
          newRanges.append((sourceStart, rangeEnd))
          splitted = True
          splittedRange = True
          break
        elif rangeStart >= sourceStart and rangeEnd >= sourceStart + length:
          # print('case 4')
          newRanges.append((rangeStart, sourceStart + length - 1))
          newRanges.append((sourceStart + length, rangeEnd))
          splitted = True
          splittedRange = True
          break
  
      if not splittedRange:
        newRanges.append((rangeStart, rangeEnd))
    
    ranges = newRanges
  
  return ranges

# Check if ranges are contiguous and merge if they wont overlap a mappingLine
def mergeRanges(ranges, mapping):
  merged = True
  while merged:
    merged = False
    for mappingLine in mapping:
      [_, sourceStart, length] = mappingLine
      for i in range(len(ranges) - 1):
        (rangeStart, rangeEnd) = ranges[i]
        (rangeStart_, rangeEnd_) = ranges[i + 1]
        if rangeEnd + 1 == rangeStart_ and rangeEnd < sourceStart and rangeEnd_ < sourceStart:
          ranges[i] = (rangeStart, rangeEnd_)
          del ranges[i + 1]
          merged = True
          break
      if merged:
        break
  return ranges

def processMapping(ranges, mapping):
  for i in range(len(ranges)):
    (rangeStart, rangeEnd) = ranges[i]
    for mappingLine in mapping:
      [destinationStart, sourceStart, length] = mappingLine
      if rangeStart >= sourceStart and rangeEnd < sourceStart + length:
        ranges[i] = (destinationStart + rangeStart - sourceStart, destinationStart + rangeEnd - sourceStart)
        break
  return ranges

def processMappings(ranges, mappings):
  for mapping in mappings:
    ranges = mergeRanges(ranges, mapping)
    ranges = splitRanges(ranges, mapping)
    ranges = processMapping(ranges, mapping)
    ranges.sort(key=lambda x: x[0])
  return ranges

with open('input.txt') as file:
  txt = file.read()
  sections = txt.split('\n\n')
  seeds = list(map(lambda x: int(x), re.findall(r'\d+', sections[0])))
  mappings = [list(map(lambda x: list(map(lambda y: int(y), x.split())), section.split('\n')[1:])) for section in sections[1:]]
  for mapping in mappings:
    mapping.sort(key=lambda x: x[1])
  
  # Part 1
  tmpSeeds = seeds
  tmpSeeds = sorted(tmpSeeds)
  tmpSeeds = [(seed, seed) for seed in tmpSeeds]
  locations = processMappings(tmpSeeds, mappings)
  print(locations[0][0])

  # Part 2
  seeds = [(seed, seed + length - 1) for (seed, length) in pairwise(seeds)]
  seeds.sort(key=lambda x: x[0])
  locations = processMappings(seeds, mappings)
  print(locations[0][0])

