# -*- coding: utf-8 -*-
from fileinput import filename
from pprint import pprint

# Подсчитать статистику по буквам в романе Война и Мир. +
# Входные параметры: файл для сканирования +
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)+
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class LettersRating:
    def __init__(self, filename):
        self.filename = filename
        self.stat = {}
        self.total = None
        self.stat_sorted = None

    def get_stats(self):
        with open(self.filename,'r', encoding='cp1251') as file: # открыли в режиме чтения
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1
                    else:
                        pass
        return self.stat
    def get_total_letters(self):
        x = self.stat.values()
        self.total = sum(x)
        return self.total

    def from_bigger_sorted(self):
        self.stat_sorted = sorted(self.stat.items(), key=lambda x: -x[1])
        return self.stat_sorted

    def from_less_sorted(self):
        self.stat_sorted = sorted(self.stat.items(), key=lambda x: x[1])
        return self.stat_sorted

    def from_a_sorted(self):
        self.stat_sorted = sorted(self.stat.items(), key=lambda x: x[0])
        return self.stat_sorted

    def from_z_sorted(self):
        self.stat_sorted = reversed(sorted(self.stat.items(), key=lambda x: x[0]))
        return self.stat_sorted

    def row_maker(self):
        for a,b in self.stat_sorted:
            rem = 10 - len(str(b)) - 3
            x = rem*' '
            print(f'|    {a}    |   {b}{x}|')


    def show_nice_tab(self):
        # self.from_bigger_sorted()
        print(f'+{9*'-'}+{10*'-'}+')
        print('|  буква  | частота  |')
        print(f'+{9*'-'}+{10*'-'}+')
        self.row_maker()
        # pprint(self.stat_sorted)
        print(f'+{9*'-'}+{10*'-'}+')
        print(f'|  итого  |  {self.total} |')
        print(f'+{9*'-'}+{10*'-'}+')

class LettersSortedFromLess(LettersRating):
    def show_nice_tab(self):
        self.from_less_sorted()
        print(f'+{9 * '-'}+{10 * '-'}+')
        print('|  буква  | частота  |')
        print(f'+{9 * '-'}+{10 * '-'}+')
        self.row_maker()
        # pprint(self.stat_sorted)
        print(f'+{9 * '-'}+{10 * '-'}+')
        print(f'|  итого  |  {self.total} |')
        print(f'+{9 * '-'}+{10 * '-'}+')

class LettersSortedFromA(LettersRating):
    def show_nice_tab(self):
        self.from_a_sorted()
        print(f'+{9 * '-'}+{10 * '-'}+')
        print('|  буква  | частота  |')
        print(f'+{9 * '-'}+{10 * '-'}+')
        self.row_maker()
        # pprint(self.stat_sorted)
        print(f'+{9 * '-'}+{10 * '-'}+')
        print(f'|  итого  |  {self.total} |')
        print(f'+{9 * '-'}+{10 * '-'}+')

class LettersSortedFromZ(LettersRating):
    def show_nice_tab(self):
        self.from_z_sorted()
        print(f'+{9 * '-'}+{10 * '-'}+')
        print('|  буква  | частота  |')
        print(f'+{9 * '-'}+{10 * '-'}+')
        self.row_maker()
        # pprint(self.stat_sorted)
        print(f'+{9 * '-'}+{10 * '-'}+')
        print(f'|  итого  |  {self.total} |')
        print(f'+{9 * '-'}+{10 * '-'}+')
book = LettersRating('python_snippets/voyna-i-mir.txt')
print('Сортировка букв')
print('от большего количества')
book.get_stats()
book.from_bigger_sorted()
book.get_total_letters()
book.show_nice_tab()

book2 = LettersSortedFromLess('python_snippets/voyna-i-mir.txt')
print('Сортировка букв')
print('от меньшего количества')
book2.get_stats()
book2.from_less_sorted()
book2.get_total_letters()
book2.show_nice_tab()

A_to_Z = LettersSortedFromA('python_snippets/voyna-i-mir.txt')
print('Сортировка букв')
print('в алфавитном порядке')
A_to_Z.get_stats()
A_to_Z.from_a_sorted()
A_to_Z.get_total_letters()
A_to_Z.show_nice_tab()


Z_to_A = LettersSortedFromZ('python_snippets/voyna-i-mir.txt')
print('Сортировка букв')
print('в порядке обратном алфавитному')
Z_to_A.get_stats()
Z_to_A.from_z_sorted()
Z_to_A.get_total_letters()
Z_to_A.show_nice_tab()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
