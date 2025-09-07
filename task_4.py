import numpy as np

def task_4():
    # (x, y)
    cities = [
        [119, 38],
        [37, 38],
        [197, 55],
        [85, 165],
        [12, 50],
        [100, 53],
        [81, 142],
        [121, 137],
        [85, 145],
        [80, 197],
        [91, 176],
        [106, 55],
        [123, 57],
        [40, 81],
        [78, 125],
        [190, 46],
        [187, 40],
        [37, 107],
        [17, 11],
        [67, 56],
        [78, 133],
        [87, 23],
        [184, 197],
        [111, 12],
        [66, 178]
    ]

    # random population
    population = np.array([np.random.permutation(25) for _ in range(100)])
    generation = 0

    while True:
        print("Generation: ", generation)

        # fitness function
        fitness_rates = np.empty(100)
        for row, chromosome in enumerate(population):
            total_distance = 0

            for i in range(len(chromosome) - 1):
                city_1_index = chromosome[i]
                city_2_index = chromosome[i + 1]

                city_1 = np.array(cities[city_1_index])
                city_2 = np.array(cities[city_2_index])

                distance = np.linalg.norm(city_1 - city_2)
                total_distance += distance

            city_1_index = chromosome[-1]
            city_2_index = chromosome[0]

            city_1 = np.array(cities[city_1_index])
            city_2 = np.array(cities[city_2_index])

            distance = np.linalg.norm(city_1 - city_2)
            total_distance += distance

            fitness_rates[row] = total_distance
            if total_distance <= 869:
                print(f"Total distance: {total_distance}, route: {chromosome}")


        # find 20 best individuals - elite
        sorted_fitness_rates_indices = np.argsort(fitness_rates)
        elite = population[sorted_fitness_rates_indices[:20]]

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

        # choosing parents for crossover
        # 81 parents -> 80 children (80%) + 20 elite (20%) = 100 individuals - new population
        crossover_parents = np.empty((81, 25), dtype=int)
        for roulette in range(81):
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

        # order crossover
        new_population = np.empty((100, 25), dtype=int)
        for i in range(len(crossover_parents) - 1):
            crossover_indices = np.sort(np.random.choice(24, size=2, replace=False) + 1)

            parent_1 = crossover_parents[i]
            parent_2 = crossover_parents[i + 1].tolist()

            child = np.ones(25, dtype=int) * -1
            for j in range(crossover_indices[0], crossover_indices[1]):
                child[j] = parent_1[j]

            for j, city in enumerate(child):
                if city != -1:
                    continue

                for _ in parent_2:
                    new_city = parent_2.pop(0)

                    if new_city not in child:
                        child[j] = new_city
                        break

            new_population[i] = child

        # mutation (80 children for mutation)
        for chromosome in range(80):
            for gene in range(25):
                mutation_rate = np.random.random()

                if mutation_rate < 0.01:
                    current_city = new_population[chromosome][gene]

                    valid_cities_indices = np.delete(np.arange(25), current_city)
                    choice = np.random.choice(valid_cities_indices)
                    choice_index = np.where(new_population[chromosome] == choice)

                    new_population[chromosome][gene] = choice
                    new_population[chromosome][choice_index] = current_city


        # TODO: change 20 individuals in new population - elite
        new_population[-1] = elite_1
        new_population[-2] = elite_2
        population = new_population
        generation += 1


if __name__ == '__main__':
    task_4()