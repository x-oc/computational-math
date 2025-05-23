from methods.integral_computing_method import IntegralComputingMethod


class SimpsonMethod(IntegralComputingMethod):

    def __init__(self):
        super().__init__("Метод Симпсона", 15)

    def compute(self, func, a, b, n):
        h = (b - a) / n
        result = func(a) + func(b)

        for i in range(1, n):
            try:
                coef = 3 + (-1) ** (i + 1)
                result += coef * func(a + i * h)
            except:
                pass

        result *= h / 3
        return result
