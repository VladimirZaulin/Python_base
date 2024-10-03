# -*- coding: utf-8 -*-
import json
import os
import re
from collections import defaultdict
from datetime import time, datetime
from decimal import ROUND_HALF_EVEN, Decimal
from dis import pretty_flags
from os import remove
from pprint import pprint
from random import randint
from time import gmtime, strftime
from unicodedata import decimal

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход

remaining_time = '1234567890.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']

class YouWin(Exception):
    pass

class YouAreDead(Exception):
    pass

class Player:

    def __init__(self, name):
        self.name = name
        self.exp = 0
        self.tm = '1234567890.0987654321'
        CONST_TM = Decimal('1234567890.0987654321')
        self.passed_time = (CONST_TM - Decimal(self.tm))
        self.location = None

    def go(self, location):
        self.location = location
        dice = randint(1,4)
        if dice == 1:
            print(self.name, 'осторожно входит в', location)
        if dice == 2:
            print(self.name, 'устремляется в', location)
        if dice == 3:
            print(self.name, 'вышибает с ноги дверь в', location)
        if dice == 4:
            print(self.name, 'взламывает замок в', location)
        tm_waste = re.search(r'tm(\d+)', location)
        self.tm = Decimal(self.tm) - Decimal(tm_waste.group(1))

    def state(self,):
        print(f'Вы находитесь в {self.location}')
        print(f'У вас {self.exp} опыта и осталось {self.tm} секунд')
        self.passed_time = self.passed_time.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
        # Преобразуем Decimal в количество секунд (целое число)
        seconds = int(self.passed_time)
        # Преобразуем количество секунд в структуру времени
        time_struct = gmtime(seconds)
        # Форматируем время в строку HH:MM:SS
        formatted_time = strftime('%H:%M:%S', time_struct)
        # Выводим отформатированное время
        print(f'Прошло уже {formatted_time}')

    def attack(self, monster):
        print(self.name, 'атакует монстра', monster)
        tm_waste = re.search(r'tm(\d+)', monster)
        self.tm = str(Decimal(self.tm) - Decimal(tm_waste.group(1)))
        add_exp = re.search(r'exp(\d+)_', monster)
        self.exp = int(add_exp.group(1))
    def die(self):
        while True:
            if self.tm == 0 or self.tm is None:
                raise YouAreDead


file_path = "/Users/dream9hacker/PycharmProjects/probe/Python_base/lesson_015/rpg.json"
if os.path.exists(file_path):
    with open(file_path, 'r') as incoming_map:
        map = json.load(incoming_map)
else:
    print(f"Ошибка: файл {file_path} не найден.")


map_dict = dict(map)

def explore(way, message=None, _ways=None, previous_location=None, beaten_mons=None):
    global boss
    if _ways is None:
        _ways = []
    if previous_location is None:
        previous_location = []
    if beaten_mons is None:
        beaten_mons = []
    if message is not None:
        print(message)
    monsters = []
    _doors = 0
    print('Внутри вы видите:')
    for key in way:
        if 'Mob' in key:
            print(f'-- Монстра {key}')
            monsters.append(key)
        elif 'Loc' in key:
            _doors += 1
            _ways.append(key)
            print(f'-- Вход в локацию:{key}')
        elif 'Boss' in key:
            print(f'-- Босса {key}')
            boss = key
    if _doors == 0 and len(monsters) == 1:
        print('(можно прокрасться мимо)')

    print('Выберите действие:')
    print('1.Атаковать монстра')
    print('2.Перейти в другую локацию')
    print('3.Выход')
    _input = input()
    if _input == '1':
        print(_ways)
        if len(monsters) == 0:
            print('тут нет монстров')
            _input = input()
        elif len(monsters) == 1:
            # monster = monsters[0]
            player.attack(monsters[0])
            beaten_mons.extend(monsters)
            player.state()
            if 'Mob' in way[0]:
                way[0] = 'corpse'
            monsters.clear()
            explore(way[1],message="МОНСТР УБИТ, ТЕПЕРЬ ВИДНО ДВЕРЬ", _ways=_ways, previous_location=previous_location)


        elif len(monsters) > 1:
            print('какого монстра побьем?')
            for index, mons in enumerate(monsters, start=1):
                print(index, mons)
            try:
                input_ = int(input())
                if 0 < input_ <= len(monsters):
                    player.attack(monsters[input_ - 1])
                    beaten_mons.extend(monsters[input_ - 1])
                else:
                    print("Некорректный выбор монстра.")
            except ValueError:
                print("Введите число.")
    if _input == '2':

        if len(_ways) == 1:
            previous_location.extend(way)
            print(way[_ways[0]])
            explore(way[_ways[0]],message="УДАЛОСЬ ЗАЙТИ В ДВЕРЬ", _ways=_ways, previous_location=previous_location)

        elif len(_ways) == 0:
            print('... Путь дальше завален, надо возвращаться...')
            player.go(way)
            explore(way,message="ОСТАЕМСЯ ТАМ ГДЕ И БЫЛИ", _ways=_ways, previous_location=previous_location)

        elif len(_ways) > 1:
            print('Какую дверь откроем?')
            for index, door in enumerate(_ways, start=1):
                print(index, door)
            input_2 = input()
            previous_location.extend(way)
            player.go(way[_ways[int(input_2) - 1]])
            explore(way[_ways[int(input_2) - 1]],message="ВЫБРАЛИ ДВЕРЬ", _ways=_ways, previous_location=previous_location)
    elif _input == '3':
        _path = previous_location[-1]
        print(_path)
        previous_location.remove(_path)
        player.go(_path)
        explore(_path,message="ПЕРЕХОДИМ НА ПРЕЖНЮЮ ПОЗИЦИЮ", _ways=_ways, previous_location=previous_location)


player = Player('Вася')
# print("!!!!"
#       ,map["Location_0_tm0"][0])

explore(map.copy())


# Учитывая время и опыт, не забывайте о точности вычислений!

