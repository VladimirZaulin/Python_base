def power(number, pow):
    print('Функцию вызвали с параметрами', number, pow)
    power_value = number ** pow
    print (power_value)

my_list = [3, 14, 15, 92, 6]
for element in my_list:
    result = power(number=element, pow=10)
    print(result)

