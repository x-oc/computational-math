from math import factorial

from method.interpolation_method import InterpolationMethod


class Bessel(InterpolationMethod):

    def __init__(self):
        super().__init__("Многочлен Бесселя")

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

        def interpolate(x):
            base = (ys[alpha_ind] + ys[alpha_ind]) / 2
            total = base

            for k in range(1, n + 1):
                product1 = 1.0
                for j in range(k):
                    product1 *= (x - xs[alpha_ind]) / h + dts1[j]
                term1 = product1 * fin_difs[k][len(fin_difs[k]) // 2] / factorial(k)

                product2 = (x - xs[alpha_ind]) / h - 0.5
                for j in range(k):
                    product2 *= (x - xs[alpha_ind]) / h + dts1[j]
                term2 = product2 * fin_difs[k][len(fin_difs[k]) // 2] / factorial(k)

                total += term1 + term2

            return total

        return interpolate
