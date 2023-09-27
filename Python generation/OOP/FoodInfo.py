class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates


    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"


    def do_math(self, n, operator):
        if not isinstance(n, (int, float)):
            return NotImplemented

        operators = {"*": lambda x: x * n, "/": lambda x: x / n, "//": lambda x: x // n}
        
        return FoodInfo(*map(operators[operator], (self.proteins, self.fats, self.carbohydrates)))


    def __add__(self, other):
        if not isinstance(other, FoodInfo):
            return NotImplemented
        
        return FoodInfo(
            self.proteins + other.proteins,
            self.fats + other.fats,
            self.carbohydrates + other.carbohydrates
        )


    def __mul__(self, n):
        return self.do_math(n, "*")


    def __truediv__(self, n):
        return self.do_math(n, "/")


    def __floordiv__(self, n):
        return self.do_math(n, "//")

food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 10, 20)

print(food1 + food2)
print(food1 * 2)
print(food1 / 2)
print(food1 // 2)

food1 = FoodInfo(10, 20, 30)

try:
    food2 = (5, 10, 15) + food1
except TypeError:
    print('Некорректный тип данных')
