# -*- coding: utf-8 -*-


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
        if isinstance(self, Air):
            return Storm.__str__
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
    def __radd__(self, other):
         if isinstance(self, Water):
             return Storm.__str__
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
    # def __add__(self, other):
    #     return
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
    # def __add__(self, other):
    #     return
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
    # def __add__(self, other):
    #     return
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
    # def __add__(self, other):
    #     return
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
    # def __add__(self, other):
    #     return
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
    # def __add__(self, other):
    #     return

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
    # def __add__(self, other):
    #     return
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
    # def __add__(self, other):
    #     return
# class CraftingTable:
#     def __init__(self):
#         self.temperature = 0
#         self.dirtiness = 0
#         self.damage = 0
#         self.gravity = 0
#         Storm() = Water() + Air()  # Вода + Воздух = Шторм
#         Steam() = Water() + Fire()  # Вода + Огонь = Пар
#         Dirt() = Water() + Ground()  # Вода + Земля = Грязь
#         Lightning() = Water() + Fire()  # Воздух + Огонь = Молния
#         Dust() = Ground() + Air()  # Воздух + Земля = Пыль
#         Lava() = Ground() + Fire()  # Огонь + Земля = Лава
#     def __add__(self,other):


drops = Water()
flow = Air()
matches = Fire()
sand = Ground()

print(Water(), '+', Air(), '=', Water() + Air())

# bottle = Water()
# print(bottle.__str__())
# suburban_air = Air()
# print(suburban_air)
# print('bottle' '+' 'suburban_air')
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым. Water, Air, Fire, Ground, Storm, Steam, Dirt, Lightning, Dust, Lava
