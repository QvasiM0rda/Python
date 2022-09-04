def fill_matrix(rows):
    return [[int(i) for i in input().split()] for _ in range(rows)]

# Доработать
def mult_matrix(matrix1, matrix2, rows1, cols1, rows2, cols2):
    pass

def print_matrix(matrix):
    for row in matrix:
        print(*row)

n, m = map(int, input().split())
matrixA = fill_matrix(n)
input()
m, k = map(int, input().split())
matrixB = fill_matrix(m)
print_matrix(mult_matrix(matrixA, matrixB, n, m, m, k))
