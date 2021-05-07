# 生成模拟图像星表
# 100 x y mag

import pandas as pd

# 取视星等参数
date = '2021/1/1'
#真实数据
filepath = 'E:/Python/NEA/limitmag/2021_01_01.csv'
# # filepath = '/home/maoym/PycharmProjects/Asteroid/' + tablename + '.csv'
data = pd.read_csv(filepath, header=None, index_col=None)  # 用第一列的数据作为行索引 不要列索引
nums = data.shape[0]
mag_0 = []
for i in range(nums):
    #  取第i行数据
    # print(type(data.iloc[i])) #<class 'pandas.core.series.Series'>
    v = data.iloc[i][4]
    mag = data.iloc[i][3]
    id = data.iloc[i][0]
    mag_0.append(mag)

print(min(mag_0),max(mag_0))
# 坐标按顺序取
# 取其中的16384颗=128*128
magList = mag_0[:16384]
num = len(magList)
print(num)
x = []
for i in range(128):
    x.append(40+80*i)
X = x*128
Y = []
for i in range(num):
    Y.append(x[i//128])

print(x)
# #示意图
# import matplotlib.pyplot as plt
# #plt.hist(H0,bins=100,alpha=0.3)
# plt.ylabel('Y')
# plt.xlabel('X')
# plt.scatter(X,Y,s=5)
# plt.show()

# # 写入星表文件.list
# for i in range(num):
#     tmp = ['100', str(X[i]), str(Y[i]), str(magList[i])]
#     line = (' '.join(tmp)+'\n')
#     with open('E:/Python/NEA/list/neas.list', 'a', encoding='utf-8') as f:
#         f.write(line)