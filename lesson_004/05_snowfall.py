# -*- coding: utf-8 -*-
from unicodedata import numeric

import simple_draw as sd
from simple_draw import snowflake, random_number

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


N = 20

def flying_snowflakes(length=20):
    sd.start_drawing()
    flakes_box = []
    while len(flakes_box) < length:
        flakes_box.append(sd.random_number(10,50))
    for length in flakes_box:
        x = sd.random_number(50, 750)
        y = 600
        while True:
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
            sd.snowflake(center=point, length=length, color=sd.background_color)
            y -= 10
            if y < 20:
                break
            x += 0 + sd.random_number(-10,10)
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
            sd.sleep(0.1)
            sd.finish_drawing()
            if sd.user_want_exit():
                return

flying_snowflakes()

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()





sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


