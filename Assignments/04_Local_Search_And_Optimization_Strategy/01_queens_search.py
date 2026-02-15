import random

# ============================================
# HELPER FUNCTIONS FOR 8-QUEENS PROBLEM
# ============================================


def calculate_heuristic(state):
    """Calculate number of non-attacking pairs (max 28)"""
    attacks = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j]:  # Same row
                attacks += 1
            elif abs(state[i] - state[j]) == abs(i - j):  # Same diagonal
                attacks += 1
    return 28 - attacks  # Non-attacking pairs


def generate_random_state():
    """Generate a random 8-queens state"""
    return [random.randint(1, 8) for _ in range(8)]


def generate_successors(state):
    """Generate all 56 successors by changing one column position"""
    successors = []
    for col in range(8):
        current_row = state[col]
        for new_row in range(1, 9):
            if new_row != current_row:
                new_state = state.copy()
                new_state[col] = new_row
                successors.append(new_state)
    return successors


def print_state(state, value=None):
    """Print state nicely"""
    if value:
        print(f"State: {state} Value: {value}")
    else:
        print(f"State: {state}")


# ============================================
# HILL-CLIMBING VARIANTS
# ============================================


# 1. Standard Hill-Climbing
def hill_climbing(initial_state, threshold=28, max_iterations=100):
    print("\n=== STANDARD HILL-CLIMBING ===")
    current = initial_state.copy()
    current_value = calculate_heuristic(current)

    print(f"Initial state: {current} Value: {current_value}")

    iteration = 1
    while iteration <= max_iterations and current_value < threshold:
        successors = generate_successors(current)
        best_successor = None
        best_value = current_value

        for succ in successors:
            val = calculate_heuristic(succ)
            if val > best_value:
                best_value = val
                best_successor = succ

        if best_successor and best_value > current_value:
            current = best_successor
            current_value = best_value
            print(f"Iteration {iteration}: {current} Value: {current_value}")
        else:
            print(f"Stuck at local maximum: {current} Value: {current_value}")
            break

        iteration += 1

    if current_value >= threshold:
        print(f"Solution found! {current} Value: {current_value}")
    else:
        print(f"Failed to reach threshold. Best: {current} Value: {current_value}")

    return current, current_value


# 2. Random Restart Hill-Climbing
def random_restart_hill_climbing(threshold=28, max_restarts=10):
    print("\n=== RANDOM RESTART HILL-CLIMBING ===")

    best_overall = None
    best_value = 0

    for restart in range(max_restarts):
        print(f"\nRestart #{restart+1}")
        initial = generate_random_state()
        current = initial.copy()
        current_value = calculate_heuristic(current)

        iteration = 1
        while iteration <= 50 and current_value < threshold:
            successors = generate_successors(current)
            best_successor = None
            best_successor_value = current_value

            for succ in successors:
                val = calculate_heuristic(succ)
                if val > best_successor_value:
                    best_successor_value = val
                    best_successor = succ

            if best_successor and best_successor_value > current_value:
                current = best_successor
                current_value = best_successor_value
            else:
                break

            iteration += 1

        print(f"Restart {restart+1} best: {current} Value: {current_value}")

        if current_value > best_value:
            best_overall = current
            best_value = current_value

        if current_value >= threshold:
            print(f"Solution found! {best_overall} Value: {best_value}")
            return best_overall, best_value

    print(
        f"\nBest overall after {max_restarts} restarts: {best_overall} Value: {best_value}"
    )
    return best_overall, best_value


# 3. Stochastic Hill-Climbing
def stochastic_hill_climbing(initial_state, threshold=28, max_iterations=100):
    print("\n=== STOCHASTIC HILL-CLIMBING ===")
    current = initial_state.copy()
    current_value = calculate_heuristic(current)

    print(f"Initial state: {current} Value: {current_value}")

    iteration = 1
    while iteration <= max_iterations and current_value < threshold:
        successors = generate_successors(current)

        # Collect all uphill moves
        uphill_moves = []
        for succ in successors:
            val = calculate_heuristic(succ)
            if val > current_value:
                uphill_moves.append((succ, val))

        if uphill_moves:
            # Choose random uphill move
            chosen, chosen_value = random.choice(uphill_moves)
            current = chosen
            current_value = chosen_value
            print(f"Iteration {iteration}: {current} Value: {current_value}")
        else:
            print(f"No uphill moves at: {current} Value: {current_value}")
            break

        iteration += 1

    if current_value >= threshold:
        print(f"Solution found! {current} Value: {current_value}")

    return current, current_value


# 4. First-Choice Hill-Climbing
def first_choice_hill_climbing(initial_state, threshold=28, max_iterations=100):
    print("\n=== FIRST-CHOICE HILL-CLIMBING ===")
    current = initial_state.copy()
    current_value = calculate_heuristic(current)

    print(f"Initial state: {current} Value: {current_value}")

    iteration = 1
    while iteration <= max_iterations and current_value < threshold:
        # Randomly generate and test successors until finding a better one
        found_better = False
        attempts = 0

        while not found_better and attempts < 100:
            # Generate random successor
            col = random.randint(0, 7)
            new_row = random.randint(1, 8)
            while new_row == current[col]:
                new_row = random.randint(1, 8)

            successor = current.copy()
            successor[col] = new_row
            succ_value = calculate_heuristic(successor)

            if succ_value > current_value:
                current = successor
                current_value = succ_value
                found_better = True
                print(f"Iteration {iteration}: {current} Value: {current_value}")

            attempts += 1

        if not found_better:
            print(
                f"Couldn't find better successor at: {current} Value: {current_value}"
            )
            break

        iteration += 1

    if current_value >= threshold:
        print(f"Solution found! {current} Value: {current_value}")

    return current, current_value


