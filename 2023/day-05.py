import re

def pairwise(iterable):
  a = iter(iterable)
  return zip(a, a)

def processMapping(toFind, mapping):
  for mappingLine in mapping:
    [destinationStart, sourceStart, length] = mappingLine
    if toFind >= sourceStart and toFind < sourceStart + length:
      return destinationStart + toFind - sourceStart
  return toFind

def processMappings(toFind, mappings):
  for mapping in mappings:
    toFind = processMapping(toFind, mapping)
  return toFind

with open('input.txt') as file:
  txt = file.read()
  sections = txt.split('\n\n')
  seeds = list(map(lambda x: int(x), re.findall(r'\d+', sections[0])))
  mappings = [list(map(lambda x: list(map(lambda y: int(y), x.split())), section.split('\n')[1:])) for section in sections[1:]]
  
  # Part 1
  destinations = [processMappings(seed, mappings) for seed in seeds]
  print(min(destinations))

  # Part 2
  seeds_ = set()
  for startSeed, length in pairwise(seeds):
    for i in range(length):
      seeds_.add(startSeed + i)
  seeds = seeds_
  destinations = [processMappings(seed, mappings) for seed in seeds]
  print(min(destinations))
