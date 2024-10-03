import numpy as np

from function.Function import Function
from function.bounds.Specification import Specification


# source: https://www.sfu.ca/~ssurjano/rosen.html
class Rosenbrock(Function):
    def __init__(self, specification=Specification(2, -10, 10)):
        super().__init__(specification)

    def evaluate(self, params: np.ndarray) -> int:
        return np.sum([100 * np.pow(params[i + 1] - np.pow(params[i], 2), 2)
                       + np.pow((params[i] - 1), 2) for i in
                       range(self.specification.dimension - 1)])
