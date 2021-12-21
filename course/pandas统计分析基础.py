import numpy as np
import pandas as pd

# # 将字典转为数据框
d = {'color': ['blue', 'green', 'yellow', 'red', 'white'],
     'object': ['ball', 'pen', 'pencil', 'paper', 'mug'],
     'price': [1.2, 1.0, 0.6, 0.9, 1.7]}
df2 = pd.DataFrame(d)
print(f'=====> {df2} <=====')

# 将列表转为数据框
d = [[1.3, 2.0, 3, 4], [2, 4, 1, 4], [2, 5, 1.9, 7], [3, 1, 0, 11]]
df1 = pd.DataFrame(d, columns=['A', 'B', 'C', 'D'], index=['a', 'b', 'c', 'd'])
print(f'=====> {df1} <=====')

# 数据框的索引&切片
print(df1.iloc[0, 0])      # 方式一：通过元素的行列位置(顺序)进行索引/切片
print(df1.iloc[2, 2])
print(df1.iloc[:2, 0:2])
print(df1.iloc[:, 0])

print(df1.loc['a', 'A'])            # 方式二：通过元素的行列名称进行索引/切片
print(df1.loc['a':'b', 'A':'B'])    # 注意，利用行列名称进行切片时，取出的元素范围是闭区间

print(df1['A'])             # 方式三：访问单列/多列元素
print(df1[['A', 'C']])

print(df1.loc[[True, False, False, True], :])    # 方式四：通过逻辑值进行数据访问
print(df1.loc[df1['A'] >= 3, :])

# 修改数据框中的元素
df1.iloc[0, 0] = 10.01
df1.loc[:, 'B'] = [1, 2, 3, 4]

# 在数据框中新增元素
df1['E'] = 1.3
df1.loc['e', :] = 0.25

# 删除数据框中的元素
df1.drop('E', axis=1)    # 删除指定的行/列元素
# df1_1 = df1.drop(['a', 'e'], axis=0)
df1.drop(['a', 'e'], axis=0, inplace=True)    # 直接在df1上执行删除操作

# 描述分析数据框的元素
df1.values      # 数据框的值（数组结构的）
df1.index       # 数据框的行索引
df1.columns     # 数据框的列索引
df1.shape       # 查看数据框的尺寸

df1.mean(axis=1)
df1.mean(axis=0)
df1.max()          # 取出每列元素的最大值
df1.idxmax()       # 取出每列元素最大值的索引(行名称)

# pd.max(df1)      # 非法操作，pandas中没有提供max函数

# 数据文件的读取
iris = pd.read_csv('iris_test.csv', sep=',')
meal_order = pd.read_excel('meal_order_detail.xlsx', sheet_name='meal_order_detail1')

# 分组聚合
grouby1 = meal_order.groupby(by='order_id').agg({'counts': 'sum'})    # 先依据order_id对数据框分组，然后对counts列执行求和操作
meal_order.groupby(by='order_id').agg({'counts': ['sum', 'count']})   # 先依据order_id对数据框分组，然后对counts列执行求和及计数操作
# 先依据order_id对数据框分组，然后对counts列执行求和及计数操作、对amounts列执行求均值操作
meal_order.groupby(by='order_id').agg({'counts': ['sum', 'count'], 'amounts': 'mean'})
meal_order.groupby(by='order_id').agg('mean')  # 先依据order_id对数据框分组，然后对其余所有列执行求均值操作


