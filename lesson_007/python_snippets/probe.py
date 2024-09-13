

class Toyota:

    def __init__(self):
        self.color = "Бордовый металлик"
        self.price = "1 000 000 руб"
        self.max_velocity = "200 км/ч"
        self.current_velocity = "0 км/ч"
        self.engine_rpm = 0

    def start(self):
        print('Vjтор запущен')
        self.engine_rpm = 900

    def go(self):
        print("Поехали")
        self.engine_rpm = 2000
        self.current_velocity = "20 км/ч"

my_car = Toyota()
print('color',my_car.color)
print('price',my_car.price)
print('max_velocity',my_car.max_velocity)
print('rpm',my_car.engine_rpm)
print('current_velocity',my_car.current_velocity)


my_car.start()
