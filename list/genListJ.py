# 生成模拟图像星表 均匀分布的

# 100 x y mag

import pandas as pd
import numpy as np

mag_0 = np.linspace(15,25,16384)
print(mag_0)
# 坐标按顺序取
# 取其中的16384颗=128*128
# magList = mag_0[:16384]
num = len(mag_0)
print(num)
x = []
for i in range(128):
    x.append(40+80*i)
X = x*128
Y = []
for i in range(num):
    Y.append(x[i//128])

# print(x)
#示意图
import matplotlib.pyplot as plt
plt.hist(mag_0,bins=100,alpha=0.3)

plt.ylabel('Numbers')
plt.xlabel('Apparent visual Magnitude V')
plt.show()
#
# # 写入星表文件.list
# for i in range(num):
#     tmp = ['100', str(X[i]), str(Y[i]), str(mag_0[i])]
#     line = (' '.join(tmp)+'\n')
#     with open('E:/Python/NEA/list/mag.list', 'a', encoding='utf-8') as f:
#         f.write(line)