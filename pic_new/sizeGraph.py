import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

x1 = [_ for _ in range(5)]
x2 = [_+0.4 for _ in range(5)]
#
# 总数量统计： [167533, 12654, 724, 54, 5]
# 检测列表数量统计1： [213, 123, 52, 7, 2]
# 检测列表数量统计2： [1261, 550, 119, 14, 2]

#总数
z = [167533, 12654, 724, 54, 5]
# xuyi
z1 = [33, 15, 14, 2, 2]

# lenghu
z2 = [235,135, 54, 7, 2]


y1 = [z1[i]/z[i] for i in range(len(z))]
y2 = [z2[i]/z[i] for i in range(len(z))]



# 刻度向内  要在plt.plo之前。且，plt.grid、plt.xlabel、plt.ylabel要放在最后
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

#设置纵坐标为百分比
def to_percent(temp,pos):
  return '%1.0f'%(100*temp) + '%'

plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))


name = ['0-0.03','0.03-0.1','0.1-0.3','0.3-1','1+']


plt.bar(x1, y1,width=0.4,label='Xuyi')
plt.bar(x2, y2,width=0.4,label='Lenghu')

plt.xticks([_+0.2 for _ in x1],name)

plt.xlabel('$D$/km')
plt.ylabel('Detection rate')
# 添加百分比
for x, y in enumerate(y1):
    tmp = str(round(100*y, 2))+'%'
    print(tmp)
    plt.text(x, y+0.15/20,tmp, ha='center')
for x, y in enumerate(y2):
    tmp = str(round(100*y, 2))+'%'
    plt.text(x+0.45, y+0.15/20,tmp, ha='center')

plt.legend(loc='best')
# 四面都显示刻度
plt.tick_params(top=True,bottom=True,left=True,right=True)
#plt.savefig('./5.eps')
plt.show()

