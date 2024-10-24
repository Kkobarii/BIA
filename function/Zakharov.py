import numpy as np

from function.Function import Function
from function.bounds.Specification import Specification


# source: https://www.sfu.ca/~ssurjano/zakharov.html
class Zakharov(Function):
    def __init__(self, specification=Specification(2, -10, 10)):
        super().__init__(specification)

    def evaluate(self, params: np.ndarray) -> int:
        sum1 = np.sum(np.pow(params, 2))
        sum2 = np.sum(0.5 * np.arange(1, self.specification.dimension + 1) * params)
        return sum1 + np.pow(sum2, 2) + np.pow(sum2, 4)
