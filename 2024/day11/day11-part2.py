f = open("input.txt", "r")
stones = [int(d) for d in f.read().split()]

# compute the length of the number without converting it to a string
def len_number(n):
    if n == 0:
        return 1
    len = 0
    while n > 0:
        len += 1
        n //= 10
    return len

# compute the left part of the number without converting it to a string
def left_part(n, len):
    return n // 10**(len // 2)

# compute the right part of the number without converting it to a string
def right_part(n, len):
    return n % 10**(len // 2)

stones_nb = len(stones)
zero_stones = 0
even_stone_sizes = 0
else_stones = 0

for i in range(stones_nb):
    if stones[i] == 0:
        zero_stones += 1
        continue
    lenNumber = len_number(stones[i])
    if lenNumber % 2 == 0:
        even_stone_sizes += 1
    else:
        else_stones += 1

steps = [
    [[1], [2024], [20, 24], [2, 0, 2, 4]],
    [[2024], [20, 24], [2, 0, 2, 4]],
    [[4048], [40, 48], [4, 0, 4, 8]],
    [[6072], [60, 72], [6, 0, 7, 2]],
    [[8096], [80, 96], [8, 0, 9, 6]],
    [[10120], [20482880], [2048, 2880], [20, 48, 28, 80], [2, 0, 4, 8, 2, 8, 8, 0]],
    [[12144], [24579456], [2457, 9456], [24, 57, 94, 56], [2, 4, 5, 7, 9, 4, 5, 6]],
    [[14168], [28676032], [2867, 6032], [28, 67, 60, 32], [2, 8, 6, 7, 6, 0, 3, 2]],
    [[16192], [32772508], [3277, 2608], [32, 77, 26, 8], [3, 2, 7, 7, 2, 6, 16192]],
    [[18216], [36869184], [3686, 9184], [36, 86, 91, 84], [3, 6, 8, 6, 9, 1, 8, 4]],
]

def new_stones(stone):
    if stone == 0:
        return { 1: 1 }
    lenNumber = len_number(stone)
    if lenNumber % 2 == 0:
        left = left_part(stone, lenNumber)
        right = right_part(stone, lenNumber)
        if left == right:
            return { left: 2 }
        return { left: 1, right: 1 }
    newStone = stone * 2024
    return { newStone: 1 }


stones_count = {}
for stone in stones:
    if stone in stones_count:
        stones_count[stone] += 1
    else:
        stones_count[stone] = 1

step_stone = {}
for _ in range(75):
    next_stones_count = {}
    for (stone, count) in stones_count.items():
        if stone in step_stone:
            next_stones = step_stone[stone]
            for (next_stone, next_stone_count) in next_stones.items():
                if next_stone in next_stones_count:
                    next_stones_count[next_stone] += next_stone_count * count
                else:
                    next_stones_count[next_stone] = next_stone_count * count
        else:
            next_stones = new_stones(stone)
            step_stone[stone] = next_stones
            for (next_stone, next_stone_count) in next_stones.items():
                if next_stone in next_stones_count:
                    next_stones_count[next_stone] += next_stone_count * count
                else:
                    next_stones_count[next_stone] = next_stone_count * count
    stones_count = next_stones_count

print(sum(stones_count.values()))