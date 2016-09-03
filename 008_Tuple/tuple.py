# 元组
# 元组相当于不可变的列表, 使用圆括号 ()
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

# 修改元组变量
# 虽然不能修改元组元素, 但可以给存储元组的变量赋值. 因此, 如果要修改某个元组, 可以重新定义整个元组
print(dimensions)
dimensions = (400, 100)
print(dimensions)
