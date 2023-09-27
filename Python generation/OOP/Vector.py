class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y


    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


    def do_math(self, other, operator):
        operators = {
            "*": lambda x: x * other,
            "/": lambda x: x / other
        }

        if operator in ["+", "-"] and isinstance(other, Vector):
            return eval(f"Vector(self.x {operator} other.x, self.y {operator} other.y)")
            

        if operator in ["*", "/"] and isinstance(other, (int, float)):
            return Vector(*map(operators[operator], (self.x, self.y)))
        
        return NotImplemented


    def __add__(self, other):
        return self.do_math(other, "+")


    def __sub__(self, other):
        return self.do_math(other, "-")


    def __mul__(self, n):
        return self.do_math(n, "*")


    def __truediv__(self, n):
        return self.do_math(n, "/")


    def __rmul__(self, n):
        return self.__mul__(n)


    def __rtruediv__(self, n):
        return self.__truediv__(n)


a = Vector(1, 2)
b = Vector(3, 4)

print(a + b)
print(a - b)
print(b + a)
print(b - a)

a = Vector(3, 4)

print(a * 2)
print(2 * a)
print(a / 2)
