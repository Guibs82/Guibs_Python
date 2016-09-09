from name_function import get_formatted_name

print("输入 q 退出程序")
while True:
    first = input("你叫啥名\n")
    if first == 'q':
        break
    last = input("你姓什么\n")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("您的全名是: " + formatted_name)

