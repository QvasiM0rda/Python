def fill_matrix(rows):
    return [[int(i) for i in input().split()] for _ in range(rows)]

def add_matrix(matrix1, matrix2, rows, cols):
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(*row)

n, m = map(int, input().split())
matrix1 = fill_matrix(n)
input()
matrix2 = fill_matrix(n)
print_matrix(add_matrix(matrix1, matrix2, n, m))
