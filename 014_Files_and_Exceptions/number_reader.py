# json.load() 读取数据

import json

filename = 'number.json'

with open("json/" + filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)