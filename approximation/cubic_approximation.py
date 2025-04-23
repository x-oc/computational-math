from approximation.abstract_approximation import AbstractApproximation
from matrix import solve_sle


class CubicApproximation(AbstractApproximation):

    name = "Полиномиальная 3-й степени"

    @staticmethod
    def get(xs, ys, n):
        sx = sum(xs)
        sxx = sum(x ** 2 for x in xs)
        sxxx = sum(x ** 3 for x in xs)
        sxxxx = sum(x ** 4 for x in xs)
        sxxxxx = sum(x ** 5 for x in xs)
        sxxxxxx = sum(x ** 6 for x in xs)
        sy = sum(ys)
        sxy = sum(x * y for x, y in zip(xs, ys))
        sxxy = sum(x * x * y for x, y in zip(xs, ys))
        sxxxy = sum(x * x * x * y for x, y in zip(xs, ys))
        a, b, c, d = solve_sle(
            [
                [n, sx, sxx, sxxx],
                [sx, sxx, sxxx, sxxxx],
                [sxx, sxxx, sxxxx, sxxxxx],
                [sxxx, sxxxx, sxxxxx, sxxxxxx]
            ],
            [sy, sxy, sxxy, sxxxy],
            4
        )
        return lambda xi: a + b * xi + c * xi ** 2 + d * xi ** 3, a, b, c, d
