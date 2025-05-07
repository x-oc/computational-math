from method.interpolation_method import InterpolationMethod


class Lagrange(InterpolationMethod):

    def __init__(self):
        super().__init__("Многочлен Лагранжа")

    def compute(self, xs, ys, n):
        def interpolation_function(x):
            result = 0.0
            for i in range(n):
                term = ys[i]
                for j in range(n):
                    if i != j:
                        term *= (x - xs[j]) / (xs[i] - xs[j])
                result += term
            return result

        return interpolation_function
