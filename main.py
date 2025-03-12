import math

import numpy as np

from dto.equation import Equation
from methods.newton_method import NewtonMethod
from methods.simple_iterations_method import SimpleIterationsMethod
from methods.chord_method import ChordMethod

import system_of_equation
import user_interaction

methods = {
    1: ChordMethod,
    2: SimpleIterationsMethod,
    3: NewtonMethod
}

available_functions = {
    1: Equation(lambda x: (-1.38 * x ** 3 - 5.42 * x ** 2 + 2.57 * x + 10.95), '-1.38*x^3 - 5.42*x^2 + 2.57*x + 10.95'),
    2: Equation(lambda x: (x ** 3 - 1.89 * x ** 2 - 2 * x + 1.76), 'x^3 - 1.89*x^2 - 2*x + 1.76'),
    3: Equation(lambda x: (-x / 2 + math.e ** x + 5 * np.sin(x)), '-x/2 + e^x + 5*sin(x)'),
}

while True:
    equation_type = user_interaction.get_task()

    if equation_type == 1:
        function = user_interaction.get_equation(available_functions)
        try:
            function.draw(-10, 10)
        except Exception as e:
            print('(!) Не удалось построить график функции, ', e)
            continue

        method_number = user_interaction.get_method_number(methods)

        while True:
            if method_number == 3:
                left, eps, decimal_places = user_interaction.get_initial_newton()
                right = 0
            else:
                left, right, eps, decimal_places = user_interaction.get_initial()

            method = methods[method_number](function, left, right, eps, decimal_places)
            try:
                verified, reason = method.check()
            except TypeError as te:
                print('(!) Ошибка при вычислении значения функции. Возможно, она не определена на всем интервале.')
                continue
            if not verified:
                print('(!) Введенные данные не подходят выбранному методу.', reason)
            break

        try:
            function.draw(left, right)
        except Exception as e:
            print('(!) Не удалось построить график функции.', e)
            continue

        output_file_name = input("Введите имя файла для вывода результата или пустую строку, чтобы вывести в консоль: ")

        try:
            print('Решение: ')
            result = method.solve()
        except Exception as e:
            print('(!) Что-то пошло не так при решении: ', e)
            continue

        user_interaction.print_result(result, output_file_name)
        function.draw_with_point(-10, 10, [result.root, result.function_value_at_root])
    else:
        system_of_equation.run()
    break

print('Программа завершена успешно')
