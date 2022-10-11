from turtle import *
from random import randint
colormode(255)
from math import tan, radians, sqrt

def change_position(x, y):
    penup()
    goto(x, y)
    pendown()

def polygon(color: set, sides: int, size: int, angle: int) -> None:
    fillcolor(color)
    begin_fill()
    for _ in range(sides):
        forward(size)
        right(angle)
    end_fill()


change_position(-200, 200)
square = randint(200, 500)

for _ in range(5):
    for _ in range(5):
        sides = randint(3, 10)
        angle = 360 / sides
        size = sqrt((square * 4 * tan(radians(180) / sides)) / sides)
        color = {randint(0, 255), randint(0, 255), randint(0, 255)}
        polygon(color, sides, size, angle)
        change_position(xcor() + 50, ycor())
    change_position(-200, ycor() - 50)
