# -*- coding: utf-8 -*-

import simple_draw as sd
from simple_draw import random_number

point_0 = sd.get_point(300,30)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
def draw_branches(point=point_0, angle=90, length=100, delta=30):
    if length < 1:
       return
    v1 = sd.get_vector(point,angle,length,2)
    v1.draw()
    v2 = sd.get_vector(point,angle,length,2)
    v2.draw()
    pass
    point = v1.end_point
    angle = angle - delta
    length = length * .75
    v3 = sd.get_vector(point, angle, length, 2)
    v3.draw()
    pass
    point = v2.end_point
    angle = angle + 2 * delta - sd.random_number(5,30)
    v4 = sd.get_vector(point, angle, length, 2)
    v4.draw()
    pass
    if length > 10:
        draw_branches(point=v3.end_point, angle=angle - sd.random_number(1,5), length = length * .75, delta=delta)
        draw_branches(point=v4.end_point, angle=angle + sd.random_number(1,5), length = length * .75, delta=delta)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

draw_branches()

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


