# -*- coding: utf-8 -*-
from pprint import pprint

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as folks_1
from room_2 import folks as folks_2

print("В комнате room_1 живут:", folks_1[0],'и', folks_1[1],
    "В комнате room_2 живут:", folks_2[0])




