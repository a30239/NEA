# 用信噪比公式计算均匀分布的视星等的信噪比
# 速度设为0
from SNRCompute import SNR
import math
import pandas as pd

params = {
    'A_eff':math.pi*(0.5**2 -0.15**2), #有效光圈大小
    'solidangle':1.028, # 每像素立体角，单位：角秒
    'optical_trans':0.8, # 透光率
    'noise_r':7, # 读出噪声
    'noise_d':0.0001, # 暗流噪声
    'N0':5.79*10**10,
    'qe':0.8, # 量子效率
    'T_int':60, # 曝光时间
}
with open('./mag.list','r') as f:
    mag = []
    lines = f.readlines()
    for line in lines:
        tmp = line.split()
        mag.append(float(tmp[3][:7]))

vb,seeing,lat,k = 21,2.7,32,0.55
date = '2021/01/01'

#输出检测目标的视星等
detectedmag = []
v = 0
dec = 1
for i in range(len(mag)):

    a = SNR(date, mag[i], v, params, dec,vb,seeing,lat,k)
    snr = a.snr()
    if snr > 3:
        detectedmag.append(mag[i])


print(detectedmag)
