from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

from user_interaction import get_system_of_equations


def func(xy):
    x, y = xy
    return [x ** 2 + y ** 2 - 1, x ** 2 - y - 0.5]


def solve(a, phi1, phi2, x0, eps, max_iterations=1_000):
    x = np.array(x0, dtype=float)

    try:
        iterations = 0
        for iterations in range(max_iterations):
            x1 = phi1(x[0], x[1])
            x2 = phi2(x[0], x[1])
            x_next = np.array([x1, x2])

            print(f'{iterations}. x1={x1}, x2={x2}, xnext=({x_next[0]}, {x_next[1]}), '
                  f'|xk+1 - xk|={np.linalg.norm(x_next - x)}')

            if abs(a(x_next)[0]) < eps and abs(a(x_next)[1]) < eps:
                return x_next, iterations

            x = x_next

        print(f"Метод простой итерации не сошелся за заданное количество итераций ({max_iterations})!")
        return x_next, iterations
    except ValueError:
        print(f'Невозможно найти phi в точке ({x0[0]}, {x0[1]})')
        return None, None


def phi1(x, y):
    # x1 = phi(x1, x2, ...)
    return sqrt(1 - y ** 2)


def phi2(x, y):
    # x2 = phi(x1, x2, ...)
    return x ** 2 - 0.5


def run():
    systems = {1: [func, "x^2 + y^2 - 1, x^2 - y - 0.5"]}
    equations_number = get_system_of_equations(systems)

    plot_system(systems[equations_number][0])

    x0, y0 = map(float, input("Введите начальное приближение x0, y0: ").split())
    eps = float(input('Введите допустимую погрешность: '))

    xy_solution, iterations = solve(func, phi1, phi2, (x0, y0), eps)

    if iterations is not None:
        print(f"\nНеизвестные: x = {xy_solution[0]:.5f}, y = {xy_solution[1]:.5f}")
        print(f"Количество итераций: {iterations}")
        plot_system_with_point(systems[equations_number][0], xy_solution)


def plot_system_with_point(system, x0):
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)

    Z1 = np.array([system([x_, y_])[0] for x_, y_ in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)
    Z2 = np.array([system([x_, y_])[1] for x_, y_ in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

    plt.contour(X, Y, Z1, levels=[0], colors='r')
    plt.contour(X, Y, Z2, levels=[0], colors='b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.scatter([x0[0]], [x0[1]], color='red', s=50)
    plt.show()


def plot_system(system):
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)

    Z1 = np.array([system([x_, y_])[0] for x_, y_ in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)
    Z2 = np.array([system([x_, y_])[1] for x_, y_ in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

    plt.contour(X, Y, Z1, levels=[0], colors='r')
    plt.contour(X, Y, Z2, levels=[0], colors='b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
