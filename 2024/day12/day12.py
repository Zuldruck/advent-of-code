f = open("input.txt", "r")
grid = [line.strip() for line in f.readlines()]

def out_of_bounds(pos):
    return pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0])

directions = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "RIGHT": (0, 1),
    "LEFT": (0, -1),
}

def get_area_and_perimeter_from_region(pos, region, visited):
    if pos in visited or out_of_bounds(pos) or grid[pos[0]][pos[1]] != region:
        return 0, 0
    visited.add(pos)
    perimeter = 0
    sum_areas = 0
    sum_perimeters = 0
    for direction in directions:
        next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
        next_area, next_perimeter = get_area_and_perimeter_from_region(next_pos, region, visited)
        sum_areas += next_area
        sum_perimeters += next_perimeter
        if next_pos not in visited and (out_of_bounds(next_pos) or grid[next_pos[0]][next_pos[1]] != region):
            perimeter += 1
    return 1 + sum_areas, perimeter + sum_perimeters

total_visited = set()
total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) in total_visited:
            continue
        region_visited = set()
        area, perimeter = get_area_and_perimeter_from_region((i, j), grid[i][j], region_visited)
        total += area * perimeter
        total_visited = total_visited.union(region_visited)

print(total)
