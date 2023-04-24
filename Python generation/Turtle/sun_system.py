from turtle import *

def change_position(x, y):
    penup()
    goto(x, y)
    pendown()


def planet(size, color, name):
    fillcolor(color)
    begin_fill()
    circle(size)
    end_fill()
    write(name)


planets = { 'Солнце': [150, 'yellow'], 'Меркурий': [50, 'brown'], 'Венера': [90, 'brown'], 'Земля': [75, 'green'],
            'Марс': [40, 'red'], 'Юпитер': [120, 'brown'], 'Сатурн': [110, 'brown'], 'Уран': [110, 'light blue'],
            'Нептун': [85, 'blue'], 'Плутон': [25, 'brown'] }

change_position(-900, 0)
for k, v in planets.items():
    x = xcor() + v[0]
    y = ycor() - v[0]
    change_position(x, y)
    planet(v[0], v[1], k)
    x = xcor() + v[0] + 10
    y = 0
    change_position(x, y)
