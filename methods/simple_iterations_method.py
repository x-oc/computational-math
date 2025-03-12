import numpy as np
from scipy.differentiate import derivative
from dto.result import Result
from methods.method import Method


class SimpleIterationsMethod(Method):
    name = 'Метод простой итерации'

    def check(self):
        root_exists = self.equation.root_exists(self.left, self.right)
        return root_exists, 'На заданном промежутке корня нет или корней больше двух' if not root_exists else ''

    def solve(self) -> Result:
        f = self.equation.function

        max_derivative = max(abs(derivative(f, self.left).df), abs(derivative(f, self.right).df))
        lbd = 1 / max_derivative

        if derivative(f, self.left).df > 0:
            lbd = -lbd

        phi = lambda xx: xx + lbd * f(xx)

        print('phi\'(a) = ', abs(derivative(phi, self.left).df))
        print('phi\'(b) = ', abs(derivative(phi, self.right).df))

        phi_ = lambda xx: derivative(phi, xx).df
        q = np.max(abs(phi_(np.linspace(self.left, self.right, 100))))
        if q > 1:
            print(f'Не выполнено условие сходимости метода |phi\'(x)| < 1')
            return

        x = self.left
        iteration = 0

        for iteration in range(1, 500):
            x_prev = x
            x = phi(x)

            print(f'{iteration}: xk = {x_prev:.4f}, f(xk) = {f(x_prev)}, '
                  f'xk+1 = 𝜑(𝑥𝑘) = {x:.4f}, |xk - xk+1| = {abs(x - x_prev):}')

            if abs(x - x_prev) <= self.eps and abs(f(x)) <= self.eps:
                break
        else:
            print(f'Достигнуто максимальное количество итераций!\n')

        return Result(x, f(x), iteration, self.decimal_places)
