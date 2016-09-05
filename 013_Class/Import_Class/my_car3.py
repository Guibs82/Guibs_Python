# 导入整个模块
import car

my_new_car = car.Car('audi', 'a6', 2016)
print(my_new_car.get_descriptive_name())

my_new_electric_car = car.ElectricCar('tesla', 'model s', 2016)
my_new_electric_car.battery.describe_battery()