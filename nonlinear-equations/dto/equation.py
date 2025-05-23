from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
from scipy.differentiate import derivative


class Equation:
    def __init__(self, function: Callable, text: str):
        self.text = text
        self.function = function

    def draw(self, left: float, right: float):
        x = np.linspace(left, right)
        func = np.vectorize(self.function)(x)

        plt.title = 'График функции'
        plt.grid(True, which='both')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axhline(y=0, color='gray', label='y = 0')
        plt.plot(x, func, 'blue', label=self.text)
        plt.legend(loc='upper left')
        plt.savefig('graph.png')
        plt.show()


    def draw_with_point(self, left: float, right: float, x0):
        x = np.linspace(left, right)
        func = np.vectorize(self.function)(x)

        plt.title = 'График функции'
        plt.grid(True, which='both')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axhline(y=0, color='gray', label='y = 0')
        plt.plot(x, func, 'blue', label=self.text)
        plt.legend(loc='upper left')
        plt.savefig('graph.png')
        plt.scatter([x0[0]], [x0[1]], color='red', s=50)
        plt.show()

    def root_exists(self, left: float, right: float):
        return (self.function(left) * self.function(right) < 0) \
               and (derivative(self.function, left).df * derivative(self.function, right).df > 0)
