# -*- coding: utf-8 -*-

import simple_draw as sd
from simple_draw import circle, get_point

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = get_point(200,200)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(point, radius)

sd.circle(center_position=point)
# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


