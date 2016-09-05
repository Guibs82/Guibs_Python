# 导入类
# 导入单个类
from car import Car
my_new_car = Car('audi', 'a6', 2016)
print(my_new_car.get_descriptive_name())

from car import ElectricCar
my_new_electric_car = ElectricCar('tesla', 'model s', 2016)
my_new_electric_car.battery.describe_battery()