from approximation.abstract_approximation import AbstractApproximation
from approximation.linear_approximation import LinearApproximation
from math import log


class LogarithmicApproximation(AbstractApproximation):

    name = "Логарифмическая"

    @staticmethod
    def get(xs, ys, n):
        _, a, b = LinearApproximation.get(list(map(log, xs)), ys, n)
        return lambda xi: a + b * log(xi), a, b
