# 使用文件的内容
filename = 'pi_digits.txt'

with open('file_text/' + filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string[:13] + "...") # 显示13位
print(len(pi_string))

# 读取文本文件时, Python 将其中的所有文本都解读为字符串
# 若读取的是数字, 则需要使用 int() 或 float() 进行转换

# 检测某个字段是否包含在文件内
num = input("输入一个三位数:\n")
if num in pi_string:
    print("你输入的数字在文件中存在")
else:
    print("你输入的数字在文件中不存在")