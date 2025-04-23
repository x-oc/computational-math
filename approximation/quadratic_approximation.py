from approximation.abstract_approximation import AbstractApproximation
from matrix import solve_sle


class QuadraticApproximation(AbstractApproximation):

    name = "Полиномиальная 2-й степени"

    @staticmethod
    def get(xs, ys, n):
        sx = sum(xs)
        sxx = sum(x ** 2 for x in xs)
        sxxx = sum(x ** 3 for x in xs)
        sxxxx = sum(x ** 4 for x in xs)
        sy = sum(ys)
        sxy = sum(x * y for x, y in zip(xs, ys))
        sxxy = sum(x * x * y for x, y in zip(xs, ys))
        a, b, c = solve_sle(
            [
                [n, sx, sxx],
                [sx, sxx, sxxx],
                [sxx, sxxx, sxxxx]
            ],
            [sy, sxy, sxxy],
            3
        )
        return lambda xi: a + b * xi + c * xi ** 2, a, b, c
