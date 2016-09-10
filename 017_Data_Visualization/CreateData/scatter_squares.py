# 散点图
# [scatter()]

import shutil

import matplotlib.pyplot as plt

x_values = list(range(1, 1001)) # [1, 2, 3, 4,..., 999, 1000]
y_values = [x**2 for x in x_values] # [ 1, 4, 9, 16,..., 999*999, 1000*1000]

# 点默认为蓝色黑轮廓
# s=40 设置点的大小
# edgecolors='none' 删除数据点的轮廓
# c='red' c=(0.1, 0.2, 0.3) 设置点的颜色 [c 可以是特定颜色的单词 或 0~1的三位数元组]
# plt.scatter(x_values, y_values, edgecolors='none', s=40, c=(0.1, 0.5, 1))

# 使用颜色映射
# c=y_values, cmap=plt.cm.Blues 根据 y_values 来设置蓝色的颜色映射. 值越大, 色越深
plt.scatter(x_values, y_values, edgecolors='none', s=40, c=y_values, cmap=plt.cm.Blues)

# 设置图标标题, 并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel('值', fontsize=14)
plt.ylabel('值的平方', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 保存生成的图标 [要放在 plt.show() 前面]
# 保存路径为此 py 文件所在路径
p_name = 'squares_plot.png'
plt.savefig(p_name, bbox_inches='tight')

# 移动生成图片的位置
shutil.move(p_name, 'images/' + p_name)
print("a")

# 打开 matplotlib 查看器, 并显示绘制的图形
plt.show()