#股票时间序列  趋势性分析、相关性分析  Pandas时间序列函数
import matplotlib.pyplot as plt
import pandas as pd
from unittest import TestCase

class TestPandasStock(TestCase):
    #读取文件，了解数据
    def testReadFile(self):
        file_name='demo.csv'
        df = pd.read_csv(file_name,header=None)
#跟np选定文件不同，np处理数据无表头概念，read_csv会更加广泛？
        print(df.info())#是否有缺失值、数据类型
        print('------------------')
        print(df.describe())#统计（均值，最值，标准差）


    def testTime(self):
        file_name='demo.csv'
        df=pd.read_csv(file_name,header=None)
        df.columns=['stock_id','date','close','open','high','low','volume']

        df['data']=pd.to_datetime(df['date'])#转成时间类型、以便按照时间划分

        df['year']=df['date'].dt.year
        df['month']=df['date'].dt.month

        print (df)

    #计算最低的收盘价
    def testCloseMin(self):
        file_name='demo.csv'
        df=pd.read_csv(file_name,header=None)
        df.columns=['stock_id','date','close','open','high','low','volume']

        print('''close min : {}'''.format(df['close'].min()))
        print('''close min index : {}'''.format(df['close'].idxmin()))#拿到所在行的下标，知道位置
        print('''close min frame : {}'''.format(df['close'].idxmin()))
        print('''close min id:{}'''.format(df.loc[df['close'].idxmin()]))#获取这只产品的所有信息

#每月的平均收盘价和开盘价
    def  testMean(self):
        file_name='demo.csv'
        df=pd.read_csv(file_name,header=None)
        #read_csv默认第一行是表头，不想就加上header=None
        df.columns=['stock_id','date','close','open','high','low','volume']

        df['date']=pd.to_datetime(df['date'])
        df['month']=df['date'].dt.month 
        print('''month close mean:{}'''.format(df.groupby('month')['close'].mean()))#按月分组求收盘价的平均值
        print('''month open mean:{}'''.format(df.groupby('month')['open'].mean()))
  
#计算涨跌
    def testRipples_ratio(self):
        file_name='demo.csv'
        df=pd.read_csv(file_name,header=None)
        df.columns=['stock_id','date','close','open','high','low','volume']
        df['date']=pd.to_datetime(df['date'])

        df['rise']=df['close'].diff()#diff计算收益差（今天-昨日）
        df['rise_ratio']=df['rise']/df.shift(1)['close']

        print(df)

if __name__ == '__main__':
    import unittest
    suite = unittest.TestSuite()
    suite.addTest(TestPandasStock('testReadFile'))
    suite.addTest(TestPandasStock('testTime'))
    suite.addTest(TestPandasStock('testCloseMin'))
    suite.addTest(TestPandasStock('testMean'))
    suite.addTest(TestPandasStock('testRipples_ratio'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

