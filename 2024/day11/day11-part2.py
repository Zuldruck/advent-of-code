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