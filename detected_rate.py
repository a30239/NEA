# 根据保存的检测列表 计算检测率
# 用字典保存 检测次数

# 统计多天的检测结果 第1天到第i天的 输出为一个字典 {id:次数}
# 输入为需要计算的日期的list (输入所有需要计算的日期

def detect_result(dates):
    result = {}
    for date in dates:
        # 检测列表保存成文件
        txtname = date.replace('/', '_')
        filepath = 'E:/Python/NEA/data/' + txtname + '.txt'
        #filepath = '/home/maoym/PycharmProjects/Asteroid/' + txtname + '.txt'
        with open(filepath, 'r') as f:
            # 去除前后的[] 只取列表中的值
            detected_list = f.readline()[1:-1].split(',')
            for id in detected_list:
                if id not in result:
                    result[id] = 1
                else:
                    result[id] += 1
    return result





# dates = ['2020/12/21', '2020/12/22', '2020/12/23', '2020/12/24', '2020/12/25', '2020/12/26', '2020/12/27']
# re = detect_result(dates)
# detected = []
#
# for key,value in re.items():
#     detected.append(key[2:-1])
# # 第一个数据格式不同 手动添加
# detected.append('433 Eros')
# # if "'433 Eros'" in detected:
# #     print('true')
# with open('E:/Python/asteroid/Soft03Unusual_new.txt','r') as f:
#     a_0 = []
#     e_0 = []
#     a_detected = []
#     e_detected = []
#     # 读取小行星轨道根数数据
#     data_0 = f.readlines()
#     for line in data_0:
#         tmp = line.split(',')
#         a_0.append(float(tmp[5]))
#         e_0.append(float(tmp[7]))
#         if tmp[0] in detected:
#             a_detected.append(float(tmp[5]))
#             e_detected.append(float(tmp[7]))
# print(len(a_detected))
#
# import matplotlib.pyplot as plt
#
# plt.xlabel('Semimajor axis(AU)')
# plt.ylabel('Eccentricity')
# plt.xlim(0,4)
# plt.scatter(a_0,e_0,s=10)
# plt.scatter(a_detected,e_detected,s=10)
# # plt.plot(a_0,e_0,'o','b')
# # plt.plot(a_detected,e_detected,'o','g')
# plt.show()




# txtname = date.replace('/', '_')
# filepath = 'E:/Python/asteroid/' + txtname + '.txt'
# result = {}
# with open(filepath,'r') as f:
#     # 去除前后的[] 只取列表中的值
#     detected_list = f.readline()[1:-1].split(',')
#     for id in detected_list:
#         if id not in result:
#             result[id] = 1
#         else:
#             result[id] += 1
# print(result)