# -*- coding: utf-8 -*-
from encodings import search_function

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.



class House:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.total_money = 0
        self.total_food = 0
        self.total_coats = 0
    def __str__(self):
        return '=== В тайнике {} золотых, {} вкусностей в холодильнике, захламление {} % === '.format(
            self.money,self.food,self.dirt)
    def spoiling(self,other):
        self.dirt += 5
        other.joy -= 5
        print('                                                                                      ')


class Husband:
    def __init__(self, name):
        self.name = name
        self.energy = 30
        self.joy = 100
        self.house = None
    def __str__(self):
        return f'           {self.name}: сытость - {self.energy}, веселье - {self.joy}'
    def act(self):
        self.house.spoiling(self)
        if self.energy <= 0:
            print('{} скончался от голода'.format(self.name))
            return True
        if self.joy <= 0:
            print('{} скончался от тоски'.format(self.name))
            return True
        if self.energy <= 10:
            self.eat()
        elif self.house.money <= 90:
            self.work()
        elif self.house.food <= 0:
            self.work()
        elif self.joy < 35:
            self.gaming()
        else:
            dice = randint(1,6)
            if dice == 1:
                self.eat()
            elif dice == 2:
                self.gaming()
            else:
                self.work()
    def eat(self):
        if self.house.food >= 30:
            print('{} поел'.format(self.name))
            self.energy += 30
            self.house.total_food += 30
            self.house.food -= 30
        elif 0 < self.house.food < 30:
            self.energy +=self.house.food
            self.house.total_food += self.house.food
            self.house.food *= 0
            print('Без обид, но я - {}, я - доем'.format(self.name))
        else:
            print('{} : Нет еды! Купитее'.format(self.name))
            dice = randint(1, 3)
            if dice == 1:
                self.work()
            elif dice == 2:
                self.eat()
            else:
                self.gaming()
    def go_to_the_house(self, house):
        self.house = house
        print('{} Вьехал в дом'.format(self.name))
    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.energy -= 10
        self.house.total_money += 150
    def gaming(self):
        print('{} поиграл катку в WoT'.format(self.name))
        self.energy -= 10
        self.joy += 20


class Wife(Husband):
    def __str__(self):
        return super().__str__()
    def act(self):
        self.house.spoiling(self)
        if self.energy <= 0:
            print('{} скончалась от голода'.format(self.name))
            return True
        if self.joy <= 0:
            print('{} скончалась от тоски'.format(self.name))
            return True
        if self.energy <= 10:
            self.eat()
        elif self.house.food <= 90:
            self.shopping()
        elif self.house.dirt >= 80:
            self.clean_house()
        elif self.joy < 35:
            self.buy_fur_coat()
        else:
            dice = randint(1, 10)
            if dice == 1:
                self.buy_fur_coat()
            elif dice == 2:
                self.shopping()
            elif dice == 3:
                self.eat()
            else:
                self.clean_house()
    def eat(self):
        if self.house.food >= 10:
            print('{} поела'.format(self.name))
            self.energy += 10
            self.house.total_food += 10
            self.house.food -= 10
    def shopping(self):
        if self.house.money >= 90:
            print('{} принесла покушать'.format(self.name))
            self.house.money -= 90
            self.house.food +=90
        elif 30 <= self.house.money < 90:
            print(self.name, "купила немного еды, пора бы уже поработать, дорогой")
            self.house.money -= 30
            self.house.food += 30
        elif self.house.money < 90:
            print(f'{self.name} : где деньги? У нас есть не на что')
    def buy_fur_coat(self):
        if self.house.money >= 350:
            print('{}: ура, смотри какая шуба!'.format(self.name))
            self.house.total_coats +=1
            self.house.money -= 350
            self.joy += 60
        else:
            self.eat()
            print('{}: кто, бы шубу купил... Ну хотябы поем'.format(self.name))
            self.eat()
    def clean_house(self):
        print('{}: нда, пора прибраться'.format(self.name))
        self.house.dirt -= 100
        self.energy -= 10
        if self.house.dirt < 0:
            self.house.dirt = 0


home = House()
serge = Husband('Сережа')
serge.go_to_the_house(home)
masha = Wife(name='Маша')
masha.go_to_the_house(home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    if serge.act() or masha.act():
        break
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')

# Подвести итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.

print('За год заработано', home.total_money)
print('Съедено',home.total_food, 'вкусняшек')
print('За год куплено',home.total_coats, 'шуб')



######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:
    # есть,
    #   спать,
    #   драть обои
    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

