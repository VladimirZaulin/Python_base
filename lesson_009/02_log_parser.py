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

    def file_output(self,out_file_name=None):
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
            for key in self.counted:
                file.write(key)
                file.write(' ')
                file.write(str(self.counted.get(key)))
                file.write('\n')
            file.close()
        else:
            self.form_pretty_output()



# parser = LogParser(file_name)
# parser.find_noks()
# parser.counter()
# # parser.form_pretty_output()
# parser.file_output('OutLP.txt')

class ParseByHours(LogParser):
    def find_noks(self):
        with open(file_name,'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    self.dates.append(line[0:14]+'h]')
                else:
                    pass
        return self.dates

# par_hours = ParseByHours(file_name)
# par_hours.find_noks()
# par_hours.counter()
# par_hours.file_output('LPParseByHours.txt')

class ParseByMonths(LogParser):
    def find_noks(self):
        with open(file_name,'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    self.dates.append(line[0:8]+'m]')
                else:
                    pass
        return self.dates

# par_months = ParseByMonths(file_name)
# par_months.find_noks()
# par_months.counter()
# par_months.file_output('LPParseByMonths.txt')

class ParseByYear(LogParser):
    def find_noks(self):
        with open(file_name,'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    self.dates.append(line[0:5]+'y]')
                else:
                    pass
        return self.dates

par_years = ParseByYear(file_name)
par_years.find_noks()
par_years.counter()
par_years.file_output('LPParseByYear.txt')







# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
