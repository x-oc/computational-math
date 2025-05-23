def euler_method(f, xs, y0, eps):
    ys = [y0]
    h = xs[1] - xs[0]
    for i in range(len(xs) - 1):
        y_next = ys[i] + h * f(xs[i], ys[i])
        ys.append(y_next)
    return ys


def improved_euler_method(f, xs, y0, eps):
    ys = [y0]
    h = xs[1] - xs[0]
    for i in range(len(xs) - 1):
        y_pred = f(xs[i], ys[i])
        y_corr = f(xs[i] + h, ys[i] + h * y_pred)
        ys.append(ys[i] + 0.5 * h * (y_pred + y_corr))
    return ys


def adams_method(f, xs, y0, eps):
    n = len(xs)
    h = xs[1] - xs[0]
    y = [y0]

    for i in range(1, 4):
        k1 = h * f(xs[i - 1], y[i - 1])
        k2 = h * f(xs[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * f(xs[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * f(xs[i - 1] + h, y[i - 1] + k3)
        y.append(y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    for i in range(4, n):
        y_next = y[i - 1] + h * (55 * f(xs[i - 1], y[i - 1]) - 59 * f(xs[i - 2], y[i - 2]) +
                                 37 * f(xs[i - 3], y[i - 3]) - 9 * f(xs[i - 4], y[i - 4])) / 24

        while True:
            y_corrected = y[i - 1] + h * (9 * f(xs[i], y_next) + 19 * f(xs[i - 1], y[i - 1]) -
                                          5 * f(xs[i - 2], y[i - 2]) + f(xs[i - 3], y[i - 3])) / 24
            if abs(y_corrected - y_next) < eps:
                y_next = y_corrected
                break
            y_next = y_corrected

        y.append(y_next)

    return y