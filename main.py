from math import inf

from methods import improved_euler_method, adams_method, euler_method
from user_interaction import draw_plot, get_params

MAX_ITERS = 15


def solve(f, x0, xn, n, y0, exact_y, eps):
    print()
    methods = [("Метод Эйлера", euler_method),
               ("Усовершенствованный метод Эйлера", improved_euler_method),
               ("Метод Адамса", adams_method)]

    for name, method in methods:
        ni = n
        print(name + ":\n")

        try:
            iters = 0

            xs = [x0 + i * ((xn - x0) / ni) for i in range(ni)]
            ys = method(f, xs, y0, eps)
            inaccuracy = inf

            while inaccuracy > eps:
                if iters >= MAX_ITERS:
                    print(f"! Не удалось увеличить точность. Произведено {iters} итераций.")
                    break

                iters += 1
                ni *= 2
                xs = [x0 + i * (xn - x0) / ni for i in range(ni)]
                new_ys = method(f, xs, y0, eps)

                if method is adams_method:
                    inaccuracy = round(max([abs(exact_y(x, x0, y0) - y) for x, y in zip(xs, new_ys)]), 10)
                else:
                    p = 1 if method is euler_method else 2
                    coef = 2**p - 1
                    inaccuracy = round(abs(new_ys[-1] - ys[-1]) / coef, 10)
                print(round(xs[0], 4), round(xs[-1], 4), inaccuracy)

                ys = new_ys.copy()
            else:
                if iters != 1:
                    print(f"Для точности eps={eps} интервал был разбит на n={ni} "
                          f"частей с шагом h={round((xn - x0) / ni, 6)} за {iters} итераций.\n")
                else:
                    print(f"Для точности eps={eps} интервал был разбит на n={ni} "
                          f"частей с шагом h={round((xn - x0) / ni, 6)}.\n")

                if ni < 100:
                    print("y:\t[", *map(lambda x: round(x, 5), ys), "]")
                    print("y_точн:\t[", *map(lambda x: round(exact_y(x, x0, y0), 5), xs), "]\n")

                if method is adams_method:
                    print(f"Погрешность (max|y_iточн - y_i|): {inaccuracy}")
                else:
                    print(f"Погрешность (по правилу Рунге): {inaccuracy}")

                draw_plot(name, xs, ys, exact_y)

        except OverflowError:
            print('-' * 30 + '\n')
            print("! Невозможно вычислить. Число шагов/точность слишком большая.")


if __name__ == "__main__":
    solve(*get_params())
