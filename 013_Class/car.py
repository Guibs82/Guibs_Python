# 使用类和实例
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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# 修改属性的值
my_new_car.read_odmeter()
# 1.直接修改属性的值
my_new_car.odometer_reading = 10
my_new_car.read_odmeter()
# 2.通过方法修改属性的值
my_new_car.update_odometer(10)
my_new_car.read_odmeter()
# 3.通过方法对属性进行递增
my_new_car.increment_odmeter(10)
my_new_car.read_odmeter()
