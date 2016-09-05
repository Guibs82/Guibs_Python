# 从一个模块中导入多个类
from car import Car, ElectricCar

my_new_car = Car('audi', 'a6', 2016)
print(my_new_car.get_descriptive_name())


my_new_electric_car = ElectricCar('tesla', 'model s', 2016)
my_new_electric_car.battery.describe_battery()