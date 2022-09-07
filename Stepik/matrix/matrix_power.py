def fill_matrix(rows):
    """ Возвращает матрицу, заполненную данными, введёнными пользователем """
    return [[int(i) for i in input().split()] for _ in range(rows)]


def mult_matrix(matrix1, matrix2, rows1, cols1, cols2):
    """ Вовзращает результат умножения двух матриц """
    result = [[0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols1):
            for k in range(cols2):
                result[i][k] += matrix1[i][j] * matrix2[j][k]
    return result


def power_matrix(matrix, power, size):
    """ Возводит матрицу в степень """
    result = matrix.copy()
    for _ in range(power - 1):
        result = mult_matrix(result, matrix, size, size, size)
    return result


def print_matrix(matrix):
    """ Печатает матрицу """
    for row in matrix:
        print(*row)


n = int(input())
matrix = fill_matrix(n)
m = int(input())
print_matrix(power_matrix(matrix, m, n))
