from user_interaction import get_params
from matplotlib import pyplot as plt

from method.bessel import Bessel
from method.gauss import Gauss
from method.lagrange import Lagrange
from method.newton_divided_difference import NewtonDividedDifference
from method.newton_finite_difference import NewtonFiniteDifference, finite_differences
from method.stirling import Stirling
from user_interaction import print_finite_differences_table, draw_plot


def solve(xs, ys, x, n):
    delta_y = finite_differences(ys)
    print_finite_differences_table(delta_y)

    print('\n' + '-' * 60)

    methods = [Lagrange(), NewtonDividedDifference(), NewtonFiniteDifference(), Gauss(), Stirling(), Bessel()]

    for method in methods:
        finite_difference = True
        last = xs[1] - xs[0]
        for i in range(1, n):
            new = abs(xs[i] - xs[i - 1])
            if abs(new - last) > 0.0001:
                finite_difference = False
            last = new

        if isinstance(method, NewtonFiniteDifference) and not finite_difference:
            continue

        if isinstance(method, NewtonDividedDifference) and finite_difference:
            continue

        if (isinstance(method, Gauss) or isinstance(method, Stirling)) and len(xs) % 2 == 0:
            continue

        if isinstance(method, Bessel) and len(xs) % 2 == 1:
            continue

        h = xs[1] - xs[0]
        alpha_ind = n // 2
        t = (x - xs[alpha_ind]) / h
        print("t: ", t)

        print(method.name)
        p = method.compute(xs, ys, n)
        print(f'P({x}) = {p(x)}')
        print('-' * 60)

        plt.title(method.name)
        draw_plot(xs[0], xs[-1], p, method.name)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.scatter(x, p(x), c='r')
        for i in range(len(xs)):
            plt.scatter(xs[i], ys[i], c='b')

        plt.show()


if __name__ == "__main__":
    solve(*get_params())
