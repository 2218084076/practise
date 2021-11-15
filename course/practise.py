
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = 'False'
data1=np.loadtxt('中国进出口总额年度数据(1).csv',delimiter=',',dtype=str)
data2=np.loadtxt('中国进出口总额年度数据(1).csv',delimiter=',',dtype=float,skiprows=1,usecols=(1))
data3=np.loadtxt('中国进出口总额年度数据(1).csv',delimiter=',',dtype=float,skiprows=2,usecols=(2,3))
p1=plt.figure(figsize=(20,20))
#1.年度总额进出口折线图、散点图
ax1=p1.add_subplot(3,2,1)
plt.plot(data2)
plt.xticks(range(0,20,1),data1[range(1,21,1),0],rotation=45)
plt.title('年度进出口总额的折线图')

ax2=p1.add_subplot(3,2,2)
plt.scatter(range(0,20,1),data2)
plt.xticks(range(0,20,1),data1[range(1,21,1),0])
plt.title('年度进出口总额的散点图')
#2.2019年出口总额、进口总额饼图和直方图
ax3=p1.add_subplot(3,2,3)
label=["2019年出口总额(人民币)(亿元)","2019年进口总额(人民币)(亿元)"]
plt.pie(data3[0,:],explode=[0.01,0.01],labels=label,autopct='%1.1f%%')
plt.title('2019年出口总额(人民币)(亿元)、进口总额(人民币)(亿元)的饼图')

ax4=p1.add_subplot(3,2,4)
label=["2019年出口总额(人民币)(亿元)","2019年进口总额(人民币)(亿元)"]
plt.bar(range(2),data3[0,:],width=0.5)
plt.xticks(range(2),label)
plt.title('2019年出口总额(人民币)(亿元)、进口总额(人民币)(亿元)的直方图')
#3出口总额、进口总额箱型图
ax5 = p1.add_subplot(3,2,5)
label2=['出口总额(人民币)(亿元)','进口总额(人民币)(亿元)']
gbp=(list(data3[:,0]),list(data3[:,1]))
plt.boxplot(gbp,labels=label2)
plt.title('出口总额(人民币)(亿元)、进口总额(人民币)(亿元)的箱体图')
plt.show()