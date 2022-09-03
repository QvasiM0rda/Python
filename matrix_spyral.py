# Заполнение строки
def fill_ver(matrix, start, finish, step, num, row):
    for i in range(start, finish, step):
        matrix[row][i] = num
        num += 1
    return num

# Заполнение столбца
def fill_hor(matrix, start, finish, step, num, col):
    for i in range(start, finish, step):
        matrix[i][col] = num
        num += 1
    return num

# Заполнение всей матрицы
def fill_matrix(matrix, rows, cols):
    first_row, last_row = 0, rows
    first_col, last_col = 0, cols
    num = 1
    for i in range(rows * cols):
        if num > rows * cols:
            break
        if i % 4 == 0: # Первая строка, слева на право
            num = fill_ver(matrix, first_col, last_col, 1, num, first_row)
            first_row += 1
        if i % 4 == 1: # Последний столбец, сверху вниз
            num = fill_hor(matrix, first_row, last_row, 1, num, last_col - 1)
            last_col -= 1
        if i % 4 == 2: # Последняя строка, справа налево
            num = fill_ver(matrix, last_col - 1, first_col - 1, -1, num, last_row - 1)
            last_row -= 1
        if i % 4 == 3: # Первый столбец, сниху вверх
            num = fill_hor(matrix, last_row - 1, first_row - 1, -1, num, first_col)
            first_col += 1

def print_matrix():
    n, m = map(int, input().split())    
    matrix = [[0] * m for _ in range(n)]
    fill_matrix(matrix, n, m)
    
    for row in matrix:
        for elem in row:
            print(str(elem).ljust(3), end='')
        print()

print_matrix()
