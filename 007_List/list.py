# 列表

# 列表由一系列按特定顺序排列的元素组成, 其中元素和元素之间可以没有任何关系
# 在 Python 中, 用方括号 [] 来表示列表, 并用逗号 , 分隔其中的元素
languages = ['swift', "python", "objective-C"]
print(languages)

# 访问列表元素
# 列表是有序集合, 因此要访问列表的任何元素, 只需将该元素的位置或索引告诉 Python 即可
# 在 Python 中, 第一个元素的索引是0
print(languages[0])
print(languages[1])
print(languages[2])
# 当列表不为空时:
# 将索引设置为-1, 可以返回 Python 列表的最后一个元素
print(languages[-1])
# 将索引设置为-2, 可以返回 Python 列表的倒数第二个元素
print(languages[-2])
# 将索引设置为-3, 可以返回 Python 列表的倒数第三个元素
print(languages[-3])

# 使用列表中的元素
wanna_use = "I'd like to use " + languages[1].title() + "."
print(wanna_use)

# 添加、修改、删除元素
# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 添加列表元素
# 在列表末尾添加
# [.append()]
motorcycles.append('yamaha')
print(motorcycles)
# 在列表中插入元素
# [.insert()]
motorcycles.insert(1, "hl")
print(motorcycles)

# 删除列表元素
# [del]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
# 删除指定元素并返回被删除的值
# [.pop()]
poped_motor = motorcycles.pop(0)
print(poped_motor)
# 根据值删除元素
# [.remove()]
# 只会删除第一个出现的与该值匹配的元素
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

# 组织列表
# 对列表进行永久排序
# [.sort()]
cars = ['bmw', 'audi', 'toyota', 'mini']
print(cars)
cars.sort()
print(cars)
# 倒叙
cars.sort(reverse=True)
print(cars)

# 使用sorted() 列表进行临时排序
cars2 = ['bmw', 'audi', 'toyota', 'mini']
print(cars2)
print(sorted(cars2))
print(cars2)
# 倒叙
print(sorted(cars2, reverse=True))

# 永久反转列表顺序
# [.reverse()]
foods = ['apple', 'pear', 'banana']
print(foods)
foods.reverse()
print(foods)

# 确定列表的长度
# [len()]
print(len(foods))

# 使用列表时, 避免索引错误

# 操作列表
# 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick\n")
print("Thank you everyone")

# 创建数值列表
# 生成一系列数字
# [range()]
for value in range(1, 5):
    print(value) # 1, 2, 3, 4
# 指定步长
for value in range(1, 5, 2):
    print(value) # 1 3
# 使用函数 list() 将 range() 的结果转换为列表
numbers = list(range(1, 6))
print(numbers)

# 数字列表处理
numbers = [1, 3, 2, 7, 4, 5, 6]
print(max(numbers)) # 最大值
print(min(numbers)) # 最小值
print(sum(numbers)) # 求和

# 列表解析
squares = [value**2 for value in range(1, 10)]
print(squares)

# 使用列表的一部分
# 切片 [要创建切片, 可指定要使用的第一个和最后一个元素的索引+1]
computers = ['Macbook', 'Macbook Pro', 'iMac', 'Mac Pro']
print(computers[1:2]) # 获取 1 <= 索引 < 2 的元素
print(computers[1:]) # 获取 1 <= 索引 的元素
print(computers[:2]) # 获取 索引 < 2 的元素
print(computers[:-1]) # 获取最后一个元素之前的元素
print(computers[-3:]) # 获取最后三个元素

# 遍历切片
for computer in computers[1:3]:
    print(computer.upper())

# 复制列表
# 通过创建一个省略索引限制的切片
wanna_food = ['apple', 'pear', 'banana']
print(wanna_food)
buy_food = wanna_food[:]
print(buy_food)
# 若不使用切片. 直接将旧列表赋值到新数组, 则相当于直接引用同一列表, 而非拷贝副本