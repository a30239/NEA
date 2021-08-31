# 统计观测数据 观测目标编号和时间




idList = []
with open('E:/Python/NEA/Known/neoobs.all','r') as f:
    data = f.readlines()
    for i in range(len(data)):
        line = data[i].split()
        id = line[0]
        if id not in idList:
            idList.append(id)


print(idList)

# 根据编号查找绝对星等 转换为直径

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

#print(H_0)
HList = []
for i in range(len(id_0)):
    if id_0[i] in idList:
        HList.append(H_0[i])
#print(HList)

