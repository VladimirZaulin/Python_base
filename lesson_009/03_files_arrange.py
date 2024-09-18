# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk  --- описывает вложенные каталоги кортежами
#   os.path.dirname ---
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
count = 0
class FileSorter:
    def __init__(self):
        self.files = dict()
    def get_files(self):
        for a,b,c in os.walk('icons'):
            for file in c:
                full_path = os.path.join(a,file)
                secs = os.path.getmtime(full_path)
                gen_time = time.gmtime(secs)
                self.files[full_path] = gen_time[0:4]
        # print(self.files)

    def sort_and_relocate(self, new_place='icons_by_year/'):
        for keys in self.files:
            years_list = str(self.files.get(keys)[0])
            months_list = self.files.get(keys)[1]
            if months_list == 12 or months_list == 11 or months_list == 10:
                pass
            else:
                months_list = '0' + str(months_list)
            # new_place = 'icons_by_year/'
            way = os.path.join(new_place, years_list, str(months_list))
            if os.path.exists(way):
                pass
            else:
                os.makedirs(way)
            # # print(keys, files.get(keys))
            shutil.copy2(keys, way)


icon_sorter = FileSorter()
icon_sorter.get_files()
icon_sorter.sort_and_relocate()





















# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
