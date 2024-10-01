import warnings


#предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.

class BowlingError(ValueError):
    pass

def get_score(game_result):
    global score
    score = 0
    i = 0
    try:
        while i < len(game_result):
            if game_result[i] == 'X':  # Strike
                score += 20
                i += 1
            elif game_result[i + 1] == '/':  # Spare
                score += 15
                i += 2
            else:  # Regular frame
                try:
                    score += int(game_result[i]) + int(game_result[i + 1])
                except BowlingError as v:
                    warnings.warn(f"Значение должно быть числом, 'X' и или <числом> + / {v}", SyntaxWarning)
                    pass
                i += 2
    except Exception as ex:
        warnings.warn(f"Ошибка {ex}", SyntaxWarning)

    return score

#
# get_score(
#     game_result=input()
# )
#
# print(score)

