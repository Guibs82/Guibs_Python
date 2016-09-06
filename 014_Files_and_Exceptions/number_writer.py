# json.dump() 存储数据

import json
import os

numbers = [2, 3, 5, 7, 11, 13]

filename = 'number.json'

# 判断路径是否存在, 不存在则创建
if os.path.isdir('json'):
    pass
else:
    os.mkdir('json')

try:
    with open("json/" + filename, 'w') as f_obj:
        json.dump(numbers, f_obj)
except FileNotFoundError:
    os.mkdir("json/")