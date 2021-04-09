# 对影响因素进行定性分析
# 选择一天的数据 输入不同的变量值

import numpy as np
import pandas as pd
import math
from SNRCompute import SNR



# 用2020/12/21的数据
filepath = 'E:/Python/asteroid/2020_12_21.csv'
date = '2020/12/21'

params = {'A_eff':math.pi*(1**2 -0.15**2),'solidangle':1.028,'optical_trans':0.8,'path_trans':1,
          'noise_r':7,'noise_d':1,'kf':1,'N0':5.79*10**10,'qe':0.8,'T_int':60}

# 在参数中增加要定性分析的参数
def computeNum(x):
    data = pd.read_csv(filepath, header=None, index_col=None)  # 用第一列的数据作为行索引 不要列索引
    # 保存可被检测出的目标数量
    detected = 0
    nums = data.shape[0]
    # print(data.shape[0]) 数据的行数
    for i in range(nums):
        #  取第i行数据
        # print(type(data.iloc[i])) #<class 'pandas.core.series.Series'>
        mag = data.iloc[i][3]
        v = data.iloc[i][4]
        #id = data.iloc[i][0]
        # # print(type(mag)) #<class 'numpy.float64'>
        a = SNR(date, mag, v, params,x)
        snr = a.snr()
        if snr > 3:
            detected += 1
    return detected

Seeing_FWHM = np.linspace(0.3,3.5,30)
VB = np.linspace(17,27,10)

# 保存每一次的检测数量
detectedNum = []
for i in VB:
    detectedNum.append(computeNum(i))

num = 18097
detection = [i/num for i in detectedNum]
print(detection)
# 画出分布图
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# plt.xlabel('Seeing_FWHM')
plt.xlabel('V_B')
plt.ylabel('detection(%)')
#设置纵坐标为百分比
def to_percent(temp, position):
  return '%1.0f'%(100*temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

plt.ylim(0,1)
#plt.plot(Seeing_FWHM,detection)
plt.plot(VB,detection)
#plt.bar(Seeing_FWHM, detection, align="center", color="orange")
plt.show()