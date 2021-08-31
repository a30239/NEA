# 现有数据 模型分布 模拟数据分布图
# 保存图片

# 取原数据
with open('E:/Python/asteroid/Soft03Unusual_new.txt','r') as f:
    H0 = []
    # 读取小行星轨道根数数据
    data = f.readlines()
    for line in data:
        tmp = line.split(',')
        H0.append(float(tmp[11][1:]))

import math
def H2D(H):
    D = []
    # pv 反照率 取0.14
    pv = 0.14
    for i in H:
        D.append(math.pow(10,3.1236-0.2*i-0.5*math.log10(pv)))
    return D
def D2H(D):
    H = []
    pv = 0.14
    for i in D:
        H.append(15.618-2.5*math.log10(pv)-5*math.log10(i))
    return H
# 模拟数据
with open('E:/Python/asteroid/Soft03Unusual_expansion_sorted.txt','r') as f:
    H1 = []
    # 读取小行星轨道根数数据
    data = f.readlines()
    for line in data:
        tmp = line.split(',')
        H1.append(float(tmp[11]))

import numpy as np
import matplotlib.pyplot as plt

# #绝对星等
# #plt.xlabel('Abs.Magnitude H')
# plt.xlabel('D')
# plt.ylabel('Numbers')
# # 以对数作为纵坐标
# plt.yscale('log')
# plt.xscale('log')
#
# plt.hist(H2D(H0), bins=50, cumulative=True,facecolor='blue', edgecolor='black',alpha=0.3)
# #plt.hist(H1, bins=50, cumulative=True,facecolor='blue', edgecolor='black',alpha=0.3)
# #plt.gca().invert_xaxis()


# 刻度向内  要在plt.plo之前。且，plt.grid、plt.xlabel、plt.ylabel要放在最后
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

#根据已知公式画出函数图 双对数坐标
D = np.arange(0.001,100,0.1)
H = D2H(D)
N = 942*D**(-2.354)
plt.yscale('log')
#plt.xscale('log')
plt.plot(H,N,linestyle='--')

# # 根据已知分布求出N
# D = H2D(H0)
# N = [942*i**(-2.354) for i in D]


plt.xlabel('H / mag')
plt.ylabel('N')
plt.yscale('log')
#plt.xscale('log')
#plt.scatter(H0,N)
#plt.gca().invert_xaxis()

plt.annotate(text='Size distribution model',xy=(22,1000000),xytext=(22,10000000),weight='medium',color='black',\
             arrowprops=dict(arrowstyle='-|>',connectionstyle='arc3',color='black'))
plt.annotate(text='Distribution of simulation data',xy=(24,1000),xytext=(28,10),weight='medium',color='black',\
             arrowprops=dict(arrowstyle='-|>',connectionstyle='arc3',color='black'))
plt.annotate(text='Distribution of known data',xy=(30,10000),xytext=(32,800000),weight='medium',color='black',\
             arrowprops=dict(arrowstyle='-|>',connectionstyle='arc3',color='black'))
#plt.xlim(14.67,27.75)
plt.xlim(9.5,33)

print(min(H1))
#原始数据的分布
plt.hist(H0, cumulative=True,histtype='step',bins=50,facecolor='red', edgecolor='red')
#plt.hist(D_new, bins=50,facecolor='blue', edgecolor='black', alpha=0.3)
plt.hist(H1,bins=30,cumulative=True,histtype='step')
plt.gca().invert_xaxis()

plt.savefig('./3.png')
plt.show()