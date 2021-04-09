# 计算已知近地小行星数据
# 2021年1月1日
import ephem
import datetime
from vCompute import vcompute
import csv

date = '2021/01/01'

# 根据日期建立数据表
tablename = date.replace('/', '_')
filepath = 'E:/Python/NEA/limitmag/' + tablename + '.csv'
# filepath = 'E:/Python/asteroid/' + tablename + '.csv'
# 日期转换 计算前一天的数据用于计算速度
date1 = datetime.datetime.strptime(date, '%Y/%m/%d')  # 当天
date0 = (date1 - datetime.timedelta(days=1)).strftime('%Y/%m/%d')  # 前一天的日期
with open('E:/Python/NEA/limitmag/Soft03Unusual_new.txt', 'r') as f:
    for line in f.readlines():
        yh = ephem.readdb(line)
        # 相对测站
        # gatech = ephem.Observer()
        # gatech.lon, gatech.lat = '118.54436', '33.011971'  # 测站经纬度 弧度
        # gatech.date = date
        # 统一坐标 地心坐标
        yh1 = ephem.readdb(line)
        yh1.compute(date)
        yh2 = ephem.readdb(line)
        yh2.compute(date0)  # 前一天的数据
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

        newline = [id, vra, vdec, vmag, v]
        # newline=''消除空行
        with open(filepath, 'a', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerow(newline)