import numpy as np

def task_1():
    # random population
    population = np.random.randint(2, size=(10, 10))
    generation = 0
    test = [1,2,3,4,5,6]

    while True:
        print("Generation: ", generation)

        # fitness function
        fitness_rates = np.array([np.sum(chromosome) for chromosome in population])
        best_fitness_rate = np.max(fitness_rates)

        if best_fitness_rate == 10:
            return generation

        # find 2 best individuals
        sorted_fitness_rates_indices = np.argsort(fitness_rates)

        parent_1_index = sorted_fitness_rates_indices[-1]
        parent_2_index = sorted_fitness_rates_indices[-2]

        parent_1 = population[parent_1_index]
        parent_2 = population[parent_2_index]

        # crossover
        crossover_index = np.random.randint(10)
        parent_1_left_part = parent_1[:crossover_index]
        parent_2_left_part = parent_2[:crossover_index]

        parent_1_right_part = parent_1[crossover_index:]
        parent_2_right_part = parent_2[crossover_index:]

        child_1 = np.concatenate((parent_1_left_part, parent_2_right_part))
        child_2 = np.concatenate((parent_2_left_part, parent_1_right_part))

        # mutation
        mutation_rate = np.random.randint(101)
        if mutation_rate >= 60:
            mutation_index = np.random.randint(10)
            child_1 = child_1[mutation_index]
            child_2 = child_2[mutation_index]

        # replacement the least adapted


        print("test")








    

if __name__ == '__main__':
    task_1()