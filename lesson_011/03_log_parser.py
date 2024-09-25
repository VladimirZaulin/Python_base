# -*- coding: utf-8 -*-
from collections import Counter

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

file_name = 'events.txt'


def find_noks(file_name):
    dates = []
    with open(file_name,'r', encoding='cp1251') as file:
        for line in file:
            if 'NOK' in line:
                dates.append(line[0:17]+']')
            else:
                pass
    counted = Counter(dates)
    for items in counted:
        yield items, counted.get(items)





grouped_events = find_noks(file_name)
print(type(grouped_events))
for group_time, event_count in grouped_events:
    print(f'{group_time} {event_count}')

