# coding=utf-8

import pandas as pd

data = pd.read_excel(r'D:\github\practise\student\meal_order_detail.xlsx')
df = pd.DataFrame(data)
print(df.columns.values)
