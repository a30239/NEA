# 根据日期 计算指定天数的数据

import datetime
import time

#计算运行时间
start = time.time()

# 需要进行计算的日期
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

#print(days('2020/12/21','2020/12/27'))

from ephemCompute import dataCompute

# 输入变量 起始日期
startdate = input('输入开始日期(格式：xxxx/xx/xx)：')
enddate = input('输入结束日期(格式：xxxx/xx/xx)：')

dayslist = days(startdate,enddate)
for day in dayslist:
    dataCompute(day)


end = time.time()
total = end-start
print('time:',total)

