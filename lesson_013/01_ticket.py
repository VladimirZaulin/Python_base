# -*- coding: utf-8 -*
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

def make_ticket(fio, from_, to, date, font_path=None):
    if font_path is None:
        font_path = "ofont.ru_Anticva.ttf"
    else:
        font_path = font_path
    im = Image.open("images/ticket_template.png")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, size=16)

    y = im.size[1] - 225 - (10 + font.size) * 2
    fio_space = f"{fio}"
    draw.text((45, y), fio_space, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 192 - font.size
    from_space = f"{from_}"
    draw.text((45, y), from_space, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 90 - (10 + font.size) * 2
    fio_space = f"{to}"
    draw.text((45, y), fio_space, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 90 - (10 + font.size) * 2
    from_space = f"{date}"
    draw.text((265, y), from_space, font=font, fill=ImageColor.colormap['black'])

    # im.show()
    out_path = 'probe.png'
    im.save(out_path)
    print(f'Ticket saved as {out_path}')


if __name__ == '__main__':
    maker = make_ticket(fio="Василий Толстопузченко", from_ = "Марс", to = "Сызрань", date= "31.12.2924")

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
