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

    def random_population_around_point(self, point: np.ndarray, size: int, distance: int) -> np.ndarray:
        return np.random.uniform(point - distance, point + distance, (size, self.specification.dimension))

    def random_point(self) -> np.ndarray:
        return np.random.uniform(self.specification.lower, self.specification.upper, self.specification.dimension)

    def get_name(self) -> str:
        return self.__class__.__name__
