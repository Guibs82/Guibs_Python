# 类
# Python 中, 首字母大写的名称指的是类
class Dog():
    """模拟小狗"""

    def __init__(self, name, age): # self 必不可少, 且必须位于其他参数前面. 每个与类相关联的方法调用都自动传递实参 self, 他是一个
                                   # 指向实例本身的引用, 让实例能够访问类中的属性和方法
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " 蹲下了")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " 打了个滚")

# 根据类创造实例
my_dog = Dog('tik', 2)

# 使用点语法 . 访问类的属性
print("我的小狗名字叫: " + my_dog.name.title())
print("我的小狗今年" + str(my_dog.age) + "岁了")

# 调用类方法
my_dog.sit();
my_dog.roll_over()