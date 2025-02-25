def get_matrix():
    while True:
        try:
            n = int(input("Введите размер матрицы: "))
            if n < 1 or n > 20:
                print("Ввод некорректен!")
            else:
                break
        except ValueError:
            print("Ввод некорректен!")
    matrix = []
    print("Введите строки матрицы: ")
    for i in range(n):
        while True:
            try:
                matrix.append([float(x) for x in input().split()])
                break
            except ValueError:
                print("Введена некорректная строка!")
    return matrix


def get_accuracy():
    while True:
        try:
            a = float(input("Введите точность: "))
            if a > 0:
                return
            else:
                print("Ввод некорректен!")
        except ValueError:
            print("Ввод некорректен!")
