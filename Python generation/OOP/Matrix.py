class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows, self.cols = rows, cols
        self._value = value
        self._matrix = [[value for _ in range(cols)] for _ in range(rows)]


    def get_value(self, row, col):
        return self._matrix[row][col]


    def set_value(self, row, col, value):
        self._matrix[row][col] = value


    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"


    def __str__(self):
        result = ""
        for row in self._matrix:
            result += " ".join(str(elem) for elem in row) + "\n"
        return result[:-1]


    def copy_matrix(self, pos=True, invert=False, _round=False, _n=None):
        if invert:
            matrix = Matrix(self.cols, self.rows)
        else:
            matrix = Matrix(self.rows, self.cols)
        
        for i, row in enumerate(self._matrix):
            for j, elem in enumerate(row):
                if _round:
                    elem = round(elem, _n)
                if not pos:
                    elem = -elem
                if invert:
                    matrix.set_value(j, i, elem)
                else:
                    matrix.set_value(i, j, elem)
        return matrix
                
            

    def __pos__(self):
        return self.copy_matrix(self)


    def __neg__(self):
        return self.copy_matrix(pos=False)


    def __invert__(self):
        return self.copy_matrix(invert=True)


    def __round__(self, n=None):
        return self.copy_matrix(_round=True, _n=n)


# TEST_7:
matrix = Matrix(5, 10)

floats = [[7125.900408, 633.354471, -9237.8575119, 2865.3825158, 5509.2609336, 8712.260779, 8317.523947, 2512.4736075,
           -3087.5496014, 3861.68814],
          [-7852.451832, 376.465911, -8142.7867326, -6921.8371407, 3735.7516227, -3322.8019034, 7115.79968,
           -8949.9313078, -7032.4347679, -5217.8236385],
          [-7817.9657992, -4319.716346, -1038.6294521, -2959.8970273, -9263.5713405, 9358.607686, 1429.6576196,
           -9484.68116, 639.6343972, 3444.9938213],
          [-2844.2405153, -2078.2441427, 6812.1367017, 112.3910618, -1116.8662449, 5042.7026276, -5981.6930342,
           4370.9173164, -8851.7648474, 8990.6896422],
          [90.8102435, 5256.6137481, -9743.8477321, -131.5501688, -5920.5976176, 4963.8336619, -4907.3622526,
           8531.2015615, -244.3630074, 3421.8817151]]

for r in range(5):
    for c in range(10):
        matrix.set_value(r, c, floats[r][c])

print(matrix)
print()
print(~matrix)
print()
print(round(matrix, 2))
print()
print(-matrix)

# TEST_8:
matrix = Matrix(2, 3, 1)

round_matrix = round(matrix)
plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(round_matrix is matrix)
print(plus_matrix is matrix)
print(minus_matrix is matrix)
print(invert_matrix is matrix)

# TEST_9:
matrix = Matrix(2, 3, 1)

plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(plus_matrix.cols, plus_matrix.rows)
print(minus_matrix.cols, minus_matrix.rows)
print(invert_matrix.cols, invert_matrix.rows)
