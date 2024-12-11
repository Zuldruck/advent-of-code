f = open("input.txt", "r")
stones = [int(d) for d in f.read().split()]

for _ in range(10):
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

stones_count = {}
for stone in stones:
    if stone in stones_count:
        stones_count[stone] += 1
    else:
        stones_count[stone] = 1

print(len(stones))