def process(detected):
    ndetected = []
    for i in detected:
        ndetected.append(i.replace(' ',''))
    return ndetected


import pandas as pd
# #读2021年1月1日的检测列表 得到id 找对应的视星等
# with open ('E:/Python/NEA/data/2021_1_1.txt','r') as f:
#     detected_list = f.readline()[1:-1].split(',')
# #检测目标id
# detected = process(detected_list)

detected = ['2784.0', '3466.0', '3587.0', '4997.0', '5317.0', '7504.0', '9704.0', '10293.0', '11368.0', '11501.0', '11512.0', '11654.0', '13416.0', '15702.0', '16471.0', '18834.0', '18959.0', '19181.0', '21781.0', '21881.0', '22311.0', '22415.0', '22620.0', '25092.0', '25852.0', '26317.0', '30549.0', '30707.0', '31491.0', '31637.0', '31953.0', '33874.0', '33985.0', '35340.0', '35341.0', '35845.0', '35921.0', '35965.0', '36005.0', '36235.0', '37127.0', '38237.0', '39240.0', '40042.0', '43511.0', '43972.0', '45447.0', '45959.0', '47050.0', '47675.0', '48040.0', '48382.0', '49013.0', '49017.0', '50330.0', '50538.0', '52900.0', '53135.0', '53137.0', '53249.0', '53411.0', '54043.0', '54057.0', '54129.0', '54334.0', '55084.0', '55320.0', '55981.0', '56221.0', '56260.0', '56622.0', '56955.0', '59225.0', '60890.0', '61075.0', '62561.0', '62580.0', '62695.0', '62774.0', '63532.0', '63694.0', '63948.0', '64710.0', '64982.0', '65441.0', '65821.0', '65979.0', '66163.0', '66189.0', '68788.0', '70527.0', '70584.0', '71190.0', '71214.0', '72246.0', '73024.0', '73153.0', '74023.0', '74253.0', '74885.0', '75597.0', '75725.0', '77299.0', '79084.0', '81052.0', '82599.0', '83114.0', '83487.0', '83791.0', '83915.0', '84424.0', '84667.0', '84932.0', '85132.0', '85622.0', '88901.0', '89099.0', '92003.0', '92006.0', '92771.0', '93494.0', '93691.0', '93936.0', '94107.0', '94139.0', '97975.0', '98028.0', '98660.0', '99612.0', '99733.0', '100278.0', '100653.0', '102761.0', '102937.0', '104696.0', '105057.0', '105292.0', '107585.0', '107624.0', '108840.0', '109992.0', '111288.0', '111695.0', '111791.0', '112178.0', '112734.0', '112915.0', '113046.0', '113126.0', '113435.0', '113438.0', '123529.0', '123804.0', '124143.0', '124498.0', '125767.0', '125878.0', '127193.0', '128258.0', '128468.0', '130950.0', '133669.0', '134578.0', '135212.0', '137172.0', '137937.0', '139775.0', '139777.0', '140131.0', '141446.0', '142948.0', '143745.0', '143859.0', '143897.0', '144320.0', '144523.0', '144656.0', '145020.0', '145097.0', '145408.0', '145695.0', '146305.0', '146332.0', '147061.0', '148646.0', '149786.0', '153261.0', '154258.0', '156035.0', '157828.0', '158026.0', '158461.0', '159272.0', '159381.0', '159727.0', '161409.0', '161772.0', '161977.0', '162095.0', '162828.0', '162852.0', '164629.0', '167722.0', '168317.0', '168516.0', '168887.0', '169002.0', '169015.0', '172591.0', '174514.0', '176193.0', '180173.0']

#
#读取星表 根据id查找对应的视星等值
data = pd.read_csv('E:/Python/NEA/data/2021_1_1.csv', header=None, index_col=None)  # 用第一列的数据作为行索引 不要列索引
#根据id 获取被检测目标的视星等 mag
detected_mag = []
mag_0 = list(data[3])
# nums = data.shape[0]
# # print(data.shape[0]) 数据的行数
# for i in range(nums):
#     id = data.iloc[i][0]
#     mag = data.iloc[i][3]

    # if str(id) in detected:
    #     detected_mag.append(mag)

# print(mag_0)
#
detected_mag = [24.13, 23.68, 23.89, 24.2, 22.27, 22.6, 22.1, 23.07, 23.31, 24.16, 23.24, 24.18, 23.68, 22.83, 24.11, 23.63, 23.46, 22.82, 24.02, 21.03, 22.96, 20.22, 22.28, 24.16, 23.75, 23.34, 22.03, 24.29, 20.92, 22.04, 21.33, 22.04, 22.45, 23.88, 23.19, 23.96, 23.52, 23.57, 23.75, 23.13, 24.23, 23.8, 23.98, 23.66, 24.15, 24.1, 24.07, 23.52, 23.65, 24.09, 23.88, 23.47, 23.49, 23.53, 24.18, 23.99, 23.56, 23.58, 23.75, 23.14, 23.33, 24.15, 21.34, 21.58, 23.56, 22.87, 22.78, 23.99, 24.15, 24.27, 24.24, 24.27, 23.85, 21.26, 22.05, 21.94, 23.5, 21.04, 23.54, 22.61, 23.6, 22.23, 24.05, 23.9, 23.92, 23.46, 24.11, 22.79, 23.05, 23.56, 23.94, 24.06, 22.37, 23.17, 24.1, 23.04, 24.24, 22.59, 21.88, 24.08, 24.17, 23.72, 23.92, 23.44, 23.85, 22.89, 24.19, 23.73, 21.64, 24.29, 22.66, 18.75, 21.92, 22.78, 23.66, 23.4, 23.38, 23.67, 23.58, 22.85, 22.87, 21.95, 24.07, 23.75, 22.55, 22.07, 19.47, 23.23, 23.58, 24.14, 24.13, 23.2, 23.61, 23.6, 22.5, 23.11, 23.97, 22.34, 23.82, 22.08, 19.57, 23.77, 24.03, 22.92, 23.18, 23.81, 23.31, 23.65, 22.55, 23.43, 23.0, 23.63, 24.26, 22.88, 23.89, 24.03, 23.83, 22.34, 21.36, 21.39, 23.87, 23.85, 22.86, 24.16, 24.15, 23.32, 22.6, 23.61, 23.86, 24.01, 23.52, 24.12, 22.79, 23.5, 22.43, 24.04, 22.37, 24.27, 23.81, 23.6, 23.02, 24.05, 24.06, 23.76, 22.67, 23.94, 24.06, 23.13, 22.42, 24.24, 23.51, 21.44, 23.76, 23.49, 23.6, 24.12, 22.85, 23.78, 23.39, 23.34, 23.04, 23.68, 24.08, 19.23, 15.22, 22.85, 23.16, 23.48, 24.15, 23.52, 21.94, 22.42]

#画视星等的分布

import matplotlib.pyplot as plt

plt.ylabel('Numbers')
plt.xlabel('Apparent visual magnitude V')


plt.hist(detected_mag,bins=30,color='orange',label='detect')
# plt.hist(mag_0,bins=100,alpha = 0.8,color='blue',label='all')
plt.legend(loc='best')
plt.xlim(15,25)
plt.savefig('E:/Python/NEA/pic/detectedmag.jpg')
plt.show()