
import pandas as pd
# （1）读取数据，将数据存成变量iris

print('# （1）读取数据，将数据存成变量iris')
iris = pd.read_csv(r'D:\__easyHelper__\iris.csv')
print(f'iris.head(5)\n{iris.head(5)}')

# 创建数据框的列名称['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class’]
print('# 创建数据框的列名称["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]')
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
print(f'iris.columns\n{iris.columns}')

# 数据框中有缺失值吗？
print('# 数据框中有缺失值吗\n')
print(iris.isnull())

# 将列petal_length的第十到十九行设置为缺失值。
# 将petal_lengt缺失值全部替换为1.0。
iris.loc[8: 19, 'petal_length'] = None
iris['petal_length'].fillna(1.0, inplace=True)

# 删除列class
print('# 删除列class')
del iris['class']
print(iris.head(5))

# 将数据框前三行设置为缺失值。
iris.iloc[0: 3, :] = None

# 删除有缺失值的行。
iris.dropna(how='any', inplace=True)

# 重新设置索引。
iris.reset_index(drop=True, inplace=True)
