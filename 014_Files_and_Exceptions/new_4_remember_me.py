import json

def get_stored_username():
    """如果存储了用户名就获取"""
    filename = "username.json"
    try:
        with open("json/" + filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("请问你叫什么?")
    filename = "username.json"
    with open("json/" + filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("我已将你记在心中~")
    return username

def greet_user():
    """问候用户, 并指出其名字"""
    username = get_stored_username()
    if username:
        print("Hi " + username + ", 很高兴又看到了你~")
    else:
        username = get_new_username()

greet_user()