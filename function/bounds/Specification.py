class Specification:
    def __init__(self, dimension=None, lower=None, upper=None):
        self.dimension = dimension
        self.lower = lower
        self.upper = upper

    def __str__(self):
        return f'Bounds: {self.lower} {self.upper} ({self.dimension}D)'