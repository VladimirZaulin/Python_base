# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd
from simple_draw import clear_screen, user_want_exit


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
        self.point = sd.get_point(self.x+self.shift,self.y)
        self.transparent = sd.background_color
        SnowFlake.count = None
    def draw(self):
        # sd.start_drawing()
        sd.snowflake(center=self.point, length=self.length, color=self.color)
        # sd.finish_drawing()


    def clear_previous_picture(self):
        # sd.start_drawing()
        sd.snowflake(center=self.point, length=self.length, color=self.transparent)
        # sd.finish_drawing()

    def move(self):
        while True:
            self.draw()
            self.clear_previous_picture()
            self.y -= 10
            self.x += 0 + sd.random_number(-10, 10)
            self.point = sd.get_point(self.x, self.y)
            self.draw()
            sd.sleep(0.1)
            if self.y < 50:
                break
            sd.finish_drawing()
            if sd.user_want_exit():
                break



# def get_flakes(count):
#     fl_list = []
#     while len(fl_list) < count:
#         fl_list.append(SnowFlake())
#         print(fl_list, 'упало {} снежинок'.format(count))
#         return fl_list
# def get_fallen_flakes():
#     fallen_flakes = []
#     SnowFlake.fallen_flakes.append(SnowFlake())
#     return fallen_flakes
#
# def append_flakes(SnowFlake):
#     fl_list = get_flakes.fl_list
#     if len(SnowFlake.fl_list) == 0:
#         SnowFlake.fl_list.append(SnowFlake())
#         print(fl_list)
#         return fl_list





# flake = SnowFlake()
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     # if not flake.can_fall():
#     #     break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#     elif flake.y == 0:
#         get_fallen_flakes()
#         print(get_fallen_flakes())


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
def snow_fall(N):
    flakes = [] # создать список снежинок
    while len(flakes) < N:
        flake = SnowFlake()
        flakes.append(flake)
        if user_want_exit():
            break
    if len(flakes) == N:
        print('Список из',N, 'снежинок создан')
    count_fallen = 0
    while count_fallen < N:
        for flake in flakes:
            flake.clear_previous_picture()
            flake.move()
            flake.draw()
            count_fallen +=1  # подcчитать сколько снежинок уже упало
            print('Сейчас упала снежинка')
        if sd.user_want_exit():
            break
    if count_fallen == N:
        print('Снежинки выпали, сейчас добавлю ещё!')
        snow_fall(N=randint(5,10))
        pass



snow_fall(4)
# while len(flakes) < N: # добавить еще сверху
#         extra_flake = SnowFlake()
#         flakes.append(extra_flake)
#         for flake in flakes:
#             flake.clear_previous_picture()
#             flake.move()
#             flake.draw()
#             count_fallen += 1  # подcчитать сколько снежинок уже упало
#             print('Сейчас упала дополнительная снежинка')
#         sd.sleep(0.1)
#         if sd.user_want_exit():
#              break





sd.pause()
