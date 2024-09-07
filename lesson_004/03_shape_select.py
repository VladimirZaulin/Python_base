# -*- coding: utf-8 -*-

import simple_draw as sd
from simple_draw import COLOR_YELLOW

point = sd.get_point(250, 250)
color = COLOR_YELLOW


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
def choose_figure():
    print('Введите фигуру или её номер для отображения:',
      'Треугольник - 1,',
      'Квадрат - 2,',
      'Пятиугольник - 3,',
      'Шестиугольник - 4')
    user_input = input()
    if user_input == '1' or user_input == 'Треугольник':
        triangle(point, 23, 160, color=color)
        return
    if user_input == '2' or user_input == 'Квадрат':
        square(point, 160, 100, color=color)
        return
    if user_input == '3' or user_input == 'Пятиугольник':
        five_angles(point, 142, 40, color=color)
        return
    if user_input == '4' or user_input == 'Шестиугольник':
        six_angles(point, 24, 55, color=color)
        return
    else:
        choose_figure()
#Вызов функций

choose_figure()
# dict = {
#     1:[triangle(point, 23, 160, color=color)],
#     2:[six_angles(point, 24, 55,color=color)],
#     3:[square(point, 160, 100,color=color)],
#     4:[five_angles(point, 142, 40,color=color)]}
#
# a = dict[int(input())]



# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg



sd.pause()
