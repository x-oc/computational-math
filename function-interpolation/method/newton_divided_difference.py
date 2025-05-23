import numpy as np
from method.interpolation_method import InterpolationMethod


def divided_differences(x, y):
    n = len(y)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef


class NewtonDividedDifference(InterpolationMethod):

    def __init__(self):
        super().__init__("Многочлен Ньютона с разделенными разностями")

    def compute(self, xs, ys, n):
        coef = divided_differences(xs, ys)

        def interpolate(x):
            result = ys[0]
            for k in range(1, n):
                product = 1.0
                for j in range(k):
                    product *= (x - xs[j])
                result += coef[k] * product
            return result

        return interpolate
