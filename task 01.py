import random

def two_point_crossover(parent1, parent2):
    length = len(parent1)
    
    p1, p2 = sorted(random.sample(range(length), 2))
    
    
    child1 = parent1[:p1] + parent2[p1:p2] + parent1[p2:]
    child2 = parent2[:p1] + parent1[p1:p2] + parent2[p2:]
    
    return child1, child2, (p1, p2)


def run_generations(parent1, parent2, generations=5):
    for g in range(1, generations+1):
        child1, child2, crossover_points = two_point_crossover(parent1, parent2)
        print(f"Generation {g}:")
        print(f"  Parent1: {parent1}")
        print(f"  Parent2: {parent2}")
        print(f"  Crossover Points: {crossover_points}")
        print(f"  Child1: {child1}")
        print(f"  Child2: {child2}")
        print("-" * 40)
      
        parent1, parent2 = child1, child2


if __name__ == "__main__":
    
    p1 = input("Enter Parent 1 (binary chromosome): ")
    p2 = input("Enter Parent 2 (binary chromosome): ")
    
    
    if len(p1) != len(p2):
        print("Error: Parents must be the same length!")
    else:
        run_generations(p1, p2, generations=5)

# Example Input:
# Enter Parent 1 (binary chromosome): 110011001100
# Enter Parent 2 (binary chromosome): 001100110011