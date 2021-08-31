# 绘制分布图与原始的数据分布进行比较验证
# 归一化画在同一张图上

# 原数据处理
with open('E:/Python/asteroid/Soft03Unusual_new.txt','r') as f:
    a_0 = []
    e_0 = []
    inclination_0 = []
    #H_0 = []
    # 读取小行星轨道根数数据
    data_0 = f.readlines()
    for line in data_0:
        tmp = line.split(',')
        a_0.append(float(tmp[5]))
        e_0.append(float(tmp[7]))
        inclination_0.append(float(tmp[2]))
       # H_0.append(float(tmp[11][1:]))

    print('原数据：',len(data_0))
# 模拟数据处理
with open('E:/Python/asteroid/Soft03Unusual_expansion_sorted.txt','r') as f:
    a = []
    e = []
    inclination = []
    #H = []
    # 读取小行星轨道根数数据
    data = f.readlines()
    for line in data:
        #取数据行
        tmp = line.split(',')
        #取a,e,i 第3，6，8个字段
        a.append(float(tmp[5]))
        e.append(float(tmp[7]))
        inclination.append(float(tmp[2]))
       # H.append(float(tmp[11]))

    print('模拟数据:',len(data))


# print('原数据H的取值范围：',min(H_0),max(H_0))
# print('模拟数据H的取值范围：',min(H),max(H))
#
#画图
import matplotlib.pyplot as plt
# 刻度向内  要在plt.plo之前。且，plt.grid、plt.xlabel、plt.ylabel要放在最后
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'




# ax.xaxis.tick_top()
# ax.tick_params(labeltop=False)

# #轨道半长轴的直方分布图
# plt.xlabel('Semimajor axis/au')
# plt.ylabel('Frequency')
# plt.xlim(0,4)
# # 原数据红色 模拟数据蓝色
# plt.hist(a,bins=100,density=True,facecolor='blue',edgecolor='black',alpha=0.4)
# plt.hist(a_0,bins=100,density=True,facecolor='red',edgecolor='black',alpha=0.4)


#
# #轨道偏心率的直方分布图
# plt.xlabel('Eccentricity')
# plt.ylabel('Frequency')
# plt.hist(e,bins=20,density=True,facecolor='blue',edgecolor='black',alpha=0.4)
# plt.hist(e_0,bins=20,density=True,facecolor='red',edgecolor='black',alpha=0.4)


#倾角的直方分布图
plt.hist(inclination,bins=30,density=True,facecolor='blue',edgecolor='black',alpha=0.4)
plt.hist(inclination_0,bins=30,density=True,facecolor='red',edgecolor='black',alpha=0.4)
plt.xlim(-5,100)

plt.xlabel('Inclination/°')
plt.ylabel('Frequency')


plt.savefig('./1-3.png',dpi = 500)

plt.show()