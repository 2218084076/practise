import pandas as pd
# d={'color':['blue','green','yellow','red','white'],
#    'object':['ball','pen','pencil','paper','mug'],
#    'price':[1.2,1.0,0.6,0.9,1.7]}
#
# df2 = pd.DataFrame(d)
# print('=====df2# 将字典转为数据框=====\n',df2)
#
# # 将列表转为数据框
#
d = [[1.3, 2.0, 3, 4], [2, 4, 1, 4], [2, 5, 1.9, 7], [3, 1, 0, 11]]
df1 = pd.DataFrame(d, columns=['A', 'B', 'C', 'D'], index=['a', 'b', 'c', 'd'])
# print('=====将列表转为数据框=====\n',df1)
#
# 数据框的索引&切片
print('# 数据框的索引&切片')
print(f'df1.iloc[0, 0]\t{df1.iloc[0, 0]}')      # 方式一：通过元素的行列位置(顺序)进行索引/切片
print(f"df1.iloc[2, 2]=\t{df1.iloc[2, 2]}")
print(f'df1.iloc[:2, 0:2]\t{df1.iloc[:2, 0:2]}')
print(f'df1.iloc[:, 0]\t{df1.iloc[:, 0]}')
#
# print(f'方式二：通过元素的行列名称进行索引/切片\t{df1.loc["a", "A"]}')            # 方式二：通过元素的行列名称进行索引/切片
# print("注意，利用行列名称进行切片时，取出的元素范围是闭区间\n",df1.loc['a':'b','A':'B'])    # 注意，利用行列名称进行切片时，取出的元素范围是闭区间
#
# print(' 方式三：访问单列/多列元素\n',df1['A'])
# print("df1[['A', 'C']]\n",df1[['A', 'C']])
print('方式四：通过逻辑值进行数据访问')
print(df1.loc[[True, False, False, True], :])    # 方式四：通过逻辑值进行数据访问
print(df1.loc[df1['A'] >= 3, :])



# 数据框的常用属性
# d=[[1.3,2.0,3,4],[2,4,1,4],[2,5,1.9,7],[3,1,0,11]]
# df = pd.DataFrame(d, index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])
# print(df)
# print('values\n',df.values)
# print('index\n',df.index)
# print('shape\n',df.shape)
# print('dtypes\n',df.dtypes)
# print('axis=1\n',df.mean(axis=1))
# print('axis=0\n',df.mean(axis=0))
