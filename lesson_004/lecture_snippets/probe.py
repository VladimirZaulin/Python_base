ff = open('lesson_004/lecture_snippets/05_builtin.py', 'r', encoding='UTF8')
for line in ff.readlines():
    print(line, end='')
ff.close()