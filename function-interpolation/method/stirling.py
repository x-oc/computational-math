from math import factorial

from method.interpolation_method import InterpolationMethod


class Stirling(InterpolationMethod):

    def __init__(self):
        super().__init__("Многочлен Стирлинга")

    def compute(self, xs, ys, n):
        n = len(xs) - 1
        alpha_ind = n // 2
        fin_difs = [ys.copy()]

        for k in range(1, n + 1):
            last = fin_difs[-1].copy()
            new_difs = []
            for i in range(n - k + 1):
                new_difs.append(last[i + 1] - last[i])
            fin_difs.append(new_difs)

        h = xs[1] - xs[0]
        dts1 = [0]
        for i in range((n + 1) // 2):
            dts1.extend([-(i + 1), i + 1])

        def f1(x):
            result = ys[alpha_ind]
            for k in range(1, n + 1):
                product = 1.0
                for j in range(k):
                    product *= (x - xs[alpha_ind]) / h + dts1[j]
                middle_index = len(fin_difs[k]) // 2
                result += product * fin_difs[k][middle_index] / factorial(k)
            return result

        def f2(x):
            result = ys[alpha_ind]
            for k in range(1, n + 1):
                product = 1.0
                for j in range(k):
                    product *= (x - xs[alpha_ind]) / h - dts1[j]
                index = len(fin_difs[k]) // 2 - (1 - len(fin_difs[k])) % 2
                result += product * fin_difs[k][index] / factorial(k)
            return result

        def interpolate(x):
            return (f1(x) + f2(x)) / 2

        return interpolate
