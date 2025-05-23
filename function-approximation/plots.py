import matplotlib.pyplot as plt


def draw_plot(x, y):
    plt.scatter(x, y, label="Вводные точки")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Приближение функции различными методами")
    plt.show()


def draw_func(func, name, x, dx=0.001):
    a = x[0]
    b = x[-1]
    xs, ys = [], []
    a -= 0.1
    b += 0.1
    x = a
    while x <= b:
        xs.append(x)
        ys.append(func(x))
        x += dx
    plt.plot(xs, ys, label=name)
