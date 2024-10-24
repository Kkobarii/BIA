import numpy as np

from algorithm.Algorithm import Algorithm


class SimulatedAnnealing(Algorithm):
    def __init__(self, function, initial_temperature=100, minimal_temperature=0.5, cooling_rate=0.95):
        super().__init__(function)
        self.temperature = initial_temperature
        self.current_generation = 0
        self.path = []
        self.current_best = None
        self.initial_temperature = initial_temperature
        self.minimal_temperature = minimal_temperature
        self.cooling_rate = cooling_rate

    def search(self) -> tuple:
        # init search with a random point
        current_point = self.function.random_point()
        current_cost = self.function.evaluate(current_point)
        self.current_best = (current_point, current_cost)
        self.path.append((True, self.current_best))

        print(f'\nStarting {self.get_name()} search for {self.function.__class__.__name__}')
        while self.temperature > self.minimal_temperature:
            self.step()

        print('Search complete!')
        print(f'Best solution: {self.current_best[0]} -> {self.current_best[1]}')
        return self.current_best

    def step(self):
        # get a random neighbour
        new_point = self.function.random_normal_neighbour(self.current_best[0], 0.02)
        new_cost = self.function.evaluate(new_point)

        if new_cost < self.current_best[1]:
            self.current_best = (new_point, new_cost)
            self.path.append((True, self.current_best))
        else:
            r = self.random()
            delta = new_cost - self.current_best[1]
            if self.acceptance_probability(delta, self.temperature) > r:
                self.current_best = (new_point, new_cost)
                self.path.append((True, self.current_best))

        self.temperature = self.temperature * self.cooling_rate
        return self.current_best

    def acceptance_probability(self, delta, temperature):
        if delta < 0:
            return 1
        return np.exp(-delta / temperature)

    def random(self):
        return np.random.random()

    def get_path(self):
        return self.path

    def get_result(self):
        return self.current_best
