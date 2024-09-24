# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self,n):
        self.n=n
        self.prime_numbers = get_prime_numbers(n)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self.prime_numbers):
            raise StopIteration
        _current_prime = self.prime_numbers[self.i]
        self.i += 1
        return  _current_prime





prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    list = get_prime_numbers(n)
    return list


# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
def is_happy(n):
    num_str = str(n)
    length = len(num_str)
    half_length = length // 2

    if len(str(n)) % 2 == 0:
        left_half_sum = sum(int(digit) for digit in num_str[:half_length])
        right_half_sum = sum(int(digit) for digit in num_str[half_length:])

    else:
        left_half_sum = sum(int(digit) for digit in num_str[:half_length])
        right_half_sum = sum(int(digit) for digit in num_str[half_length + 1:])

    return left_half_sum == right_half_sum


# ten_thou_simp_gen = prime_numbers_generator(n=10000)
#
#
#
# print(set(filter(is_happy, range(1,10000))))



# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
def is_palindrome(n):
    str_text = str(n)
    oppo_str = str_text[::-1]
    return oppo_str == str_text
print(list(filter(is_palindrome,prime_number_iterator)))
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
