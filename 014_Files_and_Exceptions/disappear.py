# FileNotFoundError
filename = "disapper.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("没找到这个文件啊亲~")