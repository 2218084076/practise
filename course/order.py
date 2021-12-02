# 该代码用于分析本地excel表格数据
# coding=utf-8

import pandas as pd
import pymysql
pd.set_option('max_columns', 5)
pd.set_option('max_rows', 5)

'''
1.处理“订单.xlsx”数据，要求：
（1）读取数据为orders的数据框；
（2）统计数据中缺失值大于3个字段的记录，并删除，打印出删除的条目；
（3）统计“利润”小于零的所有“订单 ID”；
（4）对“销售额”数据求均值并打印；
（5）将处理后的数据框保存到Mysql数据库中，表名为“订单”（仅写出代码即可）。
'''

''' 
读取数据为orders的数据框
'''
file = '订单.xlsx'
orders = pd.DataFrame(pd.read_excel(file))
print('=====> orders数据框 <=====\n',orders)


'''
统计数据中缺失值大于3个字段的记录，并删除，打印出删除的条目
'''
print('\n=====> 统计数据中缺失值大于3个字段的记录，并删除，打印出删除的条目 <=====\n')
orders = orders.dropna(thresh=20)
print(orders)
print('\n',orders.isna().sum())

low_profit_id=[]
low_profit = []
m, n = orders.shape
print(orders.shape)
print(m,n)
print('每列缺省值个数\n')
a = orders.isnull().any().sum()
print(a)

for i in range(0, m):
    for j in range(0,n):
        if orders.iloc[i, j] == 'X':
            orders.iloc[i, j] = None


'''
统计“利润”小于零的所有“订单 ID 
'''
print('=====> 统计“利润”小于零的所有“订单 ID”； <=====')
a = orders[['订单 ID','利润']]
a = a.dropna()
n,m = a.shape

for i in range(0,n):
    if int(a.iloc[i,1]) < 0 :
        # print('利润为：',a1.iloc[i,1])
        # print('ID：',a1.iloc[i,0])
        low_profit_id.append(a.iloc[i, 0])
        low_profit.append(a.iloc[i, 1])
low_profit_dir = dict(map(lambda key,value:[key, value],low_profit_id,low_profit))
print(f'“利润”小于零的所有“订单 ID: \n{low_profit_dir}')



'''
对“销售额”数据求均值并打印
'''
print('=====> 对“销售额”数据求均值并打印 <=====')
sales_average = orders['销售额'].mean()
print('平均销售额为：\n',sales_average)




'''
将处理后的数据框保存到Mysql数据库中，表名为“订单”
'''
# db=pymysql.connect("localhost","root","12****adsd","订单",charset="utf8")
# cursor=db.cursor()
