import numpy as np

from function.Function import Function
from function.bounds.Specification import Specification


# source: https://www.sfu.ca/~ssurjano/michal.html
class Michalewicz(Function):
    def __init__(self, specification=Specification(2, 0, np.pi)):
        super().__init__(specification)

    def evaluate(self, params: np.ndarray) -> int:
        m = 10
        return -np.sum([np.sin(params[i]) * np.sin((i + 1) * params[i] ** 2 / np.pi) ** (2 * m)
                        for i in range(self.specification.dimension)])
