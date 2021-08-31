# 按年份统计

idList = []
dateList = []
with open('E:/Python/NEA/Known/neoobs.all', 'r') as f:
    data = f.readlines()
    for i in range(len(data)):
        line = data[i].split()
        id = line[0]
        date = line[3]
        if date[:4] == '2017':
            dateList.append(date[:10])
            if id not in idList:
                idList.append(id)

print(len(idList))
print(len(dateList))

# # 统计观测次数
# datenums = len(list(set(dateList)))
# print(datenums)


#
with open('E:/Python/NEA/Known/Soft03Unusual_new.txt','r') as f2:
    id_0 = []
    H_0 = []
    # 读取小行星轨道根数数据
    data_0 = f2.readlines()
    for line in data_0:
        tmp = line.split(',')
        idtmp = tmp[0].split()[1:]
        id_0.append(''.join(idtmp))
        H_0.append(float(tmp[11][1:]))


HList = []
for i in range(len(id_0)):
    if id_0[i] in idList:
        HList.append(H_0[i])

print(len(HList))
print(HList)