import json

# 如果以前存储了名字, 就加载
# 如果以前没存储名字, 就提示用户输入并存储

filename = 'username.json'

try:
    with open("json/" + filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("请问您叫什么名字")
    with open("json/" + filename) as f_obj:
        json.dump(username, f_obj)
        print("我会将你记在心中的, " + username)
else:
    print("Hi, " + username + ", 很高兴又能和你重逢~")