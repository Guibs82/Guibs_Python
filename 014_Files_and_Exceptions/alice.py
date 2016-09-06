filename = "alice.txt"

try:
    with open("file_text/" + filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("文件未找到")
else:
    # 计算文件中单词数量
    words = contents.split() # 按空格分割
    num_words = len(words)
    print(filename + "共有" + str(num_words) + "个单词")
