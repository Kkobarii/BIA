import numpy as np

from function.Function import Function
from function.bounds.Specification import Specification


# source: https://www.sfu.ca/~ssurjano/ackley.html
class Ackley(Function):
    def __init__(self, specification=Specification(2, -32.768, 32.768)):
        super().__init__(specification)

    def evaluate(self, params: np.ndarray) -> int:
        a = 20
        b = 0.2
        c = 2 * np.pi
        sum1 = np.sum(np.pow(params, 2))
        sum2 = np.sum(np.cos(c * params))
        return -a * np.exp(-b * np.sqrt(sum1 / self.specification.dimension)) - np.exp(
            sum2 / self.specification.dimension) + a + np.exp(1)
