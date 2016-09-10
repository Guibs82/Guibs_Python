import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个 RandomWalk 实例, 并将其包含的点都绘制起来
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘制窗口大小
    # figsize 单位为英寸
    # dpi: 像素/英寸 [Python 默认值80]
    plt.figure(dpi=128, figsize=(10, 6))

    point_orders = list(range(rw.num_points))
    # c=point_numbers, cmap=plt.cm.Blues 根据点的先后顺序进行蓝色的映射
    plt.scatter(rw.x_values, rw.y_values, edgecolors='none', s=1, c=point_orders, cmap=plt.cm.Blues)

    # 重绘起点终点从而突出
    plt.scatter(0, 0, c='green', edgecolors='none', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', edgecolors='none', s=20)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # 关闭绘制的图片后, 询问是否再次绘制
    rw_again = input("是否再次绘制?(y/n):\n")
    if rw_again == 'n':
        break