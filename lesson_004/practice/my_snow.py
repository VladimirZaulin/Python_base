import simple_draw as sd

sd.resolution = (1200, 600)




y=500
x=100

y2=450
x2=145

while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=20, factor_a=0.5)
    y -= 50
    if y < 0:
       break
    x = x * 1.3

    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point, length=20, factor_a=0.5)
    y2 -= 50
    if y2 < 0:
        break
    x2 = x2 * 1.3

    sd.sleep(0.1)
    if sd.user_want_exit():
        break



sd.pause()