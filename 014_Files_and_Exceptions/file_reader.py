# 文件读取

# 读取整个文件
# 函数 open 接收一个参数: 要打开的文件的名称
# Python 在当前执行的文件所在目录中查找指定的文件
# 关键字 with 在不再需要访问文件后将其关闭.
# 通过 with, Python 可以自己控制关闭文件的时机, 防止自行通过 open() close() 导致程序出错
# 使用 read() 读取文件的全部内容.
# read() 在到达文件末尾时, 返回一个空字符串, 这个字符串显示出来就是一个空行
# 可以使用 .rstrip() 删除多余空行

with open('file_text/pi_digits.txt') as file_object_1:
    contents = file_object_1.read()
    print(contents.rstrip())

# 注: 在 PyCharm 中, 无论是否使用 .rstrip() 都会出现空行
#     在终端中, 无论是否使用 .rstrig() 都不会出现空行

# 文件路径
# 可以使用相对路径/绝对路径

# OS X / Linux
# [/]
# with open('text_files_path/filename.txt') as file_object:
# Windows
# [\]
# with open('text_files_path\filename.txt') as file_object:

# 逐行读取
with open('file_text/pi_digits.txt') as file_object_2:
    for line in file_object_2:
        print(line.rstrip()) # 使用.rstrip() 去除每一行后的空行

# 创建一个包含文件各行内容的列表
# [.readlines()] 从文件中读取每一行, 将其存储在一个列表中
with open('file_text/pi_digits.txt') as file_object_3:
    lines = file_object_3.readlines()
# 此时可以在 with 代码块外访问 lines
for line in lines:
    print(line.rstrip()) # 使用.rstrip() 去除每一行后的空行
