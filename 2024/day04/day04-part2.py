f = open("input.txt", "r")
grid = [line.strip() for line in f.readlines()]

res = 0

for i in range(len(grid) - 2):
    for j in range(len(grid[0]) - 2):
        # Diagonal Down Right
        diagonals = []
        letters = ""
        x = i
        y = j
        while x < i + 3 and y < j + 3:
            letters += grid[x][y]
            x += 1
            y += 1
        diagonals.append(letters)

        # Diagonal Down Left
        letters = ""
        x = i
        y = j + 2
        while x < i + 3 and y > j - 1:
            letters += grid[x][y]
            x += 1
            y -= 1
        diagonals.append(letters)

        # Diagonal Up Right
        letters = ""
        x = i + 2
        y = j
        while x > i - 1 and y < j + 3:
            letters += grid[x][y]
            x -= 1
            y += 1
        diagonals.append(letters)

        # Diagonal Up Left
        letters = ""
        x = i + 2
        y = j + 2
        while x > i - 1 and y > j - 1:
            letters += grid[x][y]
            x -= 1
            y -= 1
        diagonals.append(letters)

        if len([d for d in diagonals if d == "MAS"]) == 2:
            res += 1

print(res)
