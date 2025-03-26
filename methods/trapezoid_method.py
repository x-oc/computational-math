from methods.integral_computing_method import IntegralComputingMethod


class TrapezoidMethod(IntegralComputingMethod):

    def __init__(self):
        super().__init__("Метод трапеций", 3)

    def compute(self, func, a, b, n):
        h = (b - a) / n
        result = (func(a) + func(b)) / 2

        for i in range(1, n):
            try:
                result += func(a + i * h)
            except:
                pass

        result *= h
        return result
