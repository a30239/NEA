# 计算多天的检测率 表示检测的完备度
# 需要进行计算的日期 单独列为一个程序

import datetime
from detected_rate import detect_result

def days(startdate,enddate):
    datestart = datetime.datetime.strptime(startdate, '%Y/%m/%d')
    dateend = datetime.datetime.strptime(enddate, '%Y/%m/%d')
    dayslist = []
    while datestart < dateend:
        datestart += datetime.timedelta(days=1)
        dayslist.append(datestart.strftime('%Y/%m/%d'))
    # 不包括startdate 在结果中直接添加
    dayslist.insert(0,startdate)
    return dayslist


# 计算多次
startdate = '2020/12/21'
enddate = '2020/12/27'

# 总数 180970
num = 18097

day = days(startdate,enddate)
# 用字典保存 每日的检测率 {'2020/12/21': 0.0021550533237553187, '2020/12/22': 0.0022213626567939436,
detect_completion = {}
for i in range(len(day)):
    # date 表示计算第i天的检测率 统计第一天到第i天的检测结果
    dates = days(startdate,day[i])
    result = detect_result(dates)
    deteceted_rate = len(result)/num
    detect_completion[day[i]] = deteceted_rate

# for key,value in detect_completion.items():
#     print(type(key),value)

print(detect_completion)

# 绘制完备度分布图
# 横坐标为日期 纵坐标为检测率（百分比
date = [key for key,value in detect_completion.items()]
rate = [value for key,value in detect_completion.items()]

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.xlabel('date')
plt.ylabel('completion')
# 设置纵坐标为百分比
# def to_percent(temp, position):
#   return '%1.0f'%(10*temp) + '%'
# plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

plt.plot(date,rate)
plt.show()