# 继承

class Car():
    """模拟汽车"""

    def __init__(self, name, model, year):
        """初始化描述汽车属性"""
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 给属性设置默认值 [设置里程数初始值为0]

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + " " + self.name + " " + self.model
        return long_name

    def read_odmeter(self):
        """打印公里数"""
        print("这辆车已经行驶了: " + str(self.odometer_reading) + "公里了")

    def update_odometer(self, mileage):
        """将里程表设置为指定的值"""
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("请不要造假里程数谢谢~")

    def increment_odmeter(self, mileage):
        """将里程数增加指定的量"""
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        """添加汽油"""
        print("添加汽油")

class Battery():
    """模拟电池"""

    def __init__(self, battery_size=70): # battery_size 默认值为70
        """初始化电池属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印描述电瓶容量的信息"""
        print("电池容量为: " + str(self.battery_size) + "-kWh")

    def get_range(self):
        """打印可行驶公里数"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 290
        message = "这个电动车可以跑" + str(range) + "公里"
        print(message)

class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, name, model, year):
        """初始化父类的属性"""
        super().__init__(name, model, year)
        # super(ElectricCar, self).__init__(name, model, year) # 也可用

        """初始化弗雷的属性, 再初始化电动车特有的属性"""
        # 设置实例用作类的属性
        self.battery = Battery()

    def describe_battery_by_car(self):
        """打印一条描述电瓶容量的消息"""
        self.battery.describe_battery()

    # 重写该父类的方法
    def fill_gas_tank(self):
        """电动车不需要加油"""
        print("电动车...不用加油...")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery_by_car()
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()