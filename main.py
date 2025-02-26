from diagonal_dominance import make_matrix_diagonal_dominance
from user_interaction import get_matrix, get_accuracy, print_matrix


def solve():
    accuracy = get_accuracy()
    matrix = get_matrix()
    coefs = []
    values = []
    for row in matrix:
        coefs.append(row[:-1])
        values.append(row[-1])
    if not make_matrix_diagonal_dominance(coefs, values):
        print("Матрица не может быть подготовлена для выполнения алгоритма")
        return
    for i in range(len(matrix)):
        matrix[i] = coefs[i] + [values[i]]
    print("Преобразованная матрица:")
    print_matrix(matrix)


if __name__ == '__main__':
    solve()
