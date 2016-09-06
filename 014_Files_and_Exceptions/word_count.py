def count_words(filename):
    """计算一个文件中有多少单词"""
    try:
        with open("file_text/" + filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # pass # pass 可以用于告知 Python 什么也不做

        with open("file_text/wanna.txt", 'w') as f_obj2:
            '''写入不存在的文件名'''
            f_obj2.write(filename)
    else:
        # 计算文件中单词数量
        words = contents.split()  # 按空格分割
        num_words = len(words)
        print(filename + "共有" + str(num_words) + "个单词")

filename = 'alice.txt'
count_words(filename=filename)

# 计算多个文件的所含词汇量
filenames = ['alice.txt', 'alice2.txt', 'alice3.txt', 'alice4.txt']

for filename in filenames:
    count_words(filename)
