def get_function(functions):
    print("Выберите функцию:")
    for i in range(len(functions)):
        print(str(i + 1) + '.' + functions[i].view)

    while True:
        try:
            chosen_f = int(input()) - 1
            if 0 <= chosen_f < len(functions):
                return functions[chosen_f]
            print("Введите корректный номер функции.\n")
        except:
            print("Ошибка ввода. Введите число - один из предложенных номеров функций.\n")


def get_integration_limit():
    while True:
        try:
            a = float(input("Введите начальный предел интегрирования: "))
            b = float(input("Введите конечный предел интегрирования: "))

            if a >= b:
                print(f'Начальный предел должен быть меньше конечного.\n')
            else:
                return a, b
        except:
            print("Ошибка ввода. Введите корректное рациональное число.\n")


def get_epsilon():
    while True:
        try:
            return float(input("Введите требуемую точность вычислений: "))
        except:
            print("Ошибка ввода.")


def print_result(result, n):
    print(f"Значение интеграла: {result}")
    print(f"Число разбиений интервала интегрирования для достижения требуемой точности: n = {n}")
