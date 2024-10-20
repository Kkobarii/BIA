import numpy as np

from function.bounds.Specification import Specification


class Function:
    def __init__(self, specification: 'Specification'):
        self.specification = specification

    def evaluate(self, params: np.ndarray) -> int:
        pass

    def grid(self, size: int):
        x = np.linspace(self.specification.lower, self.specification.upper, 100)
        return np.meshgrid(x, x)

    def random_population(self, size: int) -> np.ndarray:
        return np.random.uniform(self.specification.lower, self.specification.upper,
                                 (size, self.specification.dimension))

    def random_point(self) -> np.ndarray:
        return np.random.uniform(self.specification.lower, self.specification.upper, self.specification.dimension)

    def random_normal_population_around_point(self, point: np.ndarray, size: int, distance: int) -> np.ndarray:
        return (np.random.normal(point, distance, (size, self.specification.dimension))
                .clip(self.specification.lower, self.specification.upper))

    def random_normal_neighbour(self, point: np.ndarray, percentage: int) -> np.ndarray:
        distance = (self.specification.upper - self.specification.lower) * percentage / 100
        return (np.random.normal(point, distance)
                .clip(self.specification.lower, self.specification.upper))

    def get_name(self) -> str:
        return self.__class__.__name__
