import shutil
import pygal

from die import Die

# 创建一个 D6 和 D10 [8面骰子]
die_1 = Die()
die_2 = Die(10)

# 抛几次骰子, 并将结果存储在一个数组中
results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

# 分析结果
frequencies = []

for value in range(2, die_1.num_sides + die_2.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "抛 D6 和 D10 骰子的和"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "结果"
hist.y_title = "次数"

hist.add('D6 + D10', frequencies) # 柱状图注释及数值
hist.render_to_file('die_visual.svg')

# 移动生成图片的位置
shutil.move("die_visual.svg", 'images/die_visual.svg')