import numpy as np

from function.Function import Function
from function.bounds.Specification import Specification


# source: https://www.sfu.ca/~ssurjano/levy.html
class Levy(Function):
    def __init__(self, specification=Specification(2, -10, 10)):
        super().__init__(specification)

    def evaluate(self, params: np.ndarray) -> int:
        w = 1 + (params - 1) / 4
        dim = self.specification.dimension - 1
        return (np.sin(np.pi * w[0]) ** 2
                + np.sum([(w[i] - 1) ** 2 * (1 + 10 * np.sin(np.pi * w[i] + 1) ** 2) for i in
                          range(dim)])
                + (w[dim] - 1) ** 2 * (
                        1 + np.sin(2 * np.pi * w[dim]) ** 2))
