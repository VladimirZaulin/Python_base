from unicodedata import numeric

from simple_draw import random_number

def generate_number():
    global a, b, c, d, number
    a = random_number(1, 9)
    b = random_number(0, 9)
    c = random_number(0,9)
    d = random_number(0, 9)
    number = [a, b, c, d]
    if a == b or a == c or a == d or b == c or b == d or c == d:
        generate_number()
    else:
        # print(number)
        return number

def check_number():
    n_bull = 0
    n_cow = 0
    user_answer=input()
    a1 = int(user_answer[0])
    b1 = int(user_answer[1])
    c1 = int(user_answer[2])
    d1 = int(user_answer[3])
    # print(a1,b1,c1,d1, a, b,c,d)
    if a1 == a:
        n_bull +=1
    if a1 == c or a1 == b or a1 == d:
        n_cow +=1
    if b == b1:
        n_bull += 1
    if b1 == a or b1 == c or b1 == d:
        n_cow +=1
    if c == c1:
        n_bull += 1
    if c1 == a or c1 == b or c1 == d:
        n_cow +=1
    if d == d1:
        n_bull += 1
    if d1 == a or d1 == b or d1 == c:
        n_cow +=1
    return n_bull, n_cow


# def how_many_bulls(n_bull, n_cow):
#     while n_bull < 4:
#         check_number()
#         print('Быки -', n_bull, 'Коровы -', n_cow)
# def get_number():
#     print('задаем число')


# generate_number()
# print(number)
# check_number()


