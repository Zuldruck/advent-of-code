f = open("input.txt", "r")
stones = [int(d) for d in f.read().split()]

for _ in range(25):
    newStones = []
    for i in range(len(stones)):
        lenNumber = len(str(stones[i]))
        if stones[i] == 0:
            newStones.append(1)
        elif lenNumber % 2 == 0:
            newStones.append(int(str(stones[i])[:lenNumber // 2]))
            newStones.append(int(str(stones[i])[lenNumber // 2:]))
        else:
            newStones.append(stones[i] * 2024)
    stones = newStones

print(len(stones))