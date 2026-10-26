# 量化小白的学习记录

这是我的个人作品集，用来记录我学习量化交易的过程，以及思考。python,VS Code

## Day1

- `p1.ipynb`： Python-numpy 提取并计算股票量化指标的代码（数据文件：demo.csv）。
- `demo.csv`：测试用的数据样本文件，条数20。
- 总结：在unittest测试环境，def定义，利用一个框架完成，最后【启动测试】
- class
-    def testXX(self):
-        file_name='demo.csv'
-        price,volume=np.loadtxt(fname=file_name,delimiter=',',usecols=( , ),unpack=True)
-    print('XX={}'.format())
  
## Day2

- p2.py:numpy 简单/指数移动平均线 卷积(数学)
- `demo.csv`：测试用的数据样本文件，条数20
- 什么是卷积?例如:两组数组相乘,先把一组顺序颠倒,变成'火车'依次与另一组数据交会,交会出对应相乘.(个人理解)
- p3.py :Pandas  股票时间序列-基础序列型数据的基础指标计算  
