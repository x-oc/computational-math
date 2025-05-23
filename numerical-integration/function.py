import math


class Function:

    def __init__(self, func, view):
        self.func = func
        self.view = view

    def try_to_compute(self, x):
        try:
            return self.func(x)
        except:
            return None


def get_some_functions():
    functions = [
        Function(lambda x: x + 1, 'x + 1'),
        Function(lambda x: x * 2, 'x * 2'),
        Function(lambda x: x ** 2, 'x^2'),
        Function(lambda x: math.sin(x), 'sin(x)'),
        Function(lambda x: -x, '-x'),
        Function(lambda x: 1 / x, '1 / x'),
        Function(lambda x: 42, '42'),
        Function(lambda x: 1 / math.sqrt(x), '1 / sqrt(x)')
    ]
    return functions
