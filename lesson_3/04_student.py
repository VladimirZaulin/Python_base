# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
term_in_months = 10
#mother_load = x
price_increasing = 0.03
full_expenses = expenses

while term_in_months > 1:
    expenses = (expenses + expenses*price_increasing)
    full_expenses += expenses
    term_in_months -= 1
mother_load = full_expenses - (educational_grant * 10)


print('Студенту нужно попросить', round(mother_load,2), 'рублей')