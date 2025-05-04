from functools import reduce
from math import factorial
import numpy as np
from method.interpolation_method import InterpolationMethod


def finite_differences(y):
    n = len(y)
    delta_y = np.zeros((n, n))
    delta_y[:, 0] = y
    for j in range(1, n):
        for i in range(n-j):
            delta_y[i, j] = delta_y[i + 1, j - 1] - delta_y[i, j - 1]
    return delta_y


class NewtonFiniteDifference(InterpolationMethod):

    def __init__(self):
        super().__init__("Многочлен Ньютона с конечными разностями")

    def compute(self, xs, ys, n):
        h = xs[1] - xs[0]
        delta_y = finite_differences(ys)
        return lambda x: ys[0] + sum([
            reduce(lambda a, b: a * b, [(x - xs[0]) / h - j for j in range(k)])
            * delta_y[0, k] / factorial(k) for k in range(1, n)])
