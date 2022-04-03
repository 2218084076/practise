import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from IPython.display import display
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']

df = pd.read_csv(r"D:\Terry\university学校\课程\大数据综合开发实训-杨彪老师\大数据综合开发实训\原始数据\心脏病案例\heart.csv")
print(df.head(3).T)

display(df.info())
total = df.isnull().sum().sort_values(ascending=False)
#统计缺失数据
print(total)
percrnt = (df.isnull().sum()/df.isnull.count()).sort_values(ascending=False)
missing_data = pd.concat([total,percrnt],axis=1,keys=['Total','Percent'])
missing_data.head(50)
print(percrnt)