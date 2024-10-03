import numpy as np

from function.Function import Function
from function.bounds.Specification import Specification


# source: https://www.sfu.ca/~ssurjano/rastr.html
class Rastrigin(Function):
    def __init__(self, specification=Specification(2, -5.12, 5.12)):
        super().__init__(specification)

    def evaluate(self, params: 'np.ndarray') -> int:
        return 10 * self.specification.dimension + np.sum(np.pow(params, 2) - 10 * np.cos(2 * np.pi * params))
