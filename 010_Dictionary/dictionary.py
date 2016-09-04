# 字典
# Python 中字典是一系列键值对.
# 键和值之间用 : 分隔, 键-值对之间用 , 分隔
book_0 = {'name': 'Swift', 'price': 22}
book_1 = {'name': 'Python', 'price': 22}

# 访问字典中的值
# 字典中的所有键
print(book_0.keys())
# 字典中的所有值
print(book_0.values())
# 要获取与键相关联的值, 可以依次指定字典名和放在方括号内的键
print(book_0['name'] + ': ' + str(book_0['price']))
print(book_1['name'] + ": " + str(book_1['price']))

# 创建一个空字典
book_2 = {}
print(book_2)

# 添加键值对
# 要添加键-值对, 可依次指定字典名、用方括号括起来的键和关联的值
book_2['author'] = 'Gubis'
print(book_2)

# 修改字典中的值
# 依次指定字典名、用方括号括起来的键和更新的值
book_2['author'] = "Guibs82"
print(book_2)

# 删除键值对
# [del]
del book_2['author']
print(book_2)

# 遍历字典
# [dictionary.items()]
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("Key: " + key)
    print("Value: " + value)

# 遍历字典中所有的键
# [.keys()]
for key in user_0.keys():
    print("With .keys() " + key + " and value is " + user_0[key])
for key in user_0:
    print("Without .keys() " + key + " and value is " + user_0[key])

# 按顺序遍历字典中的所有键
# [sorted()]
for key in sorted(user_0.keys()):
    print("Sorted key is " + key)

# 遍历字典中所有的值
for value in user_0.values():
    print(value)
# 若字典中含有大量重复的值, 为了剔除重复值, 可以使用集合 set
# [set()]
favorite_languages = {
    'Guibs': 'Swift_and_Python',
    'Guibs82': 'Swift_and_Python',
    'Someone': 'Python'
}
for value in favorite_languages.values():
    print("Without set() value is " + value)
for value in set(favorite_languages.values()):
    print("With set() value is " + value)

# 嵌套
# 字典、列表可以相互嵌套
# 列表中存储字典
books = [book_0, book_1, book_2]
for book in books[:1]:
    print(book)
# 字典中存储列表
pizza = {
    'name': 'B_Pizza',
    'size': ['small', 'big'],
    'price': [10, 15],
}
print(pizza)
# 字典中存储字典
price = {
    'small': 20,
    'big': 25,
}
pizza = {
    'name': 'G_Pizza',
    'size': ['small', 'big'],
    'price': price
}
print(pizza)