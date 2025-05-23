from math import sin, cos, exp
import matplotlib.pyplot as plt
import numpy as np


def get_odu():
    print('ОДУ: ')
    print('1. y + (1 + x)*y^2')
    print('2. x + y')
    print('3. sin(x) - y\n')

    while True:
        try:
            input_func = int(input('> Выберите ОДУ [1/2/3]: '))
            if input_func == 1:
                f = lambda x, y: y + (1 + x) * y ** 2
                # Точные значения находим через
                # https://mathdf.com/dif/ru/#expr=y'%3Dy%2B(1%2Bx)*y%5E2&func=y&arg=x&vals=x_0%3By_0
                exact_y = lambda x, x0, y0: -exp(x) / (x*exp(x) - (x0*exp(x0)*y0 + exp(x0)) / y0)
                break
            elif input_func == 2:
                f = lambda x, y: x + y
                exact_y = lambda x, x0, y0: exp(x - x0) * (y0 + x0 + 1) - x - 1
                break
            elif input_func == 3:
                f = lambda x, y: sin(x) - y
                exact_y = lambda x, x0, y0: (2*exp(x0) * y0-exp(x0)*sin(x0)+exp(x0)*cos(x0)) / (2*exp(x)) + (sin(x)) / 2 - (cos(x)) / 2
                break
            else:
                print("! Некорректный ввод. Попробуйте еще раз\n")
        except:
            print("! Некорректный ввод. Попробуйте еще раз\n")

    return f, exact_y


def get_params():
    f, exact_y = get_odu()

    while True:
        try:
            x0 = float(input('> Введите первый элемент интервала x0: '))
            xn = float(input('> Введите последний элемент интервала xn: '))
            if xn <= x0:
                print('! xn должен быть больше x0. Введите еще раз.')
                continue
            n = int(input('> Введите число элементов в интервале n: '))
            if n <= 1:
                print('! Количество элементов n должно быть > 1. Введите еще раз.')
                continue
            y0 = float(input('> Введите y0: '))
            eps = float(input('> Введите точность eps: '))
            break
        except:
            print("! Некорректный ввод. Попробуйте еще раз\n")

    return f, x0, xn, n, y0, exact_y, eps


def draw_plot(name, xs, ys, func):
    print("\nПостроение графика ...")
    print('-' * 30 + '\n')

    while len(xs) > 200:
        xs = [xs[i] for i in range(len(xs)) if i % 2 == 0]
        ys = [ys[i] for i in range(len(ys)) if i % 2 == 0]

    plt.scatter(xs, ys, color='red', label='Численное решение')

    x_accurate = np.linspace(min(xs), max(xs), 1000)
    y_accurate = np.array(list(map(lambda x: func(x, xs[0], ys[0]), x_accurate)))
    plt.plot(x_accurate, y_accurate, label='Истинное решение')

    plt.title(name)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
