from math import factorial

from method.interpolation_method import InterpolationMethod


class Gauss(InterpolationMethod):

    def __init__(self):
        super().__init__("Многочлен Гаусса")

    def compute(self, xs, ys, n):
        n = len(xs) - 1
        alpha_ind = n // 2
        fin_difs = []
        fin_difs.append(ys[:])

        for k in range(1, n + 1):
            last = fin_difs[-1][:]
            new_difs = []
            for i in range(n - k + 1):
                new_difs.append(last[i + 1] - last[i])
            fin_difs.append(new_difs)

        h = xs[1] - xs[0]
        dts1 = [0]
        for i in range((n + 1) // 2):
            dts1.extend([-(i + 1), i + 1])

        def f1(x):
            total = ys[alpha_ind]
            for k in range(1, n + 1):
                product = 1
                for j in range(k):
                    product *= (x - xs[alpha_ind]) / h + dts1[j]
                total += product * fin_difs[k][len(fin_difs[k]) // 2] / factorial(k)
            return total

        def f2(x):
            total = ys[alpha_ind]
            for k in range(1, n + 1):
                product = 1
                for j in range(k):
                    product *= (x - xs[alpha_ind]) / h - dts1[j]
                index = len(fin_difs[k]) // 2 - (1 - len(fin_difs[k]) % 2)
                total += product * fin_difs[k][index] / factorial(k)
            return total

        def result(x):
            return f1(x) if x > xs[alpha_ind] else f2(x)

        return result
