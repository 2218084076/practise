import numpy as np
import pandas as pd
import openpyxl
import xlrd

# 读取数据为orders的数据框
file = '订单.xlsx'
orders =  pd.read_excel(file)
# print('=====> orders数据框 <=====\n',orders.head(5))

# 统计数据中缺失值大于3个字段的记录，并删除，打印出删除的条目
# print('=====> 统计数据中缺失值大于3个字段的记录，并删除，打印出删除的条目 <=====\n')

low_profit=[]
# m, n = orders.shape
print(orders.shape)
# print(m,n)
# print('每列缺省值个数')
# a = orders.isnull().any().sum()
# print(a)

# for i in b :
#     i = int(i)
#     if i > 3:
#         print(i)
#
#     else:
#         print('No')
#
# for i in range(0, m):
#     for j in range(0,n):
#         if orders.loc[i, j] == 'X':
#             orders.loc[i, j] = None


print('=====> 统计“利润”小于零的所有“订单 ID”； <=====')
a = orders[['订单 ID','利润']]
a1 = a.dropna()
print(a1[['利润']].isnull().sum())
print(a[['利润']].isnull().sum())
n,m = a.shape
print(n)
for i in range(0,n):
    if a1.iloc[i,1] < 0 :
        low_profit.append(a1.iloc[i,0])
        # print('利润为：',a1.iloc[i,1])
        print('ID：',a1.iloc[i,0])
print(low_profit)

'''1.处理“订单.xlsx”数据，要求：
（1）读取数据为orders的数据框；
（2）统计数据中缺失值大于3个字段的记录，并删除，打印出删除的条目；
（3）统计“利润”小于零的所有“订单 ID”；
（4）对“销售额”数据求均值并打印；
（5）将处理后的数据框保存到Mysql数据库中，表名为“订单”（仅写出代码即可）。
'''
# print('=====> 对“销售额”数据求均值并打印 <=====')
# print(orders['销售额'].mean())