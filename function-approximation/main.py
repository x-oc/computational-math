import inspect
from math import sqrt
import sys

from approximation.cubic_approximation import CubicApproximation
from approximation.exponential_approximation import ExponentialApproximation
from approximation.linear_approximation import LinearApproximation
from approximation.logarithmic_approximation import LogarithmicApproximation
from approximation.power_approximation import PowerApproximation
from approximation.quadratic_approximation import QuadraticApproximation
from user_interaction import get_x_y_n
from plots import draw_plot, draw_func


def get_pearson_correlation(x, y, n):
    av_x = sum(x) / n
    av_y = sum(y) / n
    return sum((x - av_x) * (y - av_y) for x, y in zip(x, y)) / \
        sqrt(sum((x - av_x) ** 2 for x in x) * sum((y - av_y) ** 2 for y in y))


def get_mean_squared_error(x, y, fi, n):
    return sqrt(sum(((fi(xi) - yi) ** 2 for xi, yi in zip(x, y))) / n)


def get_measure_of_deviation(x, y, fi):
    epss = [fi(xi) - yi for xi, yi in zip(x, y)]
    return sum((eps ** 2 for eps in epss))


def get_coefficient_of_determination(xs, ys, fi, n):
    av_fi = sum(fi(x) for x in xs) / n
    return 1 - sum((y - fi(x)) ** 2 for x, y in zip(xs, ys)) / sum((y - av_fi) ** 2 for y in ys)


def get_str_presentation(func):
    str_func = inspect.getsourcelines(func)[0][0]
    return str_func.split('lambda x: ')[-1].split(',')[0].strip()


def get_coefficients_str(coeffs):
    if len(coeffs) == 2:
        return '(a, b)'
    if len(coeffs) == 3:
        return '(a, b, c)'
    if len(coeffs) == 4:
        return '(a, b, c, d)'
    return '(a, b, c, d, e)'


def get_pir_status(correlation):
    rc = abs(correlation)
    if rc < 0.05:
        pir_status = 'связь между переменными отсутствует'
    elif rc < 0.3:
        pir_status = 'связь слабая'
    elif rc < 0.5:
        pir_status = 'связь умеренная'
    elif rc < 0.7:
        pir_status = 'связь заметная'
    elif rc < 0.9:
        pir_status = 'связь высокая'
    elif rc <= 0.99:
        pir_status = 'связь весьма высокая'
    else:
        pir_status = 'строгая линейная функциональная зависимость'
    return pir_status


def get_r2_status(r2):
    if r2 >= 0.95:
        r2_status = 'высокая точность аппроксимации'
    elif r2 >= 0.75:
        r2_status = 'удовлетворительная точность аппроксимации'
    elif r2 >= 0.5:
        r2_status = 'слабая точность аппроксимации'
    else:
        r2_status = 'точность аппроксимации недостаточна'
    return r2_status


def run(functions, x, y, n):
    best_mse = float("inf")
    best_func = None

    for function in functions:
        approximation = function.get
        name = function.name
        try:
            fi, *coeffs = approximation(x, y, n)

            s = get_measure_of_deviation(x, y, fi)
            mse = get_mean_squared_error(x, y, fi, n)
            r2 = get_coefficient_of_determination(x, y, fi, n)
            r2_status = get_r2_status(r2)

            if mse <= best_mse:
                best_mse = mse
                best_func = name

            draw_func(fi, name, x)

            print(f"{name} функция:")
            print(f"*  Функция: f(x) =", get_str_presentation(fi))
            print(f"*  Коэффициенты {get_coefficients_str(coeffs)}: {list(map(lambda cf: round(cf, 4), coeffs))}")
            print(f"*  Среднеквадратичное отклонение: σ = {mse:.5f}")
            print(f"*  Коэффициент детерминации: R^2 = {r2:.5f}, {r2_status}")
            print(f"*  Мера отклонения: S = {s:.5f}")
            if approximation == LinearApproximation.get:
                correlation = get_pearson_correlation(x, y, n)
                pir_status = get_pir_status(correlation)
                print(f"*  Коэффициент корреляции Пирсона: r = {correlation}, ({pir_status})")

        except Exception as e:
            print(f"Ошибка приближения {name} функции: {e}\n")

        print('\n' + ('-' * 40) + '\n')

    print(f"Лучшая аппроксимирующая функция: {best_func}")
    draw_plot(x, y)


def main():
    x, y, n = get_x_y_n()

    if all(map(lambda xi: xi > 0, x)):
        if all(map(lambda yi: yi > 0, y)):
            functions = [
                LinearApproximation,
                QuadraticApproximation,
                CubicApproximation,
                ExponentialApproximation,
                LogarithmicApproximation,
                PowerApproximation
            ]
        else:
            functions = [
                LinearApproximation,
                QuadraticApproximation,
                CubicApproximation,
                LogarithmicApproximation
            ]
    else:
        if all(map(lambda yi: yi > 0, y)):
            functions = [
                LinearApproximation,
                QuadraticApproximation,
                CubicApproximation,
                ExponentialApproximation
            ]
        else:
            functions = [
                LinearApproximation,
                QuadraticApproximation,
                CubicApproximation
            ]

    with open('out.txt', 'w') as output:
        option = input("Куда выводим? 'f' - файл, 't' - терминал: ")
        if option == 'f':
            print("Выбран вывод в файл 'out.txt'")
            sys.stdout = output
        else:
            print('\n' + ('-' * 30) + '\n')

        run(functions, x, y, n)


if __name__ == "__main__":
    main()
