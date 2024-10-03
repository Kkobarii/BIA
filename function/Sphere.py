import numpy as np

from function.Function import Function
from function.bounds.Specification import Specification


# source: https://www.sfu.ca/~ssurjano/spheref.html
class Sphere(Function):
    def __init__(self, specification=Specification(2, -5.12, 5.12)):
        super().__init__(specification)

    def evaluate(self, params: np.ndarray) -> int:
        return np.sum(np.pow(params, 2))
