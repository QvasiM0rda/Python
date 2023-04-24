from turtle import *

def change_position(x, y):
    penup()
    goto(x, y)
    pendown()


def square(side: int, color = 'white') -> None:
    fillcolor(color)
    begin_fill()
    for _ in range(4):
        forward(side)
        right(90)
    end_fill()


speed(0)
change_position(-160, 160)
square(320)

colors = ['black', 'white']
for _ in range(8):
    for i in range(8):
        square(40, colors[i % 2])
        change_position(xcor() + 40, ycor())
    colors[0], colors[1] = colors[1], colors[0]
    change_position(-160, ycor() - 40)
    
