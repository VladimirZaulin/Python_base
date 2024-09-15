# -*- coding: utf-8 -*-
from timeit import default_repeat


# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __init__(self):
        self.temperature = 10
        self.dirtiness = 0
        self.damage = 0
        self.gravity = 1

    def __str__(self):
        return ('Вода плещется в озерке, её температура {} градусов, '
                'загрязнена на {} процентов, наносит {} урона, {} притяжения к земле'.format(
            self.temperature, self.dirtiness, self.damage, self.gravity))

    def __add__(self, other):
        if isinstance(other, Air):
           return Storm()
        if isinstance(other, Fire):
           return Steam()
        if isinstance(other, Ground):
            return Dirt()




class Air:
    def __init__(self):
        self.temperature = 16
        self.dirtiness = 1
        self.damage = 0
        self.gravity = -1

    def __str__(self):
        return ('Воздух не плох в этих местах, температура {} градусов, '
                'загрязнен на {} процентов, наносит {} урона, {} притяжения к земле'.format(
            self.temperature, self.dirtiness, self.damage, self.gravity))

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Ground):
            return Dust()


class Fire:
    def __init__(self):
        self.temperature = 500
        self.dirtiness = 0
        self.damage = 100
        self.gravity = 0

    def __str__(self):
        return ('Огонь горит в глазах, его температура {} градусов, '
                'загрязнен на {} процентов, наносит {} урона, {} притяжения к земле'.format(
            self.temperature, self.dirtiness, self.damage, self.gravity))
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Air):
           return Lightning()
        if isinstance(other, Ground):
           return Lava()


class Ground:
    def __init__(self):
        self.temperature = 5
        self.dirtiness = 100
        self.damage = 15
        self.gravity = 2

    def __str__(self):
        return ('Земля в раскопанной яме, её температура {} градусов, '
                'загрязнена на {} процентов, наносит {} урона, {} притяжения к земле'.format(
            self.temperature, self.dirtiness, self.damage, self.gravity))
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()

class Storm:
    def __init__(self):
        self.temperature = 10
        self.dirtiness = 100
        self.damage = 150
        self.gravity = 0

    def __str__(self):
        return ('Поднимается могучая буря, её температура {} градусов, '
                'загрязнена на {} процентов, наносит {} урона, {} притяжения к земле'.format(
            self.temperature, self.dirtiness, self.damage, self.gravity))



class Steam:
    def __init__(self):
        self.temperature = 100
        self.dirtiness = 0
        self.damage = 500
        self.gravity = 0

    def __str__(self):
        return ('Пар пышит пышно, его температура {} градусов, '
                'загрязнен на {} процентов, наносит {} урона, {} притяжения к земле'.format(
            self.temperature, self.dirtiness, self.damage, self.gravity))



class Dirt:
    def __init__(self):
        self.temperature = 10
        self.dirtiness = 500
        self.damage = 14
        self.gravity = 1

    def __str__(self):
        return ('Грязь, её температура {} градусов, '
                'загрязнена на {} процентов, наносит {} урона, {} притяжения к земле'.format(
            self.temperature, self.dirtiness, self.damage, self.gravity))

class Lightning:
    def __init__(self):
        self.temperature = 5000
        self.dirtiness = 0
        self.damage = 1000
        self.gravity = 0

    def __str__(self):
        return ('Магическая молния, её температура {} градусов, '
                'загрязнена на {} процентов, наносит {} урона, {} притяжения к земле'.format(
            self.temperature, self.dirtiness, self.damage, self.gravity))



class Dust:
    def __init__(self):
        self.temperature = 20
        self.dirtiness = 200
        self.damage = 30
        self.gravity = 0

    def __str__(self):
        return ('Пыль проникает повсюду, её температура {} градусов, '
                'загрязнена на {} процентов, наносит {} урона, {} притяжения к земле'.format(
            self.temperature, self.dirtiness, self.damage, self.gravity))



class Lava:
    def __init__(self):
        self.temperature = 10000
        self.dirtiness = 100
        self.damage = 100000
        self.gravity = 40

    def __str__(self):
        return ('Лава никого не оставит равнодушным, её температура {} градусов, '
                'загрязнена на {} процентов, наносит {} урона, {} притяжения к земле'.format(
            self.temperature, self.dirtiness, self.damage, self.gravity))





drops = Water()
flow = Air()
matches = Fire()
sand = Ground()

print('Вода + Воздух', '=', drops + flow)
print('Вода + Огонь', '=', drops + matches)
print('Вода + Земля', '=', drops + sand)#   Вода + Земля = Грязь
print('Воздух + Огонь', '=', flow + matches)#   Воздух + Огонь = Молния
print('Воздух + Земля', '=', flow + sand)#   Воздух + Земля = Пыль
print('Огонь + Земля', '=', matches + sand)#   Огонь + Земля = Лава



# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым. Water, Air, Fire, Ground, Storm, Steam, Dirt, Lightning, Dust, Lava
