import pandas as pd
import math
from SNRCompute import SNR

#
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
#xuyi
vb,seeing,lat,k = 21,2.7,32,0.55
# #lenghu
# vb,seeing,lat,k = 22,0.75,38,0.15

date = '2021/01/01'
filepath = 'E:/Python/NEA/limitmag/2021_01_01.csv'
# # filepath = '/home/maoym/PycharmProjects/Asteroid/' + tablename + '.csv'
data = pd.read_csv(filepath, header=None, index_col=None)  # 用第一列的数据作为行索引 不要列索引
#输出检测目标的视星等
detectedmag = []
nums = data.shape[0]


for i in range(nums):
    dec = data.iloc[i][2]
    ra = data.iloc[i][1]
    mag = data.iloc[i][3]
    v = data.iloc[i][4]
    id = data.iloc[i][0]
    # print(type(mag)) #<class 'numpy.float64'>
    a = SNR(date, mag, v, params, dec,vb,seeing,lat,k)
    snr = a.snr()
    if snr > 3:
        detectedmag.append(mag)

print(detectedmag)
