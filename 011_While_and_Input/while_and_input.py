# While And Input

# input()
# input() 接收一个参数: 即要向用户显示的提示或说明
message = input("告诉我你想跟我说的话, 我会重复你的话~\n")
print("你说: " + message)

# 使用 int() 来获取数值输入
age = input("你多大?\n")
print('那么. 你明年' + str(int(age) + 1) + '了')

# 使用 while 循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# 1 2 3 4 5

# 使用标志来控制循环
activity = True
num = 1
while activity:
    print("Hello")
    num += 1
    if num == 3:
        activity = False
# Hello Hello

# 使用 break 退出循环
current_number = 1
while current_number <= 5:
    if current_number != 3:
        print(current_number)
        current_number += 1
    else:
        break
# 1 2

# 使用 continue 跳入下一次循环
current_number = 1
while current_number <= 5:
    if current_number != 3:
        print(current_number)
        current_number += 1
    else:
        current_number += 1
        continue
# 1 2 4 5

# 使用 while 处理列表和字典
unconfirmed_users = ['Alice', 'Guibs', 'Mike']
confirmed_users = []
print("未确认名单: " + str(unconfirmed_users))
print("已确认名单: " + str(confirmed_users))
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print(current_user + " 已确认")
print("未确认名单: " + str(unconfirmed_users))
print("已确认名单: " + str(confirmed_users))

# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'rabbit']
while 'dog' in pets:
    pets.remove('dog')
print(pets)

# 使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("叫什么名字\n")
    response = input("喜欢什么\n")
    responses[name] = response
    repeat = input("是否继续添加?是/否\n")
    if repeat == '否':
        polling_active = False
print(responses)