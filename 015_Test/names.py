from name_function import get_formatted_name

print("输入q跳出程序")
while True:
    first = input("你叫什么?\n")
    if first == 'q':
        break
    last = input("你姓什么?\n")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("你的名字是: " + formatted_name)