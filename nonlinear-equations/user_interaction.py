from typing import Tuple
import decimal

from dto.equation import Equation


def get_task():
    print("Что будем решать?")
    print('1) Нелинейное уравнение')
    print('2) Система нелинейных уравнений')

    try:
        task_number = int(input("Введите номер задачи: "))
    except ValueError:
        print('(!) Некорректный ввод!')
        return get_task()
    if task_number not in [1, 2]:
        print("(!) Такого номера нет.")
        return get_task()
    return task_number


def get_equation(functions) -> Equation:
    print("Выберите уравнение:")
    for num, func in functions.items():
        print(str(num) + ') ' + func.text)
    try:
        equation_number = int(input("Введите номер уравнения: "))
    except ValueError:
        print('(!) Некорректный ввод!')
        return get_equation(functions)
    if equation_number < 1 or equation_number > len(functions):
        print("(!) Такого номера нет.")
        return get_equation(functions)
    return functions[equation_number]


def get_method_number(methods) -> int:
    print("Выберите метод:")
    for num, mtd in methods.items():
        print(str(num) + ') ' + mtd.name)
    try:
        method_number = int(input("Введите номер метода: "))
    except ValueError:
        print('(!) Некорректный ввод!')
        return get_method_number(methods)
    if method_number < 1 or method_number > len(methods):
        print("(!) Такого номера нет.")
        return get_method_number(methods)
    return method_number


def print_result(result, output_file_name):
    if output_file_name == '':
        print('\n' + str(result))
    else:
        f = open(output_file_name, "w")
        f.write(str(result))
        f.close()
        print('Результат записан в файл.')


def get_initial() -> Tuple[float, float, float, int]:
    while True:
        filename = input("Введите имя файла для загрузки исходных данных и интервала "
                         "или пустую строку, чтобы ввести вручную: ")
        if filename == '':
            left = float(input('Введите левую границу интервала: '))
            right = float(input('Введите правую границу интервала: '))
            eps = input('Введите допустимую погрешность: ')
            break
        else:
            try:
                f = open(filename, "r")
                left = float(f.readline())
                right = float(f.readline())
                eps = f.readline()
                print('Считано из файла:')
                print(f'Левая граница: {left}, правая: {right}, погрешность: {eps}')
                f.close()
                break
            except FileNotFoundError:
                print('(!) Файл для загрузки исходных данных не найден.')

    decimal_places = abs(decimal.Decimal(eps).as_tuple().exponent)
    eps = float(eps)

    return left, right, eps, decimal_places


def get_initial_newton() -> Tuple[float, float, int]:
    while True:
        filename = input("Введите имя файла для загрузки исходных данных и интервала "
                         "или пустую строку, чтобы ввести вручную: ")
        if filename == '':
            x0 = float(input('Введите начальное приближение: '))
            eps = input('Введите погрешность вычисления: ')
            break
        else:
            try:
                f = open(filename, "r")
                x0 = float(f.readline())
                eps = f.readline()
                f.close()
                print('Считано из файла:')
                print(f'Начальное приближение: {x0}, погрешность: {eps}')
                break
            except FileNotFoundError:
                print('(!) Файл для загрузки исходных данных не найден.')

    decimal_places = abs(decimal.Decimal(eps).as_tuple().exponent)
    eps = float(eps)

    return x0, eps, decimal_places


def get_system_of_equations(functions):
    print("Выберите систему уравнений:")
    for key, value in functions.items():
        print(str(key) + ") " + value[1])

    try:
        equations_number = int(input("Введите номер системы: "))
    except ValueError:
        print('(!) Некорректный ввод!')
        return get_system_of_equations(functions)
    if equations_number < 1 or equations_number > len(functions):
        print("(!) Такого номера нет.")
        return get_system_of_equations(functions)
    return equations_number
