import math

from function import get_some_functions
from methods.rectange_middle_method import RectangleMiddleMethod
from methods.rectangle_left_method import RectangleLeftMethod
from methods.rectangle_right_method import RectangleRightMethod
from methods.simpson_method import SimpsonMethod
from methods.trapezoid_method import TrapezoidMethod
from user_interaction import get_function, get_integration_limit, get_epsilon, print_result

METHODS = {
    RectangleLeftMethod(),
    RectangleMiddleMethod(),
    RectangleRightMethod(),
    TrapezoidMethod(),
    SimpsonMethod()
}
MAX_BREAKPOINTS = 10_000


def get_break_points(function, a, b, n):
    breakpoints = []

    try:
        function.func(a)
    except (ZeroDivisionError, OverflowError, ValueError):
        breakpoints.append(a)

    try:
        function.func(b)
    except (ZeroDivisionError, OverflowError, ValueError):
        breakpoints.append(b)

    try:
        function.func((a + b) / 2)
    except (ZeroDivisionError, OverflowError, ValueError):
        breakpoints.append((a + b) / 2)

    h = (b - a) / n
    for i in range(n):
        point = a + i * h
        try:
            function.func(a + i * h)
        except (ZeroDivisionError, OverflowError, ValueError):
            breakpoints.append(point)

            if len(breakpoints) >= MAX_BREAKPOINTS:
                return get_break_points(function, a, b, n // 10)

    return list(set(breakpoints))


def compute_integral(function, a, b, eps, method):
    n = 4
    result = method.compute(function, a, b, n)
    error = math.inf

    while error > eps:
        n *= 2
        new_result = method.compute(function, a, b, n)
        error = abs(new_result - result) / method.runge_coef
        result = new_result

    return result, n


def get_convergence(function, breakpoints, eps):
    for bp in breakpoints:
        y1 = function.try_to_compute(bp - eps)
        y2 = function.try_to_compute(bp + eps)
        if y1 is not None and y2 is not None and abs(y1 - y2) > eps and abs(y1 + y2) > eps:
            print(y1, y2)
            return False
    return True


def process_method(method, function, a, b, epsilon):
    print(method.name + ":")
    result, n = compute_integral(function.func, a, b, epsilon, method)

    if result is not None and n is not None:
        print_result(result, n)


def process_method_for_discontinuous_func(method, breakpoints, a, b, eps, function, epsilon):
    print(method.name + ":")

    if len(breakpoints) == 1:
        if a in breakpoints:
            a += eps
        elif b in breakpoints:
            b -= eps
        result, n = compute_integral(function.func, a, b, epsilon, method)
        if result is not None and n is not None:
            print_result(result, n)
    else:
        res = 0
        n = 0
        if not (function.try_to_compute(a) is None or
                function.try_to_compute(breakpoints[0] - eps) is None):
            results = compute_integral(function.func, a, breakpoints[0] - eps, epsilon, method)
            res += results[0]
            n += results[1]

        if not (function.try_to_compute(b) is None or
                function.try_to_compute(breakpoints[0] + eps) is None):
            results = compute_integral(function.func, breakpoints[0] + eps, b, epsilon, method)
            res += results[0]
            n += results[1]

        for bi in range(len(breakpoints) - 1):
            b_cur = breakpoints[bi]
            b_next = breakpoints[bi + 1]

            if not (function.try_to_compute(b_cur + eps) is None or
                    function.try_to_compute(b_next - eps) is None):
                results = compute_integral(function.func, b_cur + eps, b_next - eps, epsilon, method)
                res += results[0]
                n += results[1]

        print_result(res, n)


def main():
    functions = get_some_functions()
    function = get_function(functions)
    a, b = get_integration_limit()
    breakpoints = get_break_points(function, a, b, math.ceil(b - a) * 1_000)

    if len(breakpoints) != 0:
        # есть разрыв => установить сходимость
        print(f"! Обнаружена точка разрыва: функция имеет разрыв или не существует в точках {breakpoints}.")

        eps = 0.00001
        converges = get_convergence(function, breakpoints, eps)

        if not converges:
            # расходящийся => Интеграл не существует
            print('- Интеграл не существует: интеграл расходится.')
        else:
            # сходящийся => вычисление несобственных интегралов 2 рода
            print('+ Интеграл сходится.')
            epsilon = get_epsilon()

            for method in METHODS:
                process_method_for_discontinuous_func(method, breakpoints, a, b, eps, function, epsilon)

    else:
        # нет разрыва => просто вычисляем
        epsilon = get_epsilon()

        for method in METHODS:
            process_method(method, function, a, b, epsilon)


if __name__ == '__main__':
    main()
