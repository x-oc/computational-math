from methods.integral_computing_method import IntegralComputingMethod


class RectangleLeftMethod(IntegralComputingMethod):

    def __init__(self):
        super().__init__("Метод левых прямоугольников", 1)

    def compute(self, func, a, b, n):
        h = (b - a) / n
        result = 0

        for i in range(n):
            try:
                result += func(a + i * h)
            except:
                pass

        result *= h
        return result
