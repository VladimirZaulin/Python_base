# -*- coding: utf-8 -*-
import multiprocessing
import os
from multiprocessing import Process, Queue
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


dir = list(os.walk('/Users/dream9hacker/PycharmProjects/probe/Python_base/lesson_012/trades'))

class VolatReview(Process):
    def __init__(self, dir, result_queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dir = dir
        self.result_queue = result_queue  # Очередь для передачи данных

    def run(self):
        for dirpath, dirnames, filenames in self.dir:
            for name in filenames:
                prices = list()
                full_file_path = os.path.join(dirpath, name)

                try:
                    with open(file=full_file_path, mode='r', encoding='utf8') as file:
                        for line in file:
                            if ':' in line:
                                cut_line = line.split(',')
                                price = cut_line[2]
                                prices.append(float(price))
                except Exception as e:
                    print(f"Error processing file {full_file_path}: {e}")
                    continue

                if prices:
                    max_price = max(prices)
                    min_price = min(prices)
                    average_price = (max_price + min_price) / 2
                    volat = ((max_price - min_price) / average_price) * 100
                    if volat != 0:
                        self.result_queue.put((name[7:11], volat))  # Передача данных через очередь
                    else:
                        self.result_queue.put((name[7:11], 0))  # Для бумаг с нулевой волатильностью


if __name__ == '__main__':
    @time_track
    def main():
        result_queue = Queue()  # Очередь для получения результатов от всех процессов
        processes = []

        # Создание процессов
        for _ in range(3):  # Предположим, создаем 3 процесса для примера
            process = VolatReview(dir=dir, result_queue=result_queue)
            processes.append(process)
            process.start()

        # Ожидание завершения всех процессов
        for process in processes:
            process.join()

        # Сбор всех результатов
        vol_box = {}
        null_box = {}

        while not result_queue.empty():
            ticker, volat = result_queue.get()
            if volat != 0:
                vol_box[ticker] = volat
            else:
                null_box[ticker] = volat

        # Сортировка и вывод результатов
        sorted_volatilities = sorted(vol_box.items(), key=lambda x: x[1], reverse=True)

        print('Максимальная волатильность:')
        for ticker, vol in sorted_volatilities[:3]:
            print(f'    {ticker} - {vol:.4f} %')

        print('Минимальная волатильность:')
        for ticker, vol in sorted_volatilities[-3:]:
            print(f'    {ticker} - {vol:.4f} %')

        print('Нулевая волатильность:')
        if null_box:
            print(', '.join(sorted(null_box)))
        else:
            print('Нулевых волатильностей нет.')

    main()