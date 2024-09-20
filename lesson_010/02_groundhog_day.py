# -*- coding: utf-8 -*-
from random import randint
# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

class IamGodError(BaseException):
    pass
class DrunkError(BaseException):
    pass
class CarCrashError(BaseException):
    pass
class GluttonyError(BaseException):
    pass
class DepressionError(BaseException):
    pass
class SuicideError(BaseException):
    pass


ENLIGHTENMENT_CARMA_LEVEL = 777

def one_day():
    global carma
    carma += randint(1,7)
    dice = randint(1,13)
    try:
        if dice == 1:
            raise IamGodError('Я бог')
    except IamGodError as exc:
            print(f'{exc} Да начнется новый день!')
    try:
        if dice == 2:
            raise DrunkError('Напился блн')
    except DrunkError as exc:
            print(f'{exc} Да начнется новый день!')
    try:
        if dice == 3:
            raise CarCrashError('Разбил машину:(')
    except CarCrashError as exc:
        print(f'{exc} Да начнется новый день!')
    try:
        if dice == 4:
            raise GluttonyError('Слишком много еды!')
    except GluttonyError as exc:
        print(f'{exc} Да начнется новый день!')
    try:
        if dice == 5:
            raise DepressionError('Я в депрессии')
    except DepressionError as exc:
        print(f'{exc} Да начнется новый день!')
    try:
        if dice == 6:
            raise SuicideError('Помер')
    except SuicideError as exc:
        print(f'{exc} Да начнется новый день!')


# https://goo.gl/JnsDqu
carma = 0
day = 0
while  carma <= ENLIGHTENMENT_CARMA_LEVEL:
    day+=1
    print(f'День №{day}')
    one_day()
    print(f'Количество кармы: {carma}')