# ============================================
# GENETIC ALGORITHM
# ============================================


def initialize_population(size=8):
    """Create initial population from given states"""
    initial_states = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [1, 8, 2, 7, 3, 6, 4, 5],
        [4, 5, 3, 6, 2, 7, 1, 8],
        [1, 5, 2, 6, 3, 7, 4, 8],
        [8, 4, 7, 3, 6, 2, 5, 1],
        [1, 3, 5, 7, 2, 4, 6, 8],
        [2, 4, 6, 8, 1, 3, 5, 7],
    ]

    population = []
    for state in initial_states[:size]:
        population.append(
            {"state": state.copy(), "fitness": calculate_heuristic(state)}
        )

    return population


def select_parents(population, num_parents=4):
    """Select parents based on fitness (tournament selection)"""
    parents = []
    population_copy = population.copy()

    for _ in range(num_parents):
        # Tournament selection
        tournament = random.sample(population_copy, min(3, len(population_copy)))
        tournament.sort(key=lambda x: x["fitness"], reverse=True)
        parents.append(tournament[0])
        population_copy.remove(tournament[0])

    return parents


def crossover(parent1, parent2, crossover_point=4):
    """Perform crossover at specified point"""
    state1 = parent1["state"]
    state2 = parent2["state"]

    # Single point crossover
    child1_state = state1[:crossover_point] + state2[crossover_point:]
    child2_state = state2[:crossover_point] + state1[crossover_point:]

    child1 = {"state": child1_state, "fitness": calculate_heuristic(child1_state)}
    child2 = {"state": child2_state, "fitness": calculate_heuristic(child2_state)}

    return child1, child2


def mutate(individual, mutation_rate=0.3):
    """Mutate an individual with given probability"""
    if random.random() < mutation_rate:
        state = individual["state"].copy()
        # Randomly change one position
        pos = random.randint(0, 7)
        new_val = random.randint(1, 8)
        state[pos] = new_val
        individual["state"] = state
        individual["fitness"] = calculate_heuristic(state)

    return individual


def genetic_algorithm(threshold=28, max_generations=50, population_size=8):
    print("\n=== GENETIC ALGORITHM ===")

    # Initialize population
    population = initialize_population(population_size)

    print("Initial Population:")
    for i, ind in enumerate(population):
        print(f"  {i+1}: {ind['state']} Fitness: {ind['fitness']}")

    generation = 1
    while generation <= max_generations:
        # Check if solution found
        best = max(population, key=lambda x: x["fitness"])
        if best["fitness"] >= threshold:
            print(f"\nSolution found in generation {generation}!")
            print(f"State: {best['state']} Fitness: {best['fitness']}")
            return best

        # Select parents
        parents = select_parents(population)

        # Create new population through crossover
        new_population = []

        # Keep the best individual (elitism)
        population.sort(key=lambda x: x["fitness"], reverse=True)
        new_population.append(population[0])

        # Generate rest through crossover
        while len(new_population) < population_size:
            p1, p2 = random.sample(parents, 2)
            crossover_point = random.randint(1, 7)
            child1, child2 = crossover(p1, p2, crossover_point)

            # Mutate children
            child1 = mutate(child1)
            child2 = mutate(child2)

            new_population.append(child1)
            if len(new_population) < population_size:
                new_population.append(child2)

        population = new_population

        # Print generation info
        if generation % 10 == 0:
            best = max(population, key=lambda x: x["fitness"])
            avg_fitness = sum(ind["fitness"] for ind in population) / len(population)
            print(
                f"Generation {generation}: Best={best['fitness']}, Avg={avg_fitness:.2f}"
            )

        generation += 1

    # Final results
    best = max(population, key=lambda x: x["fitness"])
    print(
        f"\nBest after {max_generations} generations: {best['state']} Fitness: {best['fitness']}"
    )
    return best


# ============================================
# MAIN PROGRAM
# ============================================


def main():
    print("=" * 60)
    print("8-QUEENS PROBLEM - HILL CLIMBING & GENETIC ALGORITHM")
    print("=" * 60)

    # Set random seed for reproducibility
    random.seed(42)

    # Test initial state from the documentation example
    initial_state = [2, 3, 4, 5, 6, 5, 7, 8]
    threshold = 27  # As in the documentation example

    print(f"\nInitial state: {initial_state}")
    print(f"Initial heuristic value: {calculate_heuristic(initial_state)}")
    print(f"Target threshold: {threshold}")
    print("-" * 40)

    # Run standard hill climbing
    hill_climbing(initial_state, threshold)

    # Run stochastic hill climbing
    stochastic_hill_climbing(initial_state, threshold)

    # Run first-choice hill climbing
    first_choice_hill_climbing(initial_state, threshold)

    # Run random restart hill climbing
    random_restart_hill_climbing(threshold, max_restarts=5)

    # Run genetic algorithm
    genetic_algorithm(threshold, max_generations=30)

    print("\n" + "=" * 60)
    print("ALL ALGORITHMS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
