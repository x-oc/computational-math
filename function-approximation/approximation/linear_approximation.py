from approximation.abstract_approximation import AbstractApproximation
from matrix import solve_sle


class LinearApproximation(AbstractApproximation):

    name = "Линейная"

    @staticmethod
    def get(xs, ys, n):
        sx = sum(xs)
        sx2 = sum(x ** 2 for x in xs)
        sy = sum(ys)
        sxy = sum(x * y for x, y in zip(xs, ys))

        a, b = solve_sle(
            [
                [n, sx],
                [sx, sx2]
            ],
            [sy, sxy], 2)
        return lambda x: a + b * x, a, b
