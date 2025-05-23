
def func(x):
    return x ** 3 - 1.89 * x ** 2 - 2 * x + 1.76


def half_div():
    global a, b
    x = round((a + b) / 2, 3)
    fa = round(func(a), 3)
    fb = round(func(b), 3)
    fx = round(func(x), 3)
    print(a, b, x, fa, fb, fx, round(abs(a - b), 3))
    if fa < 0 and fx < 0 or fa > 0 and fx > 0:
        a = x
    else:
        b = x


def simple_iter():
    global x
    new_x = round(x - (func(x)) / 7.3, 3)
    print(new_x, end=' ')
    print(round(func(x), 3), end=' ')
    print(round(abs(x - new_x), 3))
    x = new_x


def secant():
    global x
    x.append(round(x[-1] - (x[-1] - x[-2]) / (func(x[-1]) - func(x[-2])) * (func(x[-1])), 3))
    print(*x[-3:], round(func(x[-1]), 3), round(abs(x[-1] - x[-2]), 3))
