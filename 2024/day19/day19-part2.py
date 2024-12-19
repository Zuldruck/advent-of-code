f = open("input.txt", "r")
patterns, desired_designs = f.read().split('\n\n')
patterns = patterns.split(', ')
desired_designs = desired_designs.split('\n')

design_possible_ways_cache = {
    '': 0
}

def design_possible_ways(design, patterns):
    possible_ways = 0
    if design in design_possible_ways_cache:
        return design_possible_ways_cache[design]
    for pattern in patterns:
        if not design.startswith(pattern):
            continue
        possible_ways += design_possible_ways(design[len(pattern):], patterns)
    if design in patterns:
        possible_ways += 1
    design_possible_ways_cache[design] = possible_ways
    return possible_ways

count = 0
for idx, desired_design in enumerate(desired_designs):
    count += design_possible_ways(desired_design, patterns)

print(count)
