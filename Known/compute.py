# 根据模型计算各个区间的数量


# 分布函数
def N(x):
    return 942 * x ** (-2.354)

print(N(1))
print(N(0.3)-N(1))
print(N(0.1)-N(0.3))
print(N(0.03)-N(0.1))
print(N(0.03))