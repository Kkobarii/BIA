import numpy as np

from function.Function import Function
from function.bounds.Specification import Specification


# source: https://www.sfu.ca/~ssurjano/schwef.html
class Schwefel(Function):
    def __init__(self, specification=Specification(2, -500, 500)):
        super().__init__(specification)

    def evaluate(self, params: np.ndarray) -> int:
        return (418.9829 * self.specification.dimension
                - np.sum(params * np.sin(np.sqrt(np.abs(params)))))
