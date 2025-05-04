from functools import reduce
from method.interpolation_method import InterpolationMethod


class Lagrange(InterpolationMethod):

    def __init__(self):
        super().__init__("Многочлен Лагранжа")

    def compute(self, xs, ys, n):
        return lambda x: sum([ys[i] * reduce(
                lambda a, b: a * b, [(x - xs[j]) / (xs[i] - xs[j]) for j in range(n) if i != j])
            for i in range(n)])
