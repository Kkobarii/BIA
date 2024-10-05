from time import sleep

import numpy as np


class BlindSearch:
    def __init__(self, generations, population_size, function):
        self.generations = generations
        self.population_size = population_size
        self.function = function
        self.path = []
        self.current_generation = 0
        self.current_best = None

    def search(self) -> tuple:
        if self.current_generation >= self.generations:
            print('Search already complete!')
            return self.current_best

        print(f'\nStarting search for {self.function.__class__.__name__}')
        while self.current_generation < self.generations:
            self.step()
            # sleep(0.1)

        print('Search complete!')
        print(f'Best solution: {self.current_best[0]} -> {self.current_best[1]}')
        return self.current_best

    def step(self):
        if self.current_generation >= self.generations:
            print('Search already complete!')
            return self.current_best

        population = self.function.random_population(self.population_size)
        cost = np.array([self.function.evaluate(individual) for individual in population])
        best_index = np.argmin(cost)
        best = (population[best_index], cost[best_index])
        better = self.current_best is None or self.current_best[1] > best[1]

        current_result = (better, best)
        self.path.append(current_result)

        # print(f'Generation {self.current_generation}: {best[0]} -> {best[1]}')

        if better:
            self.current_best = best
            # print(f'New best!')

        self.current_generation += 1
        return current_result

    def get_name(self) -> str:
        return self.__class__.__name__
