import re, random

f = open("input.txt", "r")
groups = re.search(r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: (.+)", f.read()).groups()
_, reg_b, reg_c = map(int, groups[:3])
program = list(map(int, groups[3].split(",")))

desired_output = [2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0]
POPULATION_SIZE = 200

def execute_program(reg_a):
  pointer = 0
  reg_b = 0
  reg_c = 0
  output = []
  while pointer < len(program):
      combos = {
          0: 0,
          1: 1,
          2: 2,
          3: 3,
          4: reg_a,
          5: reg_b,
          6: reg_c,
      }
      instruction = program[pointer]
      operand = program[pointer + 1]
      combo = combos[operand] if operand != 7 else None
      jump = None
      if instruction == 0:
          reg_a = int(reg_a / (2 ** combo))
      elif instruction == 1:
          reg_b ^= operand
      elif instruction == 2:
          reg_b = combo % 8
      elif instruction == 3 and reg_a != 0:
          jump = operand
      elif instruction == 4:
          reg_b ^= reg_c
      elif instruction == 5:
          output.append(combo % 8)
      elif instruction == 6:
          reg_b = int(reg_a / (2 ** combo))
      elif instruction == 7:
          reg_c = int(reg_a / (2 ** combo))
      pointer = jump if jump is not None else pointer + 2
  return output

def fitness(candidate):
    value, output = candidate
    if len(output) != len(desired_output):
        return 0
    score = 0
    for i in range(len(output)):
        digit = output[i]
        desired_digit = desired_output[i]
        if digit == desired_digit:
            score += 1
    # if score == len(desired_output): add to the score something in order to find the lowest value
    if score == len(desired_output):
        score += 281500000620880 - value
    return score
  
def initial_population(size = POPULATION_SIZE):
    lowest  = 35184307562088
    highest = 281500000620880
    diff = highest - lowest
    population = []
    
    for i in range(size):
        value = lowest + int(i * diff / 100)
        output = execute_program(value)
        population.append((value, output))
    return population

def tournament(population, population_fitness, k):
    best_candidate = None
    best_fitness = None
    for _ in range(k):
        candidate_idx = random.randint(0, len(population) - 1)
        candidate = population[candidate_idx]
        candidate_fitness = population_fitness[candidate_idx]
        if best_candidate == None:
            best_candidate = candidate
            best_fitness = candidate_fitness
        else:
            best_candidate = best_candidate if best_fitness >= candidate_fitness else candidate
            best_fitness = best_fitness if best_fitness >= candidate_fitness else candidate_fitness
    return best_candidate

def select_parents(population, population_fitness, num_parents, k = POPULATION_SIZE // 20):
    parents = []
    for _ in range(num_parents):
        parent = tournament(population, population_fitness, k)
        parents.append(parent)
    random.shuffle(parents)
    return parents

def perform_cross_over(population, population_fitness):
    new_population = []
    parents = select_parents(population, population_fitness, POPULATION_SIZE)
    pairs = [(parents[i], parents[i + 1]) for i in range(0, len(parents), 2)]
    pairs.append((parents[-1], parents[0]))
    for parent1, parent2 in pairs:
        parent1_genetic_representation = bin(parent1[0])[2:]
        parent2_genetic_representation = bin(parent2[0])[2:]
        crossover_point = random.randint(0, len(parent1_genetic_representation) - 1)
        child1_genetic_representation = parent1_genetic_representation[:crossover_point] + parent2_genetic_representation[crossover_point:]
        child2_genetic_representation = parent2_genetic_representation[:crossover_point] + parent1_genetic_representation[crossover_point:]
        child1 = int(child1_genetic_representation, 2)
        child2 = int(child2_genetic_representation, 2)
        new_population.append((child1, execute_program(child1)))
        new_population.append((child2, execute_program(child2)))
    return new_population

def perform_mutation(population, mutation_rate = 0.5):
    for i in range(len(population)):
        if random.random() < mutation_rate:
            candidate = population[i]
            candidate_genetic_representation = bin(candidate[0])[2:]
            mutation_point = random.randint(0, len(candidate_genetic_representation) - 1)
            mutated_candidate_genetic_representation = candidate_genetic_representation[:mutation_point] + str(int(not int(candidate_genetic_representation[mutation_point]))) + candidate_genetic_representation[mutation_point + 1:]
            mutated_candidate = int(mutated_candidate_genetic_representation, 2)
            population[i] = (mutated_candidate, execute_program(mutated_candidate))

population = initial_population() + [(37222278756852, desired_output), (37222278740468, desired_output), (37222274481652, desired_output)]
population_fitness = [fitness(candidate) for candidate in population]
for i in range(10000000):
    print("Generation", i)
    max_fitness = max(population_fitness)
    print("Max fitness:", max_fitness)
    best_candidate = population[population_fitness.index(max_fitness)]
    print("Best candidate:", best_candidate)
    population = perform_cross_over(population, population_fitness)
    perform_mutation(population)
    population_fitness = [fitness(candidate) for candidate in population]
print("Done!")
