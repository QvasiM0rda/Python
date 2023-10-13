import random


class Dice:
    def __init__(self, sides):
        self.sides = sides


    def __call__(self):
        return random.randrange(1, self.sides + 1)


kingdice = Dice(10)

print(kingdice() in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


print(kingdice() in [11, 12, 13, 14])
