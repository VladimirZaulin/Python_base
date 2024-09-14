# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class SnowFlake:
    pass

    def __init__(self):
        self.length = randint(20,50)
        self.shift = randint(0,250)
        self.color = sd.COLOR_WHITE
        SnowFlake.quantity = 20
        self.x = 300
        self.y = 600
        self.point = sd.get_point(self.x,self.y)
        self.transparent = sd.background_color
    def draw(self):
        sd.start_drawing()
        sd.snowflake(center=self.point, length=self.length, color=self.color)
        sd.finish_drawing()

    def clear_previous_picture(self):
        sd.start_drawing()
        sd.snowflake(center=self.point, length=self.length, color=self.transparent)
        sd.finish_drawing()

    def move(self):
        while True:
            self.draw()
            self.clear_previous_picture()
            self.y -= 10
            self.x += 0 + sd.random_number(-10, 10)
            self.point = sd.get_point(self.x, self.y)
            self.draw()
            sd.sleep(0.1)
            sd.finish_drawing()
            if sd.user_want_exit():
                break



flake = SnowFlake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    # if not flake.can_fall():
    #     break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
