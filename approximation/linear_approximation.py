from approximation.abstract_approximation import AbstractApproximation
from matrix import solve_sle


class LinearApproximation(AbstractApproximation):

    name = "Линейная"

    @staticmethod
    def get(xs, ys, n):
        sx = sum(xs)
        sxx = sum(x ** 2 for x in xs)
        sy = sum(ys)
        sxy = sum(x * y for x, y in zip(xs, ys))

        a, b = solve_sle(
            [
                [n, sx],
                [sx, sxx]
            ],
            [sy, sxy], 2)
        return lambda xi: a + b * xi, a, b
