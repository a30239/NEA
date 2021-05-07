import math
#import numpy as np

#无self参数则不能在同一个类中调用
class SNR():
    # 输入参数
    # x作为定性分析影响因素时暂时添加的参数
    # 增加dec 赤纬 用于计算大气消光
    def __init__(self,date,mag,v,params,dec,vb,seeing,lat,k):
        self.date = date
        self.mag = mag
        self.v = v
        self.params = params
        self.dec = dec
        self.vb = vb
        self.seeing = seeing
        self.lat = lat
        self.k = k


    def signal(self):
        A_eff = self.params['A_eff']
        qe = self.params['qe']
        optical_trans = self.params['optical_trans']
        #path_trans = self.params['path_trans']
        path_trans = self.path_trans()
        N0 = self.params['N0']
        Vm = self.mag
        T_int = self.params['T_int']

        signal = A_eff*qe*optical_trans*path_trans*N0*10**(-0.4*Vm)*T_int

        return signal


    def noise(self):
        noise_r = self.params['noise_r']
        noise_d = self.params['noise_d']
        A_eff = self.params['A_eff']
        qe = self.params['qe']
        optical_trans = self.params['optical_trans']
        #path_trans = self.params['path_trans']
        path_trans = self.path_trans()
        N0 = self.params['N0']
        T_int = self.params['T_int']
        solidangle = self.params['solidangle']

        noise_b = A_eff*solidangle*qe*optical_trans*path_trans*N0*10**(-0.4*self.VB())

        noise = ((noise_r**2+noise_d*T_int+noise_b*T_int)*self.n_p()+self.signal())**0.5

        return noise

    def snr(self):
        return (1 / 2.1 ** (0.5)) *self.signal()/self.noise()

    #

    def path_trans(self):
        # 地理纬度转化为弧度单位
        lat = self.lat
        geolat = lat*math.pi/180
        z = self.dec-geolat
        Xz = 1/math.cos(z) #secz
        # 消光系数
        k = self.k
        path_trans = 10**(-0.4*k*Xz)

        return path_trans

    # 天光背景星等
    def VB(self):
        VB = self.vb
        #VB = 22
        return VB
    # 视宁度
    def seeing_FWHM(self):
        #seeing_FWHM = 0.75
        seeing_FWHM = self.seeing
        return seeing_FWHM

    # 半径与视宁度的关系
    def R(self):
        R = 3*self.seeing_FWHM() / (2 * (2 * math.log(2)) ** 0.5)
        return R

    def n_p(self):
        solidangle = self.params['solidangle']
        T_int = self.params['T_int']

        Sn_p = math.pi * self.R() ** 2 + 2 * self.v *self.R()* T_int
        n_p = Sn_p/solidangle
        return n_p

    # def n_p(self):
    #     n_p = 0.8
    #     return n_p

    #测试类中函数的相互调用 加self
    # def te(self):
    #     print(self.optical_params['A_eff'])
    #     seeing = self.seeing()
    #     print(seeing)

    # def seeing(self):
    #     # 生成满足卡方分布的随机数 从中随机抽取一个作为seeing的值
    #     seeingDis = np.random.chisquare(1,100)
    #     seeing = np.random.choice(seeingDis,1)
    #     return seeing[0]
#
# # 使用字典传递参数
# def opticalParameter(**kwargs):
#     optical_param = {}
#     for key,value in kwargs.items():
#         optical_param[key] = value
#     return optical_param
#
# optical_params = opticalParameter(A_eff = 1**2 -0.15**2,solidangle = 1.028,optical_trans=0.9)
# print(optical_params['A_eff'])

# params = {
#     'A_eff':math.pi*(1**2 -0.15**2), #有效光圈大小
#     'solidangle':1.028, # 每像素立体角，单位：角秒
#     'optical_trans':0.8, # 透光率
#     'path_trans':1, # 光程透过率
#     'noise_r':7, # 读出噪声
#     'noise_d':1, # 暗流噪声
#     'N0':5.79*10**10,
#     'qe':0.8, # 量子效率
#     'T_int':60, # 曝光时间
# }
# params = {
#     'A_eff':math.pi*(0.5**2 -0.15**2), #有效光圈大小
#     'solidangle':1.028, # 每像素立体角，单位：角秒
#     'optical_trans':0.8, # 透光率
#     'noise_r':7, # 读出噪声
#     'noise_d':0.0001, # 暗流噪声
#     'N0':5.79*10**10,
#     'qe':0.8, # 量子效率
#     'T_int':60, # 曝光时间
# }
#
#
# a = SNR(1,22.25,9.616183055709266e-09,params,-0.05313665300778733,21,2.7,32,0.55)
# print(a.path_trans())
# print(a.noise())
# print(a.snr())