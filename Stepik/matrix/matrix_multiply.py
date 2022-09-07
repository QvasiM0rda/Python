def fill_matrix(rows: int) -> list :
    """ Возвращает матрицу, заполненную данными, введёнными пользователем """
    return [[int(i) for i in input().split()] for _ in range(rows)]

def mult_matrix(matrix1: list, matrix2: list, rows1: int, cols1: int, cols2: int) -> list:
    """ Вовзращает результат умножения двух матриц """
    result = [[0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols1):
            for k in range(cols2):
                result[i][k] += matrix1[i][j] * matrix2[j][k]

    return result

def print_matrix(matrix : list):
    """ Печатает матрицу """
    for row in matrix:
        print(*row)

n, m = map(int, input().split())
matrix_1 = fill_matrix(n)
input()
m, k = map(int, input().split())
matrix_2 = fill_matrix(m)
print_matrix(mult_matrix(matrix_1, matrix_2, n, m, k))
