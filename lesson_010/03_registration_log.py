# -*- coding: utf-8 -*-
from decorator import append


# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(BaseException):
    pass

class NotEmailError(BaseException):
    pass


class CheckLog:
    def __init__(self):
        self.file = 'registrations.txt'
        self.fields = list()
        self.list_of_fields = list()
        self.user = None
        self.list_of_good = list()
        self.list_of_bad = list()
        self.bad_file = None
        self.good_file = None
    def find_fields(self):
        with open(self.file) as file:
            for _line in file:
                self.fields = _line.split()
                self.list_of_fields.append(list(self.fields))
        # pprint(self.list_of_fields)
        return self.list_of_fields
    def check_fields(self):
        self.bad_file = open('registrations_bad.log', 'a', encoding='utf8')
        for self.user in self.list_of_fields:
             if self.user in self.list_of_bad:
                continue
             try:
                if len(self.user) == 3:
                      pass
                else:
                      raise ValueError('Lack of some data!')
             except ValueError as exc:
                self.bad_file = open('registrations_bad.log', 'a', encoding='utf8')
                self.bad_file.write(f'{self.user},{exc}- формы не заполнены \n')
                self.list_of_bad.append(self.user)
                # self.list_of_fields.remove(self.user)
        self.bad_file.close()
    def check_name(self):
        self.bad_file = open('registrations_bad.log', 'a', encoding='utf8')
        for self.user in self.list_of_fields:
            if self.user in self.list_of_bad:
                continue
            try:
                if self.user[0].isalpha():
                    pass
                else:
                    raise NotNameError('This is probably not a real name')
            except NotNameError as exc:
                self.bad_file.write( f'{self.user},{exc} - Имя некорректно! \n')
                self.list_of_bad.append(self.user)
                     # self.list_of_fields.remove(self.user)
        self.bad_file.close()
    def check_email(self):
        self.bad_file = open('registrations_bad.log', 'a', encoding='utf8')
        for self.user in self.list_of_fields:
            if self.user in self.list_of_bad:
                continue
            try:
                if '@' in self.user[1]:
                    pass
                elif '.' in self.user[1]:
                    pass
                else:
                    raise NotEmailError('No needed symbols in Email')
            except NotEmailError as exc:
                self.bad_file.write(f'{self.user},{exc} - Не верный Email! \n')
                self.list_of_bad.append(self.user)
                     # self.list_of_fields.remove(self.user)
        self.bad_file.close()
    def check_age(self):
        self.bad_file = open('registrations_bad.log', 'a', encoding='utf8')
        for self.user in self.list_of_fields:
            if self.user in self.list_of_bad:
                continue
            try:
                if 10 < int(self.user[2]) < 100:
                    pass
                else:
                    print(self.user[2])
                    raise ValueError('Non appropriate age!')
            except ValueError as exc:
                self.bad_file.write(f'{self.user},{exc} - Возраст не допустим \n')
                self.list_of_bad.append(self.user)
        self.bad_file.close()
                # self.list_of_fields.remove(self.user)
            # except IndexError as exc:
            #      self.bad_file = open('registrations_bad.log', 'a', encoding='utf8')
            #      self.bad_file.write(f'{self.user},{exc} No data in the destination \n')
            #      self.bad_file.close()
            #      self.list_of_fields.remove(self.user)
    def output_good(self):
        self.good_file = open('registrations_good.log', 'a', encoding='utf8')
        for self.user in self.list_of_fields:
            if self.user in self.list_of_bad:
                pass
            else:
                self.good_file.write(f'{' '.join(self.user)}\n')
        self.good_file.close()



reg = CheckLog()
# определили поля
reg.find_fields()
# проверяем все ли поля на месте
reg.check_fields()
# проверка   поле имени содержит НЕ только буквы
reg.check_name()
#собака и точка в имейл
reg.check_email()
#проверка возраста
reg.check_age()
# создаем файлы
reg.output_good()
