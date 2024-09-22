# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
# point = sd.get_point(300, 300)

class CheckParams(BaseException):
    pass

def triangle(point, angle=34, length=200):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()
def square(point, angle=100, length=200):
    real_angle = 90 - angle
    v1 = sd.get_vector(start_point=point, angle=90 + real_angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=180 + real_angle, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=-90 + real_angle, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=360 + real_angle, length=length, width=3)
    v1.start_point = v4.end_point
    v4.draw()
def five_angles(point, angle=72, length=200):
    real_angle = 72 - angle
    v1 = sd.get_vector(start_point=point, angle=72+real_angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=144 + real_angle, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=72 * 3 + real_angle, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=72 * 4 + real_angle, length=length, width=3)
    v4.draw()

    v5 = sd.line(start_point=v4.end_point, end_point=point, width=3)
def six_angles(point, angle=60, length=200):
    real_angle = 60 - angle
    v1 = sd.get_vector(start_point=point, angle=60  + real_angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=120 + real_angle, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=180  + real_angle, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=60 * 4  + real_angle, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=60 * 5  + real_angle, length=length, width=3)
    v5.draw()

    v6 = sd.line(start_point=v5.end_point, end_point=point, width=3)


def get_polygon(n):
    def surrogate(point=0, angle=0, length=0):
        if n == 3:
            return triangle(point, angle, length)
        if n == 4:
            return square(point, angle, length)
        if n == 5:
            return five_angles(point, angle, length)
        if n == 6:
            return six_angles(point, angle, length)
        else:
            raise CheckParams('Кол-во сторон может быть от 3 до 6!')
    return surrogate


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
