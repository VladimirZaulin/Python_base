# В нем определить функции добавления ингредиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

burger = []

def add_bums():
    burger.append('булочки')
    print('Добавим сочные булочки')
def add_meat():
    burger.append('котлета')
    print('Добавим натуральную мясную котлету')
def add_cucumber():
    burger.append('огурчик')
    print('Добавим свежий огурчик')
def add_tomato():
    burger.append('помидорка')
    print('Добавим спелую помидорку')
def add_sauce():
    burger.append('майонез')
    print('Добавим диетический майонез')
def add_cheese():
    burger.append('сыр')
    print('Добавим сыр!')
