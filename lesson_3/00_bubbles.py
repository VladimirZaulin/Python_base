# -*- coding: utf-8 -*-
import random

import simple_draw as sd
from simple_draw import circle, get_point

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей



# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point,step):

    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius, width=4)
point = get_point(200, 200)
bubble(point, 10)


# Нарисовать 10 пузырьков в ряд
#for x in range(100,1101,100):
  #  bubble(point, 10)
   # point = get_point(x, 200)

# Нарисовать три ряда по 10 пузырьков
#for y in range(1,301,100):
 #   for x in range(100,1101,100):
  #      bubble(point, 10)
   #     point = get_point(x, y)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(1,10)
    bubble(point,step)


sd.pause()


