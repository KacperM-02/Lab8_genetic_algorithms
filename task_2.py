import numpy as np

def task_2():
    # random population
    population = np.random.randint(2, size=(10, 8))
    generation = 0

    while True:
        print("Generation: ", generation)

        # fitness function
        fitness_rates = np.empty((10, 1))
        for row, chromosome in enumerate(population):
            a = int("".join(str(x) for x in chromosome[:4]), 2)
            b = int("".join(str(x) for x in chromosome[4:]), 2)
            result = 2 * a**2 + b

            if result == 33:
                print(f"a = {a}, b = {b}")
                print(f"2 * {a}^2 + {b} = 33")
                return

            difference = abs(33 - result)
            fitness_rate = 1 / (difference + 1)
            fitness_rates[row] = fitness_rate

        # division into sections
        fitness_rates_sum = fitness_rates.sum()
        probability_rates = np.array([rate/fitness_rates_sum for rate in fitness_rates])
        probability_sections = []
        for i, probability in enumerate(probability_rates):
            if i == 0:
                probability_sections.append(probability)
            else:
                probability_sections.append(probability_sections[i-1] + probability)

        # roulette selection
        new_population = np.empty((10, 8), dtype=int)
        for roulette in range(10):
            random_number = np.random.random()

            for i in range(len(probability_sections)):
                found_section = False

                if i == 0:
                    if 0 <= random_number < probability_sections[i]:
                        found_section = True
                else:
                    if probability_sections[i - 1] <= random_number < probability_sections[i]:
                        found_section = True

                if found_section:
                    new_population[roulette] = population[i]
                    break

        # crossover (size = 10/2 => 5 individuals for crossover)
        random_indices = np.random.choice(len(new_population), size=5, replace=False)

        for i in range(len(random_indices) - 1):
            crossover_index = np.random.randint(1, 7)

            parent_1 = new_population[random_indices[i]]
            parent_2 = new_population[random_indices[i + 1]]

            parent_1_left_part = parent_1[:crossover_index]
            parent_2_right_part = parent_2[crossover_index:]

            child = np.concatenate((parent_1_left_part, parent_2_right_part))

            random_parent = np.random.random()
            if random_parent < 0.5:
                new_population[random_indices[i]] = child
            else:
                new_population[random_indices[i + 1]] = child

        # mutation
        for chromosome in new_population:
            mutation_rate = np.random.random()
            if mutation_rate < 0.1:
                mutation_index = np.random.randint(8)
                chromosome[mutation_index] = 1 - chromosome[mutation_index]

        population = new_population
        generation += 1


if __name__ == '__main__':
    task_2()