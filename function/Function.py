import numpy as np

from function.bounds.Specification import Specification


class Function:
    def __init__(self, specification: 'Specification'):
        self.specification = specification

    def evaluate(self, params: np.ndarray) -> int:
        pass