# 存储用户输入的数据
import json

username = input("你叫什么名字?\n")

filename = 'username.json'

with open("json/" + filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("我已经将你深深刻在我的心里~")

