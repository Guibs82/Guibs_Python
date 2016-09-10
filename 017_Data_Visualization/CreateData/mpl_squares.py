# 折线图

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5] # x
squares = [1, 4, 9, 16, 25] # y

plt.plot(input_values, squares, linewidth=5) # 根据参数绘制图形, 设置线条宽度

# 设置图标标题, 并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel('值', fontsize=14)
plt.ylabel('值的平方', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show() # 打开 matplotlib 查看器, 并显示绘制的图形