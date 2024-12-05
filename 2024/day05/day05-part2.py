f = open("input.txt", "r")
text = f.read()
[rules, orderings] = map(lambda x: x.split('\n'), text.split('\n\n'))
rules = list(map(lambda x: list(map(int,x.split('|'))), rules))
orderings = list(map(lambda x: list(map(int,x.split(','))), orderings))

mustBeBeforePage = {}

for rule in rules:
  [pageA, pageB] = rule
  if pageB not in mustBeBeforePage:
    mustBeBeforePage[pageB] = {}
  mustBeBeforePage[pageB][pageA] = True

res = 0
for ordering in orderings:
  valid = True
  pagesBefore = []
  for page in ordering:
    pageValid = True
    invalidPageIndex = -1
    for idx, pageBefore in enumerate(pagesBefore):
      if page in mustBeBeforePage.get(pageBefore, {}):
        valid = False
        pageValid = False
        invalidPageIndex = idx
        break
    if pageValid:
      pagesBefore.append(page)
    else:
      pagesBefore.insert(invalidPageIndex, page)

  if not valid:
    middleValue = pagesBefore[len(pagesBefore) // 2]
    res += middleValue
    
print(res)
