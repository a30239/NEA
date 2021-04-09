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
z1 = [34, 15, 14, 2, 2]
# lenghu
z2 =  [228, 135, 54, 7, 2]

y1 = [z1[i]/z[i] for i in range(len(z))]
y2 = [z2[i]/z[i] for i in range(len(z))]

#设置纵坐标为百分比
def to_percent(temp,pos):
  return '%1.0f'%(100*temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))


name = ['0-0.03','0.03-0.1','0.1-0.3','0.3-1','1+']


plt.bar(x1, y1,width=0.4,label='Xuyi')
plt.bar(x2, y2,width=0.4,tick_label=name,label='Lenghu')

plt.xlabel('D(km)')
plt.ylabel('Detect completion(%)')
# 添加百分比
for x, y in enumerate(y1):
    tmp = str(round(100*y, 2))+'%'
    print(tmp)
    plt.text(x, y+0.15/20,tmp, ha='center')
for x, y in enumerate(y2):
    tmp = str(round(100*y, 2))+'%'
    plt.text(x+0.45, y+0.15/20,tmp, ha='center')

plt.legend(loc='best')
plt.savefig('./pic/completionbins.png')
plt.show()

# plt.xlabel('D(km)')
# plt.ylabel('Numbers')
#
# plt.bar(x1, z,width=0.8,color='orange',tick_label=name)
# for x, y in enumerate(z):
#     print(x,y)
#
#     plt.text(x, y+0.15/20,y, ha='center')
# plt.savefig('./pic/nums.jpg')
# plt.show()