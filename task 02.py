import random

# Function to evaluate fitness: f(x) = 27x - x^2
def fitness(chromosome):
    x = int(chromosome, 2)  # decode binary to integer
    return 27 * x - x**2

# Generate a random 5-bit chromosome
def random_chromosome():
    return ''.join(random.choice("01") for _ in range(5))

# Roulette Wheel Selection
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    if total_fitness == 0:
        return random.choice(population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for chrom, fit in zip(population, fitness_values):
        current += fit
        if current >= pick:
            return chrom
    return population[-1]

# Two-point crossover
def two_point_crossover(parent1, parent2):
    p1, p2 = sorted(random.sample(range(5), 2))
    child1 = parent1[:p1] + parent2[p1:p2] + parent1[p2:]
    child2 = parent2[:p1] + parent1[p1:p2] + parent2[p2:]
    return child1, child2

# Mutation: flip a random bit
def mutate(chromosome, mutation_rate=0.1):
    chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = '1' if chromosome[i] == '0' else '0'
    return ''.join(chromosome)

# Genetic Algorithm with 4 initial chromosomes
def genetic_algorithm(pop_size=4, generations=10, mutation_rate=0.1):
    # Initial population of 4 random chromosomes
    population = [random_chromosome() for _ in range(pop_size)]
    print("Initial Population:")
    for chrom in population:
        print(f"  {chrom} (x={int(chrom,2)}, f(x)={fitness(chrom)})")
    print("-" * 40)

    for g in range(1, generations + 1):
        fitness_values = [fitness(c) for c in population]

        # Selection (roulette wheel) - pick 2 parents
        parent1 = roulette_wheel_selection(population, fitness_values)
        parent2 = roulette_wheel_selection(population, fitness_values)

        # Crossover
        child1, child2 = two_point_crossover(parent1, parent2)

        # Mutation
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)

        # Replace worst 2 chromosomes with new children
        population += [child1, child2]
        population.sort(key=lambda c: fitness(c), reverse=True)
        population = population[:pop_size]

        # Print progress
        print(f"Generation {g}:")
        for chrom in population:
            print(f"  {chrom} (x={int(chrom,2)}, f(x)={fitness(chrom)})")
        print("-" * 40)

    # Final best solution
    best = population[0]
    print("Final Best Solution:")
    print(f"Chromosome: {best}")
    print(f"x = {int(best,2)}")
    print(f"f(x) = {fitness(best)}")

# --- Run GA ---
genetic_algorithm()
