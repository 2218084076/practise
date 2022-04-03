import eli5
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None #隐藏 pandas的警示
np.random.seed(123) #固定随机数 保证实验可以重复

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz
# import eli5 # 用于排列重要性
from eli5.sklearn import PermutationImportance
# import shap #用于显示SHAP值
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_curve,auc
# from PDPbox import pdp,inof_plots

dt = pd.read_csv(r"D:\Terry\university学校\课程\大数据综合开发实训\heart.csv")
print('=====> dt.head(5) 原始数据： <=====\n',dt.head(5))

dt.columns = [
    'age',
    'sex',
    'chest_pain_type',
    'resting_blood_pressure',
    'cholesterol',
    'fasting_blood_sugar',
    'rest_ecg',
    'max_heart_rate_achieved',
    'exercise_induced_angina',
    'st_depression',
    'st_slope',
    'num_major_vessels',
    'thalassemia',
    'target'
]
print('====> dt.dtypes 数据类型（修改前） <====\n',dt.dtypes) # 数据类型

dt['sex'][dt['sex'] == 0] = 'female'
dt['sex'][dt['sex'] == 1] = 'male'

dt['chest_pain_type'][dt['chest_pain_type'] == 1] = 'typical angina'
dt['chest_pain_type'][dt['chest_pain_type'] == 2] = 'atypical angina'
dt['chest_pain_type'][dt['chest_pain_type'] == 3] = 'non-anginal angina'
dt['chest_pain_type'][dt['chest_pain_type'] == 4] = 'asymptomatic'

# 将字符数替换成文字
dt['fasting_blood_sugar'][dt['fasting_blood_sugar'] == 0] = 'lower than 120mg/ml'
dt['fasting_blood_sugar'][dt['fasting_blood_sugar'] == 1] = 'greater than 120mg/ml'

dt['rest_ecg'][dt['rest_ecg'] == 0] = 'normal'
dt['rest_ecg'][dt['rest_ecg'] == 1] = 'ST-T wave abnormaality'
dt['rest_ecg'][dt['rest_ecg'] == 2] = 'left ventricular hypertrophy'

dt['exercise_induced_angina'][dt['exercise_induced_angina'] == 0] = 'no'
dt['exercise_induced_angina'][dt['exercise_induced_angina'] == 1] = 'yes'

dt['st_slope'][dt['st_slope'] == 1] = 'upsloping'
dt['st_slope'][dt['st_slope'] == 2] = 'flat'
dt['st_slope'][dt['st_slope'] == 3] = 'downsloping'

dt['thalassemia'][dt['thalassemia'] == 1] = 'normal'
dt['thalassemia'][dt['thalassemia'] == 2] = 'fixed defect'
dt['thalassemia'][dt['thalassemia'] == 3] = 'reversable defect'

print('====> dt.dtypes 数据类型修改 <====\n',dt.dtypes) # 数据类型

dt['sex'] = dt['sex'].astype('object')
dt['chest_pain_type'] = dt['chest_pain_type'].astype('object')
dt['fasting_blood_sugar'] = dt['fasting_blood_sugar'].astype('object')
dt['rest_ecg'] = dt['rest_ecg'].astype('object')
dt['exercise_induced_angina'] = dt['exercise_induced_angina'].astype('object')
dt['st_slope'] = dt['st_slope'].astype('object')
dt['thalassemia'] = dt['thalassemia'].astype('object')
print('=====> astype 数据类型修改 <=====\n',dt.dtypes)

# 数据处理 引入one-hot编码

dt = pd.get_dummies(dt,drop_first=True)
print('====> pd.get_dummies(dt,drop_first=True)引入one-hot编码 <====\n',dt.head(5))

# 分割数据集 20%为测试集
# print('=====> 将数据集划分为 <=====')
X_train,X_test,y_train,y_test = train_test_split(dt.drop('target',1),dt['target'],test_size=.2,random_state=10)
# print(f'X_train{X_train},X_test{X_test}')
# print(f'y_train{y_train},y_test{y_test}')

model = RandomForestClassifier(max_depth=5)
model.fit(X_train,y_train)

estimator = model.estimators_[1]
feature_names = [i for i in X_train.columns]

y_train_str = y_train.astype('str')
y_train_str[y_train_str == '0'] = 'no disease'
y_train_str[y_train_str == '1'] = 'disease'
y_train_str = y_train_str.values

export_graphviz(estimator,out_file='tree.dot',
                feature_names=feature_names,
                class_names=y_train_str,
                rounded=True,
                proportion=True,
                label='root',
                precision=2,
                filled=True)

from subprocess import call
call(['dot','-Tpng','tree.dot','-0','tree.png','-Gdpi=600'])

from IPython.display import Image
Image(filename = 'tree.png')

y_predict = model.predict(X_test)
y_pred_quant = model.predict_proba(X_test)[:,1]
y_pred_bin = model.predict(X_test)

confusion_matrix = confusion_matrix(y_test,y_pred_bin)
print(confusion_matrix)

#灵敏度  特异度
total = sum(sum(confusion_matrix))
sensitivty = confusion_matrix[0,0]/(confusion_matrix[0,0]+confusion_matrix[1,0])
print('Sensitivty:',sensitivty)
specificity = confusion_matrix[1,1]/(confusion_matrix[1,1]+confusion_matrix[0,1])
print('Specificity:',specificity)

fpr,tpr,thresholds = roc_curve(y_test,y_pred_quant)
fig,ax = plt.subplots()
ax.plot(fpr,tpr)
ax.plot([0,1],[0,1],transform=ax.transAxes,ls="==",c=".3")
