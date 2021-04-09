# 对处理后的新文件进行插值
# 3-9 列直接进行插值 12列 H 对字母后的数字进行插值 并将H添加回去
# 2，10，11，13列 同一值

# 定义插值函数
from scipy import interpolate
import numpy as np

# 对数据进行插值 data为进行插值的数据 list
def interpolation(data,n):
    x = np.linspace(0,len(data)-1,len(data))
    # 数据扩充为10倍 linspace(start,stop,numbers)
    x_new = np.linspace(0,len(data)-1,n*len(data))
    # 选择插值函数
    # "nearest","zero"为阶梯插值
    #  slinear 线性插值
    # "quadratic","cubic" 为2阶、3阶B样条曲线插值
    f = interpolate.interp1d(x, data, kind='slinear')
    data_new = f(x_new)

    return data_new

# H 绝对星等的扩展函数
#写成函数供调用 输入生成数量n 输出H list形式
def expansion_H(n):
    # 分布函数
    def N(x):
        return 942 * x ** (-2.354)
    #H与D的转化公式
    import math
    def D2H(D):
        H = []
        pv = 0.14
        for i in D:
            H.append(15.618 - 2.5 * math.log10(pv) - 5 * math.log10(i))
        return H

    a = 942
    b = 2.354
    # 归一化c 0.01-30
    c = N(0.01) - N(30)

    x = np.random.rand(n)  # 产生均匀分布的随机数
    # 利用反函数求符合该分布的随机变量
    D_new = [(c / a * (1 - i)) ** (-1 / b) for i in x]
    #转换到H
    H_new = D2H(D_new)

    return H_new

# 提取需要插值的数据列
with open('E:/Python/asteroid/Soft03Unusual_new.txt','r') as f:
    # 每一列一个list(共13列 第一列不取 直接编号
    lists = [[] for _ in range(13)]
    # 读取小行星轨道根数数据
    data = f.readlines()
    for line in data:
        #取数据行
        tmp = line.split(',')
        # 只取需要进行插值的数据
        lists[2].append(float(tmp[2])) #i
        lists[3].append(float(tmp[3])) #O
        lists[4].append(float(tmp[4]))  #o
        lists[5].append(float(tmp[5]))  #a
        lists[6].append(float(tmp[6]))  #n
        lists[7].append(float(tmp[7]))  #e
        lists[8].append(float(tmp[8]))  #M
        #lists[11].append(float(tmp[11][1:])) #H 不取字母


# 输入数据扩展倍数
n = int(input('数据扩展倍数：'))
# 对数据进行扩充 扩展10倍
new_lists = [[] for _ in range(13)]
# 编号 取顺序值
new_lists[0] = [_ for _ in range(n*len(data))]
# 类型 都为e 表示对象类型为椭圆日心
new_lists[1] = ['e' for _ in range(n*len(data))]
# E epoch date 取原值
new_lists[9] = ['09/04.0/2017' for _ in range(n*len(data))]
# D the equinox year 取原值
new_lists[10] = ['2000' for _ in range(n*len(data))]
# G (H,G)的G 取0.15
new_lists[12] = ['0.15' for _ in range(n*len(data))]
# 其他列进行插值 调用interpolation函数
new_lists[2] = interpolation(lists[2],n)
new_lists[3] = interpolation(lists[3],n)
new_lists[4] = interpolation(lists[4],n)
new_lists[5] = interpolation(lists[5],n)
new_lists[6] = interpolation(lists[6],n)
new_lists[7] = interpolation(lists[7],n)
new_lists[8] = interpolation(lists[8],n)
#new_lists[11] = interpolation(lists[11])
#H的值通过分布计算得到
new_lists[11] = expansion_H(n*len(data))


# print(len(new_lists[0])) 180970

# 写入txt文件 注意格式转换
with open ('E:/Python/asteroid/Soft03Unusual_expansion_sorted.txt','w') as f:
    for i in range(len(new_lists[0])):
        # 每一行 取出 字符串格式
        # 每一行后面添加换行符
        # TODO H是否需要在前面加上字母
        line = ','.join(str(new_lists[j][i]) for j in range(len(new_lists))) + '\n'
        f.write(line)

