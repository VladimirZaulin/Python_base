# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
from simple_draw import COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_BLUE, COLOR_PURPLE, COLOR_CYAN

sd.resolution = (1200, 600)
x = 0


colors = (COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE)
for color in colors:
    first_point = sd.get_point(0 + x, 0)
    second_point = sd.get_point(450 + x, 650)
    x += 50
    line = sd.line(first_point,second_point,color,50)
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

sd.pause()
