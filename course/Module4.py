import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#正常显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif']= ['SimHei']
from IPython.display import display
import tensorflow as tf
from pandas import Series,DataFrame,concat
#正常显示符号
from matplotlib import rcParams
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import BaggingRegressor
from pylab import mpl
import seaborn as sns
from scipy.stats import norm
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline

df= pd.read_csv('result.csv')
# (三)	缺失数据处理
display(df.info())

#缺失数据统计
total = df.isnull().sum().sort_values(ascending=False)
percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total,percent],axis=1,keys=['Total','Percent'])
print(missing_data.head(50))

#看看这些缺失值的特征总共包含哪些元素
a=['elevator','model_structure','building_type','ladder_rate',]
for k in a:
   display(df[k].value_counts().head())

df=df.fillna(value='暂无数据')
df.isnull().sum().max()  #检查一下还剩多少缺失值

#提取电梯数
df['梯数']=df['ladder_rate'].apply(lambda  x:x[:(x.find('梯'))])
#提取用户
df['户数']=df['ladder_rate'].apply(lambda  x:x[(x.find('梯')+1):(x.find('户'))])
#定义中文数字转换阿拉伯数字的函数
CN_NUM = {
      '〇' : 0, '一' : 1, '二' : 2, '三' : 3, '四' : 4, '五' : 5, '六' : 6, '七' : 7, '八' : 8, '九' : 9, '零' : 0,
      '壹' : 1, '贰' : 2, '叁' : 3, '肆' : 4, '伍' : 5, '陆' : 6, '柒' : 7, '捌' : 8, '玖' : 9, '貮' : 2, '两' : 2,
}

# 提取数值和类型关键信息
def compute_content_cost(a_C, a_G):
    # 获取a_G的维度信息
    M, n_H, n_W, n_C = a_G.get_shape().as_list()

    # 对a_C与a_G从3维降到2维
    a_C_unrolled = tf.transpose(tf.reshape(a_C, [n_H * n_W, n_C]))
    a_G_unrolled = tf.transpose(tf.reshape(a_G, [n_H * n_W, n_C]))
    # 计算内容代价
    # J_content = (1/(4 * n_H * n_W * n_C)) * tf.reduce_sum(tf.square(tf.subtract(a_C_unrolled, a_G_unrolled)))
    J_content = (1 / (4 * n_H * n_W * n_C)) * tf.reduce_sum(tf.square(tf.subtract(a_C_unrolled, a_G_unrolled)))
    return J_content

df = df.convent_objects(convert_numeric = True)
df.info()
