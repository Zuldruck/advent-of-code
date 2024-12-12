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

def get_area_from_region(pos, region, visited):
    if pos in visited or out_of_bounds(pos) or grid[pos[0]][pos[1]] != region:
        return 0
    visited.add(pos)
    sum_areas = 0
    for direction in directions:
        next_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
        next_area = get_area_from_region(next_pos, region, visited)
        sum_areas += next_area
    return 1 + sum_areas

def get_nb_sides_from_region(region_cells):
    nb_sides = 0
    upmost_cell = min(region_cells, key=lambda x: x[0])
    leftmost_cell = min(region_cells, key=lambda x: x[1])
    rightmost_cell = max(region_cells, key=lambda x: x[1])
    downmost_cell = max(region_cells, key=lambda x: x[0])
    
    # Check from up to down
    side_cells = set()
    out_of_region = True
    j = leftmost_cell[1]
    while j <= rightmost_cell[1] + 1:
        i = upmost_cell[0]
        while i <= downmost_cell[0] + 1:
            if out_of_region and (i, j) in region_cells:
                out_of_region = False
                if (i - 1, j, "UP") not in side_cells:
                    nb_sides += 1
                    # Add all the cells of that side to the side_cells set
                    y = j
                    while y <= rightmost_cell[1] and (i, y) in region_cells and (i - 1, y) not in region_cells:
                        side_cells.add((i - 1, y, "UP"))
                        y += 1
            elif not out_of_region and (i, j) not in region_cells:
                out_of_region = True
                if (i, j, "DOWN") not in side_cells:
                    nb_sides += 1
                    # Add all the cells of that side to the side_cells set
                    y = j
                    while y <= rightmost_cell[1] and (i, y) not in region_cells and (i - 1, y) in region_cells:
                        side_cells.add((i, y, "DOWN"))
                        y += 1
            i += 1
        j += 1

    # Check from left to right
    side_cells = set()
    out_of_region = True
    i = upmost_cell[0]
    while i <= downmost_cell[0] + 1:
        j = leftmost_cell[1]
        while j <= rightmost_cell[1] + 1:
            if out_of_region and (i, j) in region_cells:
                out_of_region = False
                if (i, j - 1, "LEFT") not in side_cells:
                    nb_sides += 1
                    # Add all the cells of that side to the side_cells set
                    x = i
                    while x <= downmost_cell[0] and (x, j) in region_cells and (x, j - 1) not in region_cells:
                        side_cells.add((x, j - 1, "LEFT"))
                        x += 1
            elif not out_of_region and (i, j) not in region_cells:
                out_of_region = True
                if (i, j, "RIGHT") not in side_cells:
                    nb_sides += 1
                    # Add all the cells of that side to the side_cells set
                    x = i
                    while x <= downmost_cell[0] and (x, j) not in region_cells and (x, j - 1) in region_cells:
                        side_cells.add((x, j, "RIGHT"))
                        x += 1
            j += 1
        i += 1
    
    return nb_sides


total_visited = set()
total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) in total_visited:
            continue
        region_cells = set()
        area = get_area_from_region((i, j), grid[i][j], region_cells)
        total_visited = total_visited.union(region_cells)
        nb_sides = get_nb_sides_from_region(region_cells)
        total += area * nb_sides

print(total)
