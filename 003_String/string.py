# 字符串

# Python 中, 用引号括起来的都是字符串. 引号可以是单引号, 也可以是双引号
"This is a string"
'This is also a string'
# 因而可以在字符串中包含 " 或 '
'I told myself, "you are Gubis"'
"The name 'Guibs' is my nickname"

# 首字母大写指定字符串
# [.title()]
name = 'Macbook pro'
print(name.title())

# 全部大写指定字符串
# [.upper()]
print(name.upper())

# 全部小写字符串
# [.lower()]
print(name.lower())

# 合并(拼接)字符串
# [使用 + 拼接字符串]
first_name = "guibs"
last_name = 'g'
full_name = first_name + " " + last_name
print(full_name)

hello_message = "Hello, " + full_name.title() + "!"
print(hello_message)

# 制表符
# [\t]
print("Python")
print("\tPython")

# 换行符
# [\n]
print("123")
print("1\n2\n3")

# 删除字符串空白
# [.rstrip() 删除字符串末尾多余空白]
print("删除字符串 Swift and Python 末尾多余空白")
favorite_language = " Swift and Python "
print(favorite_language + " are my favorite languages")
print(favorite_language.rstrip() + " are my favorite languages" + "\n")
# [.lstrip() 删除字符串开头多余空白]
print("删除字符串 Swift and Python 开头多余空白")
print(favorite_language + " are my favorite languages")
print(favorite_language.lstrip() + " are my favorite languages" + "\n")
# [.strip() 删除字符串头尾多余空白]
print("删除字符串 Swift and Python 头尾多余空白")
print(favorite_language + " are my favorite languages")
print(favorite_language.strip() + " are my favorite languages" + "\n")

# 正确使用引号
# 保留 "" 显示
print('I told myself, "you are Gubis"')
# 保留 '' 显示
print("The name 'Guibs' is my nickname")