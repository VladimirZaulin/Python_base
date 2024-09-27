# -*- coding: utf-8 -*-
import os
import threading

from lesson_012.python_snippets.utils import time_track

# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
dir=os.walk('/Users/dream9hacker/PycharmProjects/probe/Python_base/lesson_012/trades')

class VolatReview(threading.Thread):
    def __init__(self, dir,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.dir = dir
        self.vol_box = dict()
        self.null_box = dict()

    def run(self):
        for dirpath, dirnames, filenames in self.dir:
            # print('len -',len(filenames))
            for name in filenames:
                prices = list()
                full_file_path = os.path.join(dirpath, name)
                # print(full_file_path)
                with (open(file=full_file_path, mode='r', encoding='utf8') as file):
                    for line in file:
                        if ':' in line:
                            cut_line = line.split(',')
                            price = cut_line[2]

                            prices.append(float(price))
                            # print()
                            # print(price)

                max_price = max(prices)
                min_price = min(prices)
                average_price = (max_price + min_price) / 2
                volat = ((max_price - min_price) / average_price) * 100
                if volat != 0:
                     self.vol_box[name[7:11]] = volat
                else:
                    self.null_box[name[7:11]] = volat
        self.output()
    def output(self):
        sorted_volatilities = sorted(self.vol_box.items(), key=lambda x: x[1], reverse=True)

        print('Максимальная волатильность:')
        for ticker, vol in sorted_volatilities[:3]:
            print(f'    {ticker} - {vol:.4f} %')

        print('Минимальная волатильность:')
        for ticker, vol in sorted_volatilities[-3:]:
            print(f'    {ticker} - {vol:.4f} %')

        print('Нулевая волатильность:')
        if self.null_box:
            print(', '.join(sorted(self.null_box)))
        else:
            print('Нулевых волатильностей нет.')

@time_track
def main():
    thread = VolatReview(dir)
    thread.start()
    guys = "Pinoccio", "JackSparrow", "Cheba"
    for _ in guys:
        thread.join()


main()