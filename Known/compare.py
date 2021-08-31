import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

x1 = [_ for _ in range(5)]
x2 = [_+0.4 for _ in range(5)]
#



# #总数
# z = [3191, 4757, 4481, 4401, 1267]
# # xuyi历史观测数据统计
# z1 = [0, 2, 66, 578, 512]
# # 仿真结果统计
# z2 =  [2, 12, 52, 267, 177]



# # 已知样本总数
# z = [3191, 4757, 4481, 4401, 1267]
# # xuyi历史观测数据统计
# z1 = [0, 2, 66, 578, 512]
# #xuyi 一年的仿真结果统计
# z2 =  [152, 84, 47, 7, 2]
# # 模拟样本总数
# z3 = [167533, 12654, 724, 54, 5]

# 根据模型计算的样本总数
z = [3621658, 3408819, 196809, 15087, 942]
# xuyi历史观测数据统计2020年
z1 = [0, 1, 16, 108, 151]
# # 07-21年的观测数据
# z1 = [0, 2, 66, 578, 512]

#xuyi 一年的仿真结果统计
z2 = [152, 84, 47, 7, 2]
# 模拟样本总数
z3 = [167533, 12654, 724, 54, 5]
#实际观测除以观测天数
y1 = [z1[i]/z[i] for i in range(len(z))]
y2 = [z2[i]/z3[i] for i in range(len(z))]

#设置纵坐标为百分比
def to_percent(temp,pos):
  return '%1.0f'%(100*temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))


name = ['0-0.03','0.03-0.1','0.1-0.3','0.3-1','1+']


plt.bar(x1, y1,width=0.4,label='Observation')
plt.bar(x2, y2,width=0.4,tick_label=name,label='Simulation')

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
#plt.savefig('./pic/completionbins1y_g.png')
plt.show()