from pprint import pprint
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

first = my_favorite_movies[0:10]
second = my_favorite_movies[12:25]
third = my_favorite_movies[27:33]
forth = my_favorite_movies[35:40]
fifth = my_favorite_movies[42:57]

print(first, fifth, second, forth)