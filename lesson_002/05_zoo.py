#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import int_info

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert(1,'bear')


# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)

# уберите слона
#  и выведите список на консоль
del zoo[3]

lion_number = 0 + 1
lark_numer = 5 + 1
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
#
print('Лев сидит в',lion_number,'клетке, а жаворонок в клетке №',lark_numer )


