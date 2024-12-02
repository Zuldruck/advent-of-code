f = open("input.txt", "r")
reports = [[int(level) for level in line.split()] for line in f.readlines()]

safe_reports = 0
for report in reports:
  all_possible_levels = [report]
  for i in range(len(report)):
    possible_levels = []
    for j in range(len(report)):
      if i != j:
        possible_levels.append(report[j])
    all_possible_levels.append(possible_levels)
  
  for possible_levels in all_possible_levels:
    increasing = False
    decreasing = False
    notSafe = False
    for level1, level2 in zip(possible_levels, possible_levels[1:]):
      diff = level2 - level1
      if diff > 0:
        if decreasing or diff > 3:
          notSafe = True
        increasing = True
      elif diff < 0:
        if increasing or diff < -3:
          notSafe = True
        decreasing = True
      else:
        notSafe = True
    if not notSafe:
      safe_reports += 1
      break
    
print(safe_reports)
