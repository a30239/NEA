# D与H的关系转换

import math
def H2D(H):
    D = []
    # pv 反照率 取0.14
    pv = 0.14
    for i in H:
        D.append(math.pow(10,3.1236-0.2*i-0.5*math.log10(pv)))
    return D

def D2H(D):
    H = []
    pv = 0.14
    for i in D:
        H.append(15.618-2.5*math.log10(pv)-5*math.log10(i))
    return H

# D取0.01-30时，对应的H的范围
# print(D2H([0.01])[0],D2H([30])[0])
