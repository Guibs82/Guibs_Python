# if
# if 通过缩进来控制代码块是否属于 if
# if conditional_test:
#     do something

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 条件测试
# 每条 if 语句的核心都是一个值为 True 或 False 的表达式, 这种表达式被称之为条件测试.

# 检查是否相等
# [==] 在两边的值相等时返回 True
print("bmw" == "bmw")

# 检查是否不相等
# [!=] 在两边的值不相等时返回 True
print("bmw" != "bmw")

# 比较数字
print(1 > 2)
print(1 == 2)
print(1 < 2)
print(1 != 2)
print(1 >= 2)
print(1 <= 2)

# 检查多个条件
# 使用 and 检查多个条件
# 必须几个条件都为 True 才返回 True
if 1 > 0 and 2 > 1:
    print("说的没错")
else:
    print("有问题啊")
# 使用 or 检查多个条件
# 有一个条件为 True 就返回 True
if 1 > 0 or 2 < 1:
    print("可以的")
else:
    print('没一个对的...')

# 检查特定值是否包含在列表里
# [in]
languages = ['Swift', 'Python', 'Objective-C']
print('Java' in languages)
# 检查特定值是否不包含在列表里
# [not in]
prices = [1, 3, 10, 6]
print(2 not in prices)

# 布尔表达式
# 布尔表达式的结果要么为 True 要么为 False
isExist = True
game_active = False

# if 语句
if False:
    print("这是 if 体的语句, 所以不会显示")
print("这不是 if 体的语句, 所以会显示")

# if-else 语句
age = 20
if age > 18:
    print("你已经成年了")
else:
    print("你还未成年")

# if-elif-else
# elif 可以有多个
money = 20
if money > 18:
    print("你可以买鸡排咖喱饭")
elif money > 15:
    print("你可以买猪排咖喱饭")
elif money > 12:
    print("你可以买咖喱饭")
# else 可以省略
else:
    print("你买不了咖喱饭")

# 用多个 if 语句执行一系列满足条件的判断
num = 3
if num > 0:
    print("你的数字大于0")
if num > 1:
    print("你的数字大于1")
if num > 2:
    print("你的数字大于2")

# if 处理列表
# 检查特殊元素
languages = ['Swift', 'Python', 'Objective-C', 'Java']
for language in languages:
    if language == 'Swift' or language == 'Python':
        print("非常乐意学习和使用" + language)
# 确定列表不是空的
order_books = []
if order_books:
    for book in order_books:
        print(book)
else:
    print("订购清单为空, 你还没确定要订购的图书")
# 使用多个列表
wanna_books = ['DN', 'Swift', 'Python']
sale_books = ['Swift', 'Python', 'Java', 'PHP']
for sale_book in sale_books:
    if sale_book in wanna_books:
        print(sale_book + " 恰好是我想买的")