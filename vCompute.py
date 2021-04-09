# 计算目标运动的视速度
import math
import numpy as np

# 输入 今天的位置和前一天的位置
def vcompute(ra1,dec1,ra2,dec2):
    # 前一天减去后一天的位置 除以 时间
    # dis_ra = ra1-ra2
    # dis_dec = dec1-dec2
    # 相差的角度（弧度制
    AOB = math.acos(math.sin(dec1) * math.sin(dec2) + math.cos(dec1) * math.cos(dec2) * math.cos(ra1 - ra2))
    #s = 2 * math.asin(math.sqrt(math.pow(math.sin(dis_dec/2),2)+math.cos(dec1)*math.cos(dec2)*
                                # math.pow(math.sin(dis_ra/2),2)))
    # d不应该乘以地球半径 乘轨道半长径？
    #d = s*6378.137*1000
    v = AOB/24/3600
    return v



# def seeing():
#     # 生成满足卡方分布的随机数 从中随机抽取一个作为seeing的值？
#     seeingDis = np.random.chisquare(4,100)
#     seeing = np.random.choice(seeingDis,1)
#     print(min(seeingDis),max(seeingDis))
#     return seeing[0]
#
# # 半径与视宁度的关系
# def R(seeing_FWHM):
#     R = seeing_FWHM/(2*(2*math.log(2))**0.5)
#     return R
#
# def n_p(R,t,v):
#     n_p = (math.pi*R**2+2*v*t*R)
#     return n_p
#
# v = vcompute(3.0602963888959707,-0.04763147562298675,3.061661355948813,-0.048263989662485476)
# print(v*3600*24)
# print(n_p(R(2.7),60,v))




