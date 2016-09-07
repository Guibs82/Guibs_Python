# 读取用户存储的数据

import json
filename = "username.json"

with open("json/" + filename) as f_obj:
    username = json.load(f_obj)
    print("又见到你了" + username + ", 好嗨森~")