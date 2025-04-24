from approximation.abstract_approximation import AbstractApproximation
from matrix import solve_sle


class QuadraticApproximation(AbstractApproximation):

    name = "Полиномиальная 2-й степени"

    @staticmethod
    def get(xs, ys, n):
        sx = sum(xs)
        sx2 = sum(x ** 2 for x in xs)
        sx3 = sum(x ** 3 for x in xs)
        sx4 = sum(x ** 4 for x in xs)
        sy = sum(ys)
        sxy = sum(x * y for x, y in zip(xs, ys))
        sx2y = sum(x * x * y for x, y in zip(xs, ys))
        a, b, c = solve_sle(
            [
                [n, sx, sx2],
                [sx, sx2, sx3],
                [sx2, sx3, sx4]
            ],
            [sy, sxy, sx2y],
            3
        )
        return lambda x: a + b * x + c * x ** 2, a, b, c
