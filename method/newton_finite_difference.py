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

        def newton_polynomial(x):
            result = ys[0]
            for k in range(1, n):
                product = 1.0
                for j in range(k):
                    product *= (x - xs[0]) / h - j
                result += product * delta_y[0, k] / factorial(k)
            return result

        return newton_polynomial
