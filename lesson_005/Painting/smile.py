# -*- coding: utf-8 -*-
from random import random, randrange

# (определение функций)
import simple_draw
from simple_draw import resolution, get_point, rectangle, COLOR_YELLOW, circle, COLOR_BLUE, ellipse, COLOR_RED, \
    random_color

simple_draw.resolution = (1200, 600)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: коoрдината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
# x = 500
# y = 500
# color = COLOR_YELLOW

def square_smile(x, y, color):
    base_point = get_point(x, y)
    rectangle(base_point, get_point(x + 100, y + 100), color, 3)
    x += 75
    y += 65
    circle(get_point(x, y), 10, color, 3)
    x -= 50
    circle(get_point(x, y), 10, color, 3)
    y -= 40
    ellipse(get_point(x, y), get_point(x + 50, y + 7), color, 6)

# square_smile(200,300,COLOR_RED)

# for _ in range(10):
#     x = randrange(1, 1200)
#     print(x)
#     y = randrange(1, 600)
#     color = random_color()
#     square_smile(x=x,y=y,color=color)

simple_draw.pause()
