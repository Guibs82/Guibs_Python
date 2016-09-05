import car2

my_new_car = car2.Car('audi', 'a6', 2016)
print(my_new_car.get_descriptive_name())


my_new_electric_car = car2.ElectricCar('tesla', 'model s', 2016)
my_new_electric_car.battery.describe_battery()