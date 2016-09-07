# 重构

import json

def greet_user():
    """问候用户"""
    filename = "username.json"
    try:
        with open("json/" + filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("请问你叫什么?")
        filename = "username.json"
        with open("json/" + filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("我已将你记在心中~")
    else:
        print("Hi " + username + ", 很高兴再次看了你~ ")

greet_user()