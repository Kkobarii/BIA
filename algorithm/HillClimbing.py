from algorithm.Algorithm import Algorithm


class HillClimbing(Algorithm):
    def __init__(self, generations, function, factor=0.1):
        super().__init__(function)
        self.generations = generations
        self.current_generation = 0
        self.path = []
        self.current_best = None
        self.step_size = factor * (self.function.specification.upper - self.function.specification.lower)

    def search(self) -> tuple:
        if self.current_generation >= self.generations:
            print('Search already complete!')
            return self.current_best

        # init search with a random point
        current_point = self.function.random_point()
        current_cost = self.function.evaluate(current_point)
        self.current_best = (current_point, current_cost)
        self.path.append((True, self.current_best))

        print(f'\nStarting search for {self.function.__class__.__name__}')
        while self.current_generation < self.generations:
            self.step()

        print('Search complete!')
        print(f'Best solution: {self.current_best[0]} -> {self.current_best[1]}')
        return self.current_best

    def step(self):
        if self.current_generation >= self.generations:
            print('Search already complete!')
            return self.current_best

        # get a random neighbour
        for point in self.function.random_normal_population_around_point(self.current_best[0], 100, self.step_size):
            cost = self.function.evaluate(point)
            if cost < self.current_best[1]:
                self.current_best = (point, cost)
                self.path.append((True, self.current_best))
                break

        self.current_generation += 1
        return self.current_best

    def get_path(self):
        return self.path
