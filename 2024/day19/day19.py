f = open("input.txt", "r")
patterns, desired_designs = f.read().split('\n\n')
patterns = patterns.split(', ')
desired_designs = desired_designs.split('\n')

def design_is_possible(design, patterns):
    if design in patterns:
        return True
    for pattern in patterns:
        if not design.startswith(pattern):
            continue
        if design_is_possible(design[len(pattern):], patterns):
            return True
    return False
        
count = 0
for desired_design in desired_designs:
    if design_is_possible(desired_design, patterns):
        count += 1

print(count)