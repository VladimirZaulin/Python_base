# -*- coding: utf-8 -*-
from operator import getitem

import simple_draw as sd
from pygame.examples.cursors import color_cursor
from simple_draw import COLOR_RED, get_point, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_BLUE, COLOR_CYAN, \
    COLOR_PURPLE


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
point = get_point(250, 250)
my_list = [COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE]
print('Print which color do you like from 0 to 6:' )
color = my_list[int(input())]

print(color)
# - треугольник
def triangle(point=point, angle=34, length=200, color=color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color = color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw(color = color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw(color = color)

# - квадрата

def square(point=point, angle=100, length=200,color=color):
    real_angle = 90 - angle
    v1 = sd.get_vector(start_point=point, angle=90 + real_angle, length=length, width=3,)
    v1.draw(color = color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=180 + real_angle, length=length, width=3)
    v2.draw(color = color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=-90 + real_angle, length=length, width=3)
    v3.draw(color = color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=360 + real_angle, length=length, width=3)
    v1.start_point = v4.end_point
    v4.draw(color = color)

# - пятиугольника

def five_angles(point = point, angle=72, length=200, color=color):
    real_angle = 72 - angle
    v1 = sd.get_vector(start_point=point, angle=72+real_angle, length=length, width=3)
    v1.draw(color = color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=144 + real_angle, length=length, width=3)
    v2.draw(color = color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=72 * 3 + real_angle, length=length, width=3)
    v3.draw(color = color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=72 * 4 + real_angle, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=72 * 5 + real_angle, length=length, width=3)
    v5.draw(color = color)

# - шестиугольника

def six_angles(point=point, angle=60, length=200, color = color):
    real_angle = 60 - angle
    v1 = sd.get_vector(start_point=point, angle=60  + real_angle, length=length, width=3)
    v1.draw(color = color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=120 + real_angle, length=length, width=3)
    v2.draw(color = color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=180  + real_angle, length=length, width=3)
    v3.draw(color = color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=60 * 4  + real_angle, length=length, width=3)
    v4.draw(color = color)
    v5 = sd.get_vector(start_point=v4.end_point, angle=60 * 5  + real_angle, length=length, width=3)
    v5.draw(color = color)
    v6 = sd.get_vector(start_point=v5.end_point, angle=60 * 6  + real_angle,  width=3)
    v6.draw(color=color)



#Вызов функций
triangle(point, 23, 160, color=color)
six_angles(point, 24, 55,color=color)
square(point, 160, 100,color=color)
five_angles(point, 142, 40,color=color)


sd.pause()
