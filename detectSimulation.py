# 测试七天的模拟数据
# 读取csv文件 并进行计算
# 检测结果输出到以日期命名的txt文件中

import pandas as pd
from SNRCompute import SNR
import math
import time
import datetime
#from gendata import days


def detect(date,params):

    # 计算太阳位置
    import ephem
    gatech = ephem.Observer()
    gatech.date = date
    sun = ephem.Sun()
    sun.compute(gatech)
    ra_sun = float(sun.ra)
    dec_sun = float(sun.dec)

    # 读取csv文件数据 未进行筛选（不进行天区选择
    tablename = date.replace('/', '_')
    filepath = 'E:/Python/NEA/data/' + tablename + '.csv'
    #filepath = '/home/maoym/PycharmProjects/Asteroid/' + tablename + '.csv'
    data = pd.read_csv(filepath, header=None, index_col=None)  # 用第一列的数据作为行索引 不要列索引
    # 保存可被检测出的目标的id 用于在计算多日时进行去重
    detected_list = []
    nums = data.shape[0]
    # print(data.shape[0]) 数据的行数
    for i in range(nums):
        # 增加目标的筛选 去除南纬30度以下的数据
        dec = data.iloc[i][2]
        ra = data.iloc[i][1]
        # 去除太阳附近的目标
        x = 30*math.pi/180
        if dec > -30 * math.pi / 180 and (ra_sun-x>ra or ra>ra_sun+x) and (dec_sun-x>dec or dec>dec_sun+x):
            #  取第i行数据
            # print(type(data.iloc[i])) #<class 'pandas.core.series.Series'>
            mag = data.iloc[i][3]
            v = data.iloc[i][4]
            id = data.iloc[i][0]
            # print(type(mag)) #<class 'numpy.float64'>
            a = SNR(date, mag, v, params, dec)
            snr = a.snr()
            if snr > 3:
                detected_list.append(id)
    return detected_list

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

#计算运行时间
start = time.time()

#  'path_trans':1, # 光程透过率
params = {
    'A_eff':math.pi*(1**2 -0.15**2), #有效光圈大小
    'solidangle':1.028, # 每像素立体角，单位：角秒
    'optical_trans':0.8, # 透光率
    'noise_r':7, # 读出噪声
    'noise_d':0.001, # 暗流噪声
    'N0':5.79*10**10,
    'qe':0.8, # 量子效率
    'T_int':60, # 曝光时间
}

days = days('2021/1/1','2021/1/1')
for date in days:
    detected_list = detect(date,params)
    # 检测列表保存成文件
    txtname = date.replace('/', '_')
    #txtname = 'lenghu'
    filepath = 'E:/Python/NEA/mag_SNR/' + txtname + '.txt'
    #filepath = '/home/maoym/PycharmProjects/Asteroid/' + txtname + '.txt'
    with open(filepath, 'w') as f:
        f.write(str(detected_list))




end = time.time()
total = end-start
print('time:',total)


#
# detected_rate = len(detected_list)/nums
# print(detected_rate)
