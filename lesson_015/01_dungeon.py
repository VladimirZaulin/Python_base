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

# -*- coding: utf-8 -*-



class YouWin(Exception):
    pass


class YouAreDead(Exception):
    pass


class Player:

    def __init__(self, name):
        self.name = name
        self.exp = 0
        self.tm = Decimal('1234567890.0987654321')
        self.location = None

    def go(self, location):
        self.location = location
        dice = randint(1, 4)
        actions = ['осторожно входит', 'устремляется в', 'вышибает с ноги дверь в', 'взламывает замок в']
        print(f'{self.name} {actions[dice - 1]} {location}')
        tm_waste = re.search(r'tm(\d+)', location)
        if tm_waste:
            self.tm -= Decimal(tm_waste.group(1))

    def state(self):
        print(f'Вы находитесь в {self.location}')
        print(f'У вас {self.exp} опыта и осталось {self.tm} секунд')
        seconds = int(Decimal('1234567890.0987654321') - self.tm)
        formatted_time = strftime('%H:%M:%S', gmtime(seconds))
        print(f'Прошло уже {formatted_time}')

    def attack(self, monster):
        print(f'{self.name} атакует монстра {monster}')
        tm_waste = re.search(r'tm(\d+)', monster)
        add_exp = re.search(r'exp(\d+)', monster)
        if tm_waste and add_exp:
            self.tm -= Decimal(tm_waste.group(1))
            self.exp += int(add_exp.group(1))
        else:
            print("Ошибка данных о монстре!")

    def die(self):
        if self.tm <= 0:
            raise YouAreDead



def explore(current_location, location_content, previous_locations=None):
    player.die()
    if previous_locations is None:
        previous_locations = []

    monsters = [item for item in location_content if isinstance(item, str) and 'Mob' or 'Boss' in item]
    boss = [item for item in location_content if isinstance(item, str) and 'Boss' in item]
    locations = [item for item in location_content if isinstance(item, dict)]

    print('Внутри вы видите:')
    for monster in monsters:
        if 'Mob' in monster:
            print(f'-- Монстра {monster}')
        elif 'Boss' in monster:
            print(f'-- Босса {monster}')
    for loc in locations:
        for loc_name in loc:
            print(f'-- Вход в локацию: {loc_name}')

    print('Выберите действие:')
    print('1. Атаковать монстра')
    print('2. Перейти в другую локацию')
    print('3. Вернуться назад')
    print('4. Выход')

    choice = input()

    if choice == '1':
        if monsters:
            for idx, mons in enumerate(monsters, start=1):
                print(f'{idx}. {mons}')
            monster_choice = int(input('Выберите монстра: ')) - 1
            if 0 <= monster_choice < len(monsters):
                player.attack(monsters[monster_choice])
                if str(monsters[monster_choice]) in location_content:
                    print('Yff - хрип')
                    location_content.pop(location_content.index(monsters[monster_choice]))



                # Убираем монстра из текущей локации
                player.state()
            else:
                print("Некорректный выбор.")
        else:
            print("Здесь нет монстров.")
        explore(current_location, location_content, previous_locations)

    elif choice == '2':
        if locations:
            for idx, loc in enumerate(locations, start=1):
                for loc_name in loc:
                    print(f'{idx}. {loc_name}')
            loc_choice = int(input('Выберите локацию: ')) - 1
            if 0 <= loc_choice < len(locations):
                loc_name = list(locations[loc_choice].keys())[0]
                player.go(loc_name)
                previous_locations.append((current_location, location_content))  # Добавляем текущую локацию в историю
                explore(loc_name, locations[loc_choice][loc_name], previous_locations)
            else:
                print("Некорректный выбор.")
        else:
            print("Здесь нет доступных путей.")
        explore(current_location, location_content, previous_locations)

    elif choice == '3':
        if previous_locations:
            prev_location, prev_content = previous_locations.pop()
            player.go("возвращается назад")
            explore(prev_location, prev_content, previous_locations)
        else:
            print("Некуда возвращаться.")
        explore(current_location, location_content, previous_locations)

    elif choice == '4':
        print("Вы вышли из игры.")

        quit()

    else:
        print("Некорректный ввод.")
        explore(current_location, location_content, previous_locations)


file_path = "/Users/dream9hacker/PycharmProjects/probe/Python_base/lesson_015/rpg.json"
if os.path.exists(file_path):
    with open(file_path, 'r') as incoming_map:
        map_data = json.load(incoming_map)
else:
    print(f"Ошибка: файл {file_path} не найден.")

player = Player('Вася')
initial_location = "Location_0_tm0"
explore(initial_location, map_data[initial_location].copy())



# Учитывая время и опыт, не забывайте о точности вычислений!

