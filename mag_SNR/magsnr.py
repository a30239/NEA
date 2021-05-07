# # 2021年1月2日 在两个观测站 对模拟样本库中所有数据
# 一次检测的信噪比和视星等
#
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
   # 'N0':1,
    'qe':0.8, # 量子效率
    'T_int':60, # 曝光时间
}

date = '2021/1/1'
filepath = 'E:/Python/NEA/data/2021_01_03.csv'
# # filepath = '/home/maoym/PycharmProjects/Asteroid/' + tablename + '.csv'
data = pd.read_csv(filepath, header=None, index_col=None)  # 用第一列的数据作为行索引 不要列索引
# # 保存可被检测出的目标的id 用于在计算多日时进行去重
detectedSNR =[]
detectedmag = []


#
# nums = data.shape[0]
#
# for i in range(nums):
#     #  取第i行数据
#     # print(type(data.iloc[i])) #<class 'pandas.core.series.Series'>
#     v = data.iloc[i][4]
#     mag = data.iloc[i][3]
#     id = data.iloc[i][0]
#     a = SNR(date, mag, v, params,1,21,2.7,32,0.55)
#     print(a.n_p())

def det(vb,seeing,lat,k):
    nums = data.shape[0]
    mag_0 = []
    snr_0 = []
    res = []
    for i in range(nums):
        #  取第i行数据
        # print(type(data.iloc[i])) #<class 'pandas.core.series.Series'>
        v = data.iloc[i][4]
        mag = data.iloc[i][3]
        id = data.iloc[i][0]
        mag_0.append(mag)
        a = SNR(date, mag, v, params,1,vb,seeing,lat,k)
        snr = a.snr()
        snr_0.append(snr)
        res.append(a.path_trans)
    return [snr_0,mag_0]

#xuyi
re1 = det(21,2.7,32,0.55)

#lenghu
re2 = det(22,0.75,38,0.15)

# with open('./result1.txt', 'w') as f:
#     f.write(str(re1))
# with open('./result2.txt', 'w') as f:
#     f.write(str(re2))

import matplotlib.pyplot as plt
#plt.hist(H0,bins=100,alpha=0.3)
plt.ylabel('SNR')
plt.xlabel('Apparent visual magnitude V')
plt.scatter(re1[1],re1[0],s= 10,label='Xuyi')
plt.scatter(re2[1],re2[0],s= 10,label='Lenghu')
# 画一条snr=3的线
plt.axhline(y=3, color='r', linestyle='-',label='SNR=3')
plt.axhline(y=10, color='b', linestyle='-',label='SNR=10')
plt.axhline(y=30, color='r', linestyle='-',label='SNR=30')
plt.yscale('log')
plt.legend(loc='best')
plt.xlim(18,30)
plt.ylim(1,1000)
plt.savefig('./mag-snr.png')
plt.show()