def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            x = []
            y = []
            for line in file:
                point = line.strip().split()
                if len(point) == 2:
                    x.append(float(point[0]))
                    y.append(float(point[1]))

        return x, y, None
    except IOError as err:
        return None, None, "! Невозможно прочитать файл {0}: {1}".format(filename, err)


def read_data_from_console():
    str = ' '
    x = []
    y = []
    while str:
        str = input()
        point = str.strip().split()
        if len(point) == 2:
            x.append(float(point[0]))
            y.append(float(point[1]))
        else:
            if str:
                print("! Некорректный ввод. Введенная точка не будет использована.")
    return x, y


def get_x_y_n():
    while True:
        option = input("Откуда вводим? 'f' - из файла, 't' - из терминала: ")
        if option == 'f':
            while True:
                filename = input("Введите имя файла: ")
                x, y, error = read_data_from_file(filename)
                if error is not None:
                    print(error)
                    continue
                else:
                    break
            n = len(x)
            break
        elif option == 't':
            print("Чтобы закончить ввод, введите Enter")
            x, y = read_data_from_console()
            n = len(x)
            break
        else:
            print("! Некорректный ввод. Попробуйте еще раз")
    return x, y, n
