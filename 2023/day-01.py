def replaceSpelledDigits(line):
  line = line.replace('one', 'one1one')
  line = line.replace('two', 'two2two')
  line = line.replace('three', 'three3three')
  line = line.replace('four', 'four4four')
  line = line.replace('five', 'five5five')
  line = line.replace('six', 'six6six')
  line = line.replace('seven', 'seven7seven')
  line = line.replace('eight', 'eight8eight')
  line = line.replace('nine', 'nine9nine')
  return line

s = 0
while 1:
  line = ''
  try:
    line = input()
  except EOFError:
    break
  line = replaceSpelledDigits(line) # PART 2
  # Filter only digits
  l = list(filter(lambda x: x.isdigit(), line))
  n = int(l[0]) * 10 + int(l[-1])
  s += n

print(s)
