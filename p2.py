#简单/指数移动平均线-numpy 卷积
import numpy as np
import matplotlib.pyplot as plt #画图
from unittest import TestCase #测试

class TestNumpyMA(TestCase):

    def testsMA(self):
        file_name='demo.csv'
        end_price,volume=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(2,6),
            unpack=True
        )
        print(end_price)

        N=5
        weight=np.ones(N)/N
        print(weight)  #等权重

#简单移动平均线
        sma=np.convolve(weight,end_price)[N-1:-N+1]
        print(sma)

        plt.plot(sma,linewidth=5)


#指数移动平均线
    def testEXP(self):
        X=np.arange(5)
        Y=np.arange(10)
        print('X',X) 
        print('Y',Y)
        print('''Exp x : {}'''.format(np.exp(X)))#exp可以计算出每个数组元素的指数，指数e的X次方
        print('''Exp y : {}'''.format(np.exp(Y)))
        print('''linespace : {}'''.format(np.linspace(-1,0,5)))#（-1，0是因为是的最后的指数是递增的，t
        #`np.linspace(a,b,N)`：在 `[a,b]` 之间均匀生成 N 个数字



    def testEMA(self):
        file_name='demo.csv'
        end_price,volume=np.loadtxt(
            fname=file_name,
            delimiter=',',
            usecols=(2,6),
            unpack=True
        )
        print(end_price)

#指数移动平均线计算关键-卷积
        N=5
        weighs=np.exp(np.linspace(-1,0,N)) #从小到大的数组
        weighs/=weighs.sum()#归一化
        print('weighs={}'.format(weighs))
        ema=np.convolve(weighs,end_price)[N-1:-N+1]
        #np.convolve卷积，先把权重数组颠倒顺序，再滑动对位相乘求和【-4，4】位置颠倒
        print(ema)

        t=np.arange(N-1,len(end_price))
        plt.plot(t,end_price[N-1:],lw=1.0)
        plt.plot(t,ema,lw=2.0)
        plt.show()
#指数移动平均线更加平缓，越新的价格话语权更大

#【启动测试】
if __name__ == '__main__':
    import unittest
    suite = unittest.TestSuite()
    suite.addTest(TestNumpyMA('testsMA'))
    suite.addTest(TestNumpyMA('testEXP'))
    suite.addTest(TestNumpyMA('testEMA'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #class的类、所测试的功能模块