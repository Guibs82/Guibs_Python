import csv

from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f) # 阅读器对象
    header_row = next(reader)

    # 由输出可以看到, 最高气温是 index 1
    # for index, column_header in enumerate(header_row):
        # print(index, column_header)

    highs = [] # 高温
    lows = [] # 低温
    dates = [] # 日期
    for row in reader:
        """使用 try_except 避免无数据情况"""
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except:
            print(current_date + ": 该日无气温最值")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    print(highs)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')
    plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.5)

    # 设置图形的格式
    plt.title("2014 最高气温")
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # 绘制斜的标签
    plt.ylabel("华氏度", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()