from approximation.abstract_approximation import AbstractApproximation
from approximation.linear_approximation import LinearApproximation
from math import exp, log


class ExponentialApproximation(AbstractApproximation):

    name = "Экспоненциальная"

    @staticmethod
    def get(xs, ys, n):
        ys_ = list(map(log, ys))
        _, a, b = LinearApproximation.get(xs, ys_, n)
        a = exp(a)
        return lambda x: a * exp(b * x), a, b
