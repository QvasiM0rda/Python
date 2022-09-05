def fill_matrix(rows):
    return [[int(i) for i in input().split()] for _ in range(rows)]

def flip_matrix(matrix, rows, cols):
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

# Доработать
def mult_matrix(matrix1, matrix2, rows1, cols1, rows2, cols2):
    result = [[0] * cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols1):
            for k in range(cols2):
                result[i][j] += matrix1[i][k] * matrix2[j][k]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(*row)

n, m = map(int, input().split())
matrixA = fill_matrix(n)
input()
m, k = map(int, input().split())
matrixB = flip_matrix(fill_matrix(m), m, k)
print_matrix(mult_matrix(matrixA, matrixB, n, m, m, k))
