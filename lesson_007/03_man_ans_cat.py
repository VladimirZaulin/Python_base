# -*- coding: utf-8 -*-

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def watch_MTV(self):
        print('{} смотрел MTV целый день'.format(self.name))
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
        else:
            print('{} деньги кончились!'.format(self.name))

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} Вьехал в дом'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        if self.fullness < 20:
            self.eat()
        elif self.house.money <= 150:
            self.work()
        elif self.house.food < 50:
            self.shopping()
        elif self.house.cat_food < 30:
            self.by_cat_food()

        else:
            dice = randint(1, 6)
            if dice == 1:
                self.work()
            elif dice == 2:
                self.eat()
            else:
                self.watch_MTV()
    def take_cat(self, house, other):
        Cat.house = self.house
        self.fullness -= 10
        print('{} Взял домой котика, по имени {}'.format(self.name,other.name))
    def by_cat_food(self):
        if self.house.money >= 50:
            print('{} Заказал еды котику'.format(self.name))
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            print('{} деньги кончились!'.format(self.name))

    def clean_up(self):
        if self.house.dirt >= 20:
            print('Пора прибраться, {}!'.format(self.name))
            self.fullness -= 20
            self.house.dirt -= 100
    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        # self.house = None

    def __str__(self):
        return 'МЯУ - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            print('{} нет еды'.format(self.name))
    def play(self):
        print('{} порвал обои'.format(self.name))
        self.house.dirt += 5
        self.fullness -= 10
    def sleep(self):
        print('{} мяу, мяу, пора баиньки zzz...'.format(self.name))
        self.fullness -= 10
    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        if self.fullness <= 10:
            self.eat()
        elif self.house.dirt == 0:
            self.play()
        elif self.house.money < 50:
            self.sleep()
        elif dice == 1:
            self.play()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.dirt = 0
        self.cat_food = 0

    def __str__(self):
        return ('В доме еды осталось {}, денег осталось {}, грязь {}, вискас {}'.format(self.food,
                                                                                        self.money, self.dirt,
                                                                                        self.cat_food))


host = Man(name='Хозяин')
my_sweet_home = House()
host.go_to_the_house(house=my_sweet_home)
cat = Cat('Базилио')
host.take_cat(my_sweet_home, cat)
fam = [host,cat]



for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for homer in fam:
        homer.act()

    print('--- в конце дня ---')
    for homer in fam:
        print(homer)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
