import math
import pandas as pd
from SNRCompute import SNR

# date = '2021/01/03'
# filepath = 'E:/Python/NEA/data/2021_01_03.csv'
# # # filepath = '/home/maoym/PycharmProjects/Asteroid/' + tablename + '.csv'
# data = pd.read_csv(filepath, header=None, index_col=None)  # 用第一列的数据作为行索引 不要列索引
# params = {
#     'A_eff':math.pi*(0.5**2 -0.15**2), #有效光圈大小
#     'solidangle':1.028, # 每像素立体角，单位：角秒
#     'optical_trans':0.8, # 透光率
#     'noise_r':7, # 读出噪声
#     'noise_d':0.0001, # 暗流噪声
#     'N0':5.79*10**10,
#    # 'N0':1,
#     'qe':0.8, # 量子效率
#     'T_int':60, # 曝光时间
# }
#
# def det(vb,seeing,lat,k):
#     nums = data.shape[0]
#
#     detected_list = []
#     for i in range(nums):
#         #  取第i行数据
#         # print(type(data.iloc[i])) #<class 'pandas.core.series.Series'>
#         v = data.iloc[i][4]
#         mag = data.iloc[i][3]
#         id = data.iloc[i][0]
#
#         a = SNR(date, mag, v, params,1,vb,seeing,lat,k)
#         snr = a.snr()
#         if snr > 3:
#             detected_list.append(id)
#     return detected_list
#
# #xuyi
# re1 = det(21,2.7,32,0.55)
# print(re1)

re1 = [13412.0, 13893.0, 21881.0, 22415.0, 27443.0, 31491.0, 31953.0, 54057.0, 54129.0, 58085.0, 60890.0, 62695.0, 63690.0, 74253.0, 83791.0, 84667.0, 84932.0, 93541.0, 93691.0, 93880.0, 98028.0, 108700.0, 109621.0, 109992.0, 111226.0, 125479.0, 128258.0, 128468.0, 129472.0, 134266.0, 138871.0, 149721.0, 153339.0, 155305.0, 158461.0, 158501.0, 161706.0, 168317.0, 168516.0]
#根据id 得到直径
def D(detected):
    # 找出id对应的H并计算出D的值
    # 总数据统计 H_0
    # 检测列表数据统计 H_detected
    with open('E:/Python/NEA/Soft03Unusual_expansion_sorted.txt','r') as f:

        H_detected = []
        # 读取小行星轨道根数数据
        data_0 = f.readlines()
        for line in data_0:
            tmp = line.split(',')
            if tmp[0] in detected:
                H_detected.append(float(tmp[11]))

    from D_H import H2D
    D_detected = H2D(H_detected)
    #返回总数的统计和检测列表的统计
    return D_detected

detected = []
for i in range(len(re1)):
    detected.append(str(re1[i])[:-2])

print(D(detected))
# 一次观测的直径数据
#[0.017159467113721006, 0.0913899370502672, 0.2608745281889616, 0.1402025046648677, 0.024173301889596866, 0.024344721941946246, 0.28810209666187586, 0.026630220175457065, 0.08330358275067891, 0.5701061321752714, 0.09991245860144621, 0.10764815481030368, 0.89880786514177, 0.029432283243496924, 0.10706500427088074, 0.23238676531020955, 0.08061239176353002, 0.23662817188665544, 0.016767794109063497, 0.7296976852875275, 2.425690282052066, 0.02497074602545296, 0.171402862081893, 0.1825019951491155, 0.41510110473985573, 0.5637931463161691, 0.02700093836133638, 0.11686290156769437, 0.18760163331366672, 0.42184870517008105, 0.42136327415325264, 1.5300849812415367, 0.12562365465973377, 0.7583331465121006, 0.05066280209468726, 0.531866000725687, 0.15830036704969525, 0.461704101805703, 4.128130821688681]
