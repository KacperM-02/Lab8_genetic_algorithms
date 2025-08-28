import numpy as np

def task_3():
    # (weight, value)
    items = [
        (3, 266),
        (13, 442),
        (10, 671),
        (9, 526),
        (7, 388),
        (1, 245),
        (8, 210),
        (8, 145),
        (2, 126),
        (9, 322)
        ]

    # random population
    population = np.random.randint(2, size=(8, 10))
    generation = 0

    while True:
        print("Generation: ", generation)

        # fitness function
        fitness_rates = np.empty(8)
        for row, chromosome in enumerate(population):
            weight = 0
            value = 0
            for i, gene in enumerate(chromosome):
                weight += gene * items[i][0]
                value += gene * items[i][1]

            fitness_rate = 0
            if weight <= 35:
                fitness_rate = value

                if fitness_rate == 2222:
                    print(f"Weight: {weight}, value: {value}, items:")
                    for i, v in enumerate(chromosome):
                        if v == 1:
                            print(i)
                    return

            fitness_rates[row] = fitness_rate

        # find 2 best individuals - elite
        sorted_fitness_rates_indices = np.argsort(fitness_rates)

        elite_1_index = sorted_fitness_rates_indices[-1]
        elite_2_index = sorted_fitness_rates_indices[-2]

        elite_1 = population[elite_1_index]
        elite_2 = population[elite_2_index]

        # roulette selection
        # counting probability rates
        fitness_rates_sum = fitness_rates.sum()
        probability_rates = np.array([rate/fitness_rates_sum for rate in fitness_rates])

        # division into sections
        probability_sections = []
        for i, probability in enumerate(probability_rates):
            if i == 0:
                probability_sections.append(probability)
            else:
                probability_sections.append(probability_sections[i-1] + probability)

        # choosing parents for crossover: 7 parents -> 6 children + 2 elite = 8 individuals
        crossover_parents = np.empty((7, 10), dtype=int)
        for roulette in range(7):
            random_number = np.random.random()

            for i in range(len(probability_sections)):
                found_section = False

                if i == 0:
                    if 0 < random_number <= probability_sections[i]:
                        found_section = True
                else:
                    if probability_sections[i - 1] < random_number <= probability_sections[i]:
                        found_section = True

                if found_section:
                    crossover_parents[roulette] = population[i]
                    break

        # crossover
        new_population = np.empty((8, 10), dtype=int)
        for i in range(len(crossover_parents) - 1):
            crossover_index = np.random.randint(1, 9)

            parent_1 = crossover_parents[i]
            parent_2 = crossover_parents[i + 1]

            parent_1_left_part = parent_1[:crossover_index]
            parent_2_right_part = parent_2[crossover_index:]

            child = np.concatenate((parent_1_left_part, parent_2_right_part))
            new_population[i] = child

        # mutation
        for i in range(6):
            for j in range(10):
                mutation_rate = np.random.random()

                if mutation_rate < 0.05:
                    new_population[i][j] = 1 - new_population[i][j]

        new_population[-1] = elite_1
        new_population[-2] = elite_2
        population = new_population
        generation += 1


if __name__ == '__main__':
    task_3()