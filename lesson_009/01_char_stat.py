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

    def row_maker(self):
        for a,b in self.stat_sorted:
            rem = 10 - len(str(b)) - 3
            x = rem*' '
            print(f'|    {a}    |   {b}{x}|')


    def show_nice_tab(self):

        print(f'+{9*'-'}+{10*'-'}+')
        print('|  буква  | частота  |')
        print(f'+{9*'-'}+{10*'-'}+')
        self.from_bigger_sorted()
        self.row_maker()
        # pprint(self.stat_sorted)
        print(f'+{9*'-'}+{10*'-'}+')
        print(f'|  итого  |  {self.total} |')
        print(f'+{9*'-'}+{10*'-'}+')


book = LettersRating('python_snippets/voyna-i-mir.txt')
book.get_stats()
book.get_total_letters()
book.show_nice_tab()



# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
