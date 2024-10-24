import numpy as np

from function.Function import Function
from function.bounds.Specification import Specification


# source: https://www.sfu.ca/~ssurjano/griewank.html
class Griewank(Function):
    def __init__(self, specification=Specification(2, -8, 8)):
        super().__init__(specification)

    def evaluate(self, params: np.ndarray) -> int:
        sum1 = np.sum(np.pow(params, 2))
        prod1 = np.prod(np.cos(params / np.sqrt(np.arange(1, self.specification.dimension + 1))))
        return 1 + sum1 / 4000 - prod1
