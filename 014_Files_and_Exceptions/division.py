# 异常
# 异常使用 try-except 处理

# ZearoDivisionError 异常
try:
    res = 5 / 1
except ZeroDivisionError:
    print("0不能作为被除数")
else:
    # 以来 try 代码块成功后执行的代码都应该放到 else 代码块中
    print(res)