from methods.integral_computing_method import IntegralComputingMethod


class RectangleMiddleMethod(IntegralComputingMethod):

    def __init__(self):
        super().__init__("Метод средних прямоугольников", 3)

    def compute(self, func, a, b, n):
        h = (b - a) / n
        result = 0

        for i in range(n):
            try:
                result += func(a + (i + 0.5) * h)
            except:
                pass

        result *= h
        return result
