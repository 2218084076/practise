'''
使用numpy生成一个100*5的数组A，
要求每一列数据是随机生成的整数、求解数组A每一行的平均值，并将计算结果存储再100*1的数组B中。
这里数组A第i行的平均值存储在数组B的第i个元素中。
将计算结果存储再文件avg.csv中，要求采用GB2312编码。将代码和运行结果截图上交
'''
import pandas as pd
import numpy as np

A=np.random.randint(0,100,size=[100,5],dtype='int')
print('数组A：\n%s'%(A))
B = np.mean(A,axis=1)
# print(type(average_value))
print('average_value=\t%s'%(B))
new_B = np.array(B).reshape(100,1)
print(new_B)
dataframe = pd.DataFrame(new_B)
print(dataframe)
dataframe.to_csv('avg.csv',encoding="GB2312")