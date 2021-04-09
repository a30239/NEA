# 计算位置星等 存入csv文件

import time
import ephem
import pandas as pd
import csv
import datetime
from vCompute import vcompute

# #计算运行时间
# start = time.time()

#读入小行星根数数据 date 字符串格式 日期格式转换定义一个函数
def dataCompute(date):
    # 根据日期建立数据表
    tablename = date.replace('/', '_')
    filepath = 'E:/Python/NEA/data/' + tablename + '.csv'
    # filepath = 'E:/Python/asteroid/' + tablename + '.csv'
    # 日期转换 计算前一天的数据用于计算速度
    date1 = datetime.datetime.strptime(date, '%Y/%m/%d')  # 当天
    date0 = (date1 - datetime.timedelta(days=1)).strftime('%Y/%m/%d')  # 前一天的日期
    # 根据模拟数据进行计算
    #with open('/home/maoym/PycharmProjects/Asteroid/Soft03Unusual_expansion_sorted.txt', 'r') as f:
    with open('E:/Python/NEA/Soft03Unusual_expansion_sorted.txt', 'r') as f:
        for line in f.readlines():
            yh = ephem.readdb(line)
            # 相对测站
            # gatech = ephem.Observer()
            # gatech.lon, gatech.lat = '118.54436', '33.011971'  # 测站经纬度 弧度
            # gatech.date = date
            # 统一坐标 地心坐标
            yh1 = ephem.readdb(line)
            # 计算时间 精确到具体时间
            date_n = date+' 23:59:59'
            yh1.compute(date_n)
            yh2 = ephem.readdb(line)
            date0_n = date0+' 23:59:59'
            yh2.compute(date0_n)  # 前一天的数据
            # 时分秒和度分秒的转换 转换为弧度单位
            vra = float(yh1.ra)
            vdec = float(yh1.dec)
            vmag = str(yh1.mag)
            # 计算速度
            vra0 = float(yh2.ra)
            vdec0 = float(yh2.dec)
            v = vcompute(vra, vdec, vra0, vdec0)
            id = line.split(',')[0]

            # 写入txt
            # newline = str(id)+','+str(vra)+','+str(vdec)+','+str(vmag)+'\n'
            # with open(filepath,'a') as f2:
            #     f2.write(newline)
            # 写入csv 1146.6s
            # newline = {'id':[id],'ra':[vra],'dec':[vdec],'mag':[vmag]}
            # df = pd.DataFrame(newline)
            # df.to_csv(filepath, mode='a', encoding='utf-8', header=False, index=False,sep=',')

            newline = [id,vra,vdec,vmag,v]
            #newline=''消除空行
            with open(filepath,'a',newline='') as f2:
                writer = csv.writer(f2)
                writer.writerow(newline)



# dataCompute('2020/12/21')

#
# end = time.time()
# total = end-start
# print('time:',total)
