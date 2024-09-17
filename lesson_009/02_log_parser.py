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
dates = []
#find_noks
with open(file_name,'r', encoding='cp1251') as file:
    for line in file:
        if 'NOK' in line:
            dates.append(str(line[0:17]+']'))
        else:
            pass
        # return dates
#counter
counted = Counter(dates)
# pprint(counted)

#TODO group_by_hours

#TODO group_by_months

#TODO group_by_years

# TODO pretty_output
print(Counter(dates))

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
