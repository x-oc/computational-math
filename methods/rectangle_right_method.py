from methods.integral_computing_method import IntegralComputingMethod


class RectangleRightMethod(IntegralComputingMethod):

    def __init__(self):
        super().__init__("Метод правых прямоугольников", 1)

    def compute(self, func, a, b, n):
        h = (b - a) / n
        result = 0

        for i in range(1, n + 1):
            result += func(a + i * h)

        result *= h
        return result
