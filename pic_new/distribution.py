# 使用模拟后保存的数据文件Soft03Unusual_expansion_sorted.txt
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
#
# # a e i 的直方分布图 归一化画在同一张图上（density=True
# plt.figure(1)
#
# plt.subplot(2,3,1)
# #轨道半长轴的直方分布图
# plt.xlabel('Semimajor axis(AU)')
# plt.ylabel('Numbers frequency')
# plt.xlim(0,4)
# # 原数据红色 模拟数据蓝色
# plt.hist(a,bins=100,density=True,facecolor='blue',edgecolor='black',alpha=0.4)
# plt.hist(a_0,bins=100,density=True,facecolor='red',edgecolor='black',alpha=0.4)

#plt.subplot(2,3,2)
# #轨道偏心率的直方分布图
# plt.xlabel('Eccentricity')
# plt.ylabel('Numbers frequency')
# plt.hist(e,bins=20,density=True,facecolor='blue',edgecolor='black',alpha=0.4)
# plt.hist(e_0,bins=20,density=True,facecolor='red',edgecolor='black',alpha=0.4)

#plt.subplot(2,3,3)
#倾角的直方分布图
# plt.xlabel('Inclination(deg)')
# plt.ylabel('Numbers frequency')
# plt.hist(inclination,bins=30,density=True,facecolor='blue',edgecolor='black',alpha=0.4)
# plt.hist(inclination_0,bins=30,density=True,facecolor='red',edgecolor='black',alpha=0.4)
# plt.xlim(-5,100)

#
# #绘制二维直方图（热力图
# #横轴为轨道半长轴，纵轴为轨道偏心率
# plt.figure(2)
#
#
# plt.subplot(2,1,1)
# plt.xlabel('Semimajor axis(AU)')
# plt.ylabel('Eccentricity')
# plt.hist2d(a_0,e_0,bins=50,range=[[0,5],[0,1]],cmap=plt.cm.jet)
# plt.colorbar()

# plt.subplot(2,1,2)

# 刻度向内  要在plt.plo之前。且，plt.grid、plt.xlabel、plt.ylabel要放在最后
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'


plt.xlabel('(b)      Semimajor axis/au')
plt.ylabel('Eccentricity')
plt.hist2d(a,e,bins=50,range=[[0,5],[0,1]],cmap=plt.cm.rainbow)
plt.colorbar().set_label('Numbers')

# # H的分布 累积分布 分开画

# plt.figure(3)
#
# plt.subplot(2,1,1)
# plt.xlabel('Abs.Magnitude H')
# plt.ylabel('Numbers')
# plt.hist(H_0,bins=50,facecolor='red', edgecolor='black', alpha=0.3)
# #plt.yscale('log')
# #plt.xlim(9,35)
#
# plt.subplot(2,1,2)
# plt.xlabel('Abs.Magnitude H')
# plt.ylabel('Numbers')
# plt.hist(H,bins=50,facecolor='blue', edgecolor='black', alpha=0.3)
# #plt.yscale('log')
# #plt.xlim(9,35)
plt.savefig('./2-2.png')

plt.show()