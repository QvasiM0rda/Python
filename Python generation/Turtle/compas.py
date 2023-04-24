from turtle import *

directions = ['Восток', 'Юг', 'Запад', 'Север']
penup()
goto(0, -20)
pendown()
circle(20)

for i in range(4):
    penup()
    goto(0, 0)
    pendown()
    forward(200)
    stamp()
    write(directions[i])
    right(90)
