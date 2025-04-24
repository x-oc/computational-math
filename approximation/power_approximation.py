from approximation.abstract_approximation import AbstractApproximation
from approximation.linear_approximation import LinearApproximation
from math import exp, log


class PowerApproximation(AbstractApproximation):

    name = "Степенная"

    @staticmethod
    def get(xs, ys, n):
        _, a, b = LinearApproximation.get(list(map(log, xs)), list(map(log, ys)), n)
        a = exp(a)
        return lambda x: a * x ** b, a, b
