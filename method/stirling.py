from functools import reduce
from math import factorial

from method.interpolation_method import InterpolationMethod


class Stirling(InterpolationMethod):

    def __init__(self):
        super().__init__("Многочлен Стирлинга")

    def compute(self, xs, ys, n):
        n = len(xs) - 1
        alpha_ind = n // 2
        fin_difs = []
        fin_difs.append(ys[:])

        for k in range(1, n + 1):
            last = fin_difs[-1][:]
            fin_difs.append(
                [last[i + 1] - last[i] for i in range(n - k + 1)])

        h = xs[1] - xs[0]
        dts1 = [0]
        for i in range((n + 1) // 2):
            dts1.extend([-(i + 1), i + 1])

        f1 = lambda x: ys[alpha_ind] + sum([
            reduce(lambda a, b: a * b, [(x - xs[alpha_ind]) / h + dts1[j] for j in range(k)])
            * fin_difs[k][len(fin_difs[k]) // 2] / factorial(k) for k in range(1, n + 1)])

        f2 = lambda x: ys[alpha_ind] + sum([
            reduce(lambda a, b: a * b,
                   [(x - xs[alpha_ind]) / h - dts1[j] for j in range(k)])
            * fin_difs[k][len(fin_difs[k]) // 2 - (1 - len(fin_difs[k]) % 2)] / factorial(k)
            for k in range(1, n + 1)])

        return lambda x: (f1(x) + f2(x)) / 2
