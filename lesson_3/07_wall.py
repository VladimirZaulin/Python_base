# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw
from simple_draw import get_point, rectangle, COLOR_DARK_ORANGE, random_color, COLOR_ORANGE, COLOR_YELLOW

simple_draw.resolution = (1200,600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
brick_left_bottom = 0
brick_right_top = 0
shift_rows_list = [ 50 , 150 , 250 , 350 , 450 , 550 ]

for x_axis in range(0,1200,100):
    for y_axis in range(0,600,50):
        brick_left_bottom = get_point( x_axis, y_axis )
        brick_right_top = get_point( x_axis + 100, y_axis + 50 )
        if y_axis in shift_rows_list:
            brick_left_bottom = get_point( x_axis + 50, y_axis )
            brick_right_top = get_point( x_axis + 150, y_axis + 50 )
        brick = rectangle(brick_left_bottom, brick_right_top, COLOR_DARK_ORANGE, 3)



simple_draw.pause()
