f = open("input.txt", "r")
grid = [line.strip() for line in f.readlines()]

res = 0

# RIGHT
for i in range(len(grid)):
    res += grid[i].count("XMAS")

# DOWN
for j in range(len(grid[0])):
    res += "".join([grid[i][j] for i in range(len(grid))]).count("XMAS")

# UP
for j in range(len(grid[0])):
    res += "".join([grid[i][j] for i in range(len(grid) - 1, -1, -1)]).count("XMAS")

# LEFT
for i in range(len(grid)):
    res += "".join([grid[i][j] for j in range(len(grid[i]) - 1, -1, -1)]).count("XMAS")

# DOWN-RIGHT
for j in range(len(grid[0]) -1, -1, -1):
    x = 0
    y = j
    letters = ""
    while x < len(grid) and y < len(grid[0]):
        letters += grid[x][y]
        x += 1
        y += 1
    res += letters.count("XMAS")
for i in range(1, len(grid)):
    x = i
    y = 0
    letters = ""
    while x < len(grid) and y < len(grid[0]):
        letters += grid[x][y]
        x += 1
        y += 1
    res += letters.count("XMAS")

# DOWN-LEFT
for j in range(len(grid[0])):
    x = 0
    y = j
    letters = ""
    while x < len(grid) and y >= 0:
        letters += grid[x][y]
        x += 1
        y -= 1
    res += letters.count("XMAS")
for i in range(1, len(grid)):
    x = i
    y = len(grid[0]) - 1
    letters = ""
    while x < len(grid) and y >= 0:
        letters += grid[x][y]
        x += 1
        y -= 1
    res += letters.count("XMAS")

# UP-RIGHT
for j in range(len(grid[0]) - 1, -1, -1):
    x = len(grid) - 1
    y = j
    letters = ""
    while x >= 0 and y < len(grid[0]):
        letters += grid[x][y]
        x -= 1
        y += 1
    res += letters.count("XMAS")
for i in range(len(grid) - 2, -1, -1):
    x = i
    y = 0
    letters = ""
    while x >= 0 and y < len(grid[0]):
        letters += grid[x][y]
        x -= 1
        y += 1
    res += letters.count("XMAS")

# UP-LEFT
for j in range(len(grid[0])):
    x = len(grid) - 1
    y = j
    letters = ""
    while x >= 0 and y >= 0:
        letters += grid[x][y]
        x -= 1
        y -= 1
    res += letters.count("XMAS")
for i in range(len(grid) - 2, -1, -1):
    x = i
    y = len(grid[0]) - 1
    letters = ""
    while x >= 0 and y >= 0:
        letters += grid[x][y]
        x -= 1
        y -= 1
    res += letters.count("XMAS")

print(res)
