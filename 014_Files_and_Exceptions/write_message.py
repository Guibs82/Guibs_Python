# 写入空文件
# ['w'] 写入模式
# ['r'] 读取模式
# ['a'] 附加模式[追加内容, 非覆盖]
# ['r+'] 能够读取和写入文件的模式
filename = 'programming.txt'


with open("file_text/" + filename, 'w') as file_object:
    file_object.write("Lean Python\n")

# 写入多行文件
with open("file_text/" + filename, 'w') as file_object:
    file_object.write("Python" + str(3) + "\n") # 若要将数字存储到文本文件中, 必须使用 str() 将数字转换为字符串
    # 写入多行
    # [.write()] 不会自动追加换行符
    file_object.write("人生苦短, 我用 Python3\n")

# 附加到文件[追加内容]
with open("file_text/" + filename, 'a') as file_object:
    file_object.write("Guibs\n")

