# -*- coding: utf-8 -*-
from pprint import pprint
from collections import Counter
# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

file_name = 'events.txt'

class LogParser:
    def __init__(self, file_name):
        self.dates = []
        self.counted = None
        self.filename = file_name


    def find_noks(self):
        with open(file_name,'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    self.dates.append(line[0:17]+']')
                else:
                    pass
        return self.dates
    def counter(self):
        self.counted = Counter(self.dates)
    def form_pretty_output(self):
        for items in self.counted:
            print(items, self.counted.get(items))


parser = LogParser(file_name)
parser.find_noks()
parser.counter()
parser.form_pretty_output()






#TODO group_by_hours
#TODO group_by_months
# group_by_hours = sorted(counted, key=lambda x: x[1])
# counted = dict(counted)
#TODO group_by_years






# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
