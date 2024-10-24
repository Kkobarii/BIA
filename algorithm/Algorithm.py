class Algorithm:
    def __init__(self, function):
        self.function = function

    def search(self) -> tuple:
        pass

    def get_name(self) -> str:
        return self.__class__.__name__

    def get_path(self):
        return None

    def get_result(self):
        return None
