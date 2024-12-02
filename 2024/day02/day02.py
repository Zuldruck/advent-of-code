f = open("input.txt", "r")
reports = [[int(level) for level in line.split()] for line in f.readlines()]

safe_reports = 0
for report in reports:
  increasing = False
  decreasing = False
  notSafe = False
  for level1, level2 in zip(report, report[1:]):
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

print(safe_reports)
