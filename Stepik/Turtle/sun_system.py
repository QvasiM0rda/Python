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


planets = { 'Солнце': [250, 'yellow'], 'Меркурий': [50, 'brown'], 'Венера': [100, 'brown'], 'Земля': [75, 'green'],
            'Марс': [40, 'red'], 'Юпитер': [150, 'brown'], 'Сатурн': [140, 'brown'], 'Уран': [120, 'light blue'],
            'Нептун': [100, 'blue'], 'Плутон': [25, 'brown'] }

change_position(-400, 0)
for k, v in planets.items():
    x = xcor() - v[0] / 2
    y = ycor() - v[0] / 2
    change_position(x, y)
    planet(v[0], v[1], k)
