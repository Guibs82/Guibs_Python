# 函数
# 函数是带有名字的代码块, 用于完成具体的工作

# 定义函数 greet_user
def greet_user():
    # 函数体
    print("Hello")
# 调用函数 greet_user
greet_user()

# 向函数传递信息
def greet_user(username): # username 是一个形参
    print("Hello " + username)
greet_user(username='Guibs') # Guibs 是一个实参
greet_user('Guibs')

# 带关键字传递实参
# 可以不用考虑实参传递的顺序
def greet_user(username1, username2):
    print("Hello " + username1 + " and " + username2)
greet_user(username2='Guibs', username1='Guibs82')

# 参数默认值
# 若不传递参数则调用默认值
# 含有默认值的参数必须放在后面
def greet_user_with_default_name(username1, username2='Guibs82'):
    print("Hello " + username1 + " and " + username2)
# 若未传递足够参数, 则按位置进行参数传递
greet_user_with_default_name('G')

# 返回值
def get_formatted_name(first_name, last_name, middle_name = ""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
my_name = get_formatted_name("guibs", "g")
print("My name is " + my_name)

my_name = get_formatted_name("guibs", 'g', '82')
print("My name is " + my_name)

# 返回字典
def build_person(first_name, last_name, age=''):
    '''返回一个字典, 包含有关一个人的信息'''
    person = {
        'first': first_name.title(),
        'last': last_name.title(),
    }
    if age:
        person['age'] = age
    return person
print(build_person('g', 'ghost', 22))

# 传递列表
names = ['guibs', 'ghostg', 'rio_G']
def greet_users(names):
    for name in names:
        print("Hello " + name.title())
greet_users(names=names)

# 在函数中修改列表
# 将列表传递给函数后, 函数可以对其进行永久性修改
unprinted_designs = ['iphone case', 'ipad case', 'mac case']
printed_designs = []
def print_designs(unprinted_designs, printed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("准备打印: " + current_design)
        printed_designs.append(current_design)
        print("打印完毕: " + current_design)
    print("全部作品打印完毕")
print_designs(unprinted_designs=unprinted_designs, printed_designs=printed_designs)

def show_printed_designs(printed_designs):
    print("打印完毕的作品: ")
    for printed_design in printed_designs:
        print(printed_design)
show_printed_designs(printed_designs)

# 禁止函数修改列表
# 采用切片的形式, 复制传入函数的列表
unprinted_designs = ['iphone case', 'ipad case', 'mac case', 'apple watch case']
printed_designs = []
print_designs(unprinted_designs[:], printed_designs)
print(unprinted_designs) # 此时, 原列表未被修改

# 传递任意数量的参数
# [*param_name]
# 此时, Python 将参数封装至一个元组
def print_username(*username):
    print(username)
print_username("Guibs")
print_username("Guibs", 'GhostG')

# 使用任意数量的关键字形参
# [**param_names]
def set_hobbies(name, **hobbies):
    my_hobbies = {}
    my_hobbies['name'] = name
    for key, value in hobbies.items():
        my_hobbies[key] = value
    return my_hobbies

print(set_hobbies(name="Guibs", hobby_1='Swift', hobby_2='Python'))


# 注意: 在 import 时, 若不使用系统中的解释器, 而是用自己创建的, 则报错
# 导入存储在模块中的函数
# 导入整个模块
import pizza
pizza.make_pizza(12, 'mushrooms', 'extra cheese')

# 使用 as 给模块指定别名
import pizza as p
p.make_pizza(12, 'mushrooms', 'lots of cheese')

# 导入特定的函数
# from module_name import function_name_0, function_name_1, ...
# 这种语法可以无需使用 .
from pizza import make_pizza
make_pizza(12, 'mushrooms', 'more cheese')

# 使用 as 给函数指定别名
from pizza import make_pizza as buy_pizza
buy_pizza(12, 'mushrooms', 'a lot of cheese')

# 导入模块中的所有函数
# [*]
from pizza import *
get_price()