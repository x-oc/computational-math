from approximation.abstract_approximation import AbstractApproximation
from matrix import solve_sle


class CubicApproximation(AbstractApproximation):

    name = "Полиномиальная 3-й степени"

    @staticmethod
    def get(xs, ys, n):
        sx = sum(xs)
        sx2 = sum(x ** 2 for x in xs)
        sx3 = sum(x ** 3 for x in xs)
        sx4 = sum(x ** 4 for x in xs)
        sx5 = sum(x ** 5 for x in xs)
        sx6 = sum(x ** 6 for x in xs)
        sy = sum(ys)
        sxy = sum(x * y for x, y in zip(xs, ys))
        sx2y = sum(x * x * y for x, y in zip(xs, ys))
        sx3y = sum(x * x * x * y for x, y in zip(xs, ys))
        a, b, c, d = solve_sle(
            [
                [n, sx, sx2, sx3],
                [sx, sx2, sx3, sx4],
                [sx2, sx3, sx4, sx5],
                [sx3, sx4, sx5, sx6]
            ],
            [sy, sxy, sx2y, sx3y],
            4
        )
        return lambda x: a + b * x + c * x ** 2 + d * x ** 3, a, b, c, d
