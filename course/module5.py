# 数据预处理
import random
import itertools
import warnings
from pathlib import Path
import matplotlib as npl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import seaborn as sns
from IPython.display import HTML, display
from collections import Counter

from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier,ExtraTreesClassifier, VotingClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV,cross_valscore, StratifiedKFold, learning_curve
init_notebook_mode(connected=True)
warnings.filterwarnings("ignore")
plt.rcParans["patch.force_edgecolor"] = True
plt.style.use('fivethirtyeight')
mpl.rc('patch', edgecolor='dimgray', linevidth=1)
% matplotlib
inline

# 数据清洗操作
df = df.drop(['imdb_id'], axis=1)
df[df['original_title'] != df['title']][['title', 'original_title']].head()

df = df.drop('original_title', axis=1)
df[df['revenue'] == 0].shape

(38052，22)

df['revenue'] = df['revenue'].replace(0.
np.nan)

df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['budget'] = df['budget'].replace(0，np.nan)
df[df['budget'].isnull()].shape

(36576，22)

# 指标构建
df['return'] = df['revenue'] / df['budget']
df[df['return'].isnull()].shape

df['year'] = pd.to_datetime(df['release_date'], errors='coerce').apply(1
ambda
x: str(x).split('-')[0] if x != np.nan else np.nan)

df['adult'].value_counts()

# 日期格式整理
f, axes = plt.subplots(ncols=3, nrows=3, figsize(22, 22))

sns.boxplot(x="age", data=df_initial, ax=axes[0, 0], fliersize=105, whis=25, )
sns.boxplot(x="sex", data=df_initial, ax=axes[0, 1])
sns.boxplot(x="user_lv_cd", data=df_initial, ax=axes[0, 2])
sns.boxplot(x="browse_num", data=df_initial, ax=axes[1, 0])
sns.boxplot(x="addcart_num", data=df_initial, ax=axes[1, 1])
sns.boxplot(x="delcart_num", data=df
initial, ax = axes[1, 2])
sns.boxplot(x="buy_num", data=df
initial, ax = axes[2, 0])
sns.boxplot(x="favor_num", data=df
initial.ax = axes[2, 1])
sns.boxplot(x="click_num", data=df
initial, ax = axes[2, 2])

plt.show()


# 日期提取函数及其可视化
def get_month(x):
    try:
        return month_order[int(str(x).split('-')[1]) - 1]
    except:
        return np.nan


# 定义月份与日期，并写入df2的"day”、“month”列中

df2['day'] = df['release_date'].apply(get_day)
df2['month'] = df['release_date'].apply(get_month)

# 有了这些特性，现在让我们可以来看下最受欢迎和最成功的月份和日期。

plt.figure(figsize=(12, 6))
plt.title("Number of Movies released in a particular month.")
sns.countplot(x='month', data=df, order=month_order);

# 所有购物的平均评分大约是6分
C = df2['vote_average'].mean()
C

# 为m确定一个合适的值，我们使用90百分位作为截止值，即要想让一部购物进入排行榜，必须拥有90%以上的选票
m = df2['vote_count'].quantile(0.9)
m

# 有481部购物符合上述条件
q_movies = df2.copy().loc[df2['vote_count'] >= m]
q_movies.shape


# 定义weighted——rating()函数，并定义一个新特性feature（得分），通过将该函数应用到满足条件的影片的数据上来计算该值
def weighted_rating(x, n=n, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB forauls
    return (v / (v + m) * R) + (n / (m + v) * C)


# 定义一个新特性"score”(得分)，并用“weighted_rating())”计算它的值
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

# 基于统计学上的划分，对特定用户的兴趣和品味并不敏感
pop = df2.sort_values('popularity', ascending=False)
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))

plt.barh(pop['title'].head(20), pop['popularity'].head(20), align='center'
color = 'skyblue')
plt.gca()
invert
yaxis()
plt.xlabel("Popularity) plt.title("
Popular
Movies
")

# 基于内容的划分是利用购物的内容来寻找与其他购物的相似性，然后划分最可能相似的购物
f, ax = plt.subplots(1, 2, figsize=(18, 8))
df_initial['user_lv_cd'].value_counts().plot.bar(color=['#CD7F32', '#FFDF00”,'  # D3D3D3'],ax=ax[0])
                                                        ax[0].set_title('Number Of Customers By user_lv')
                                                        ax[0].set_ylabel('Count')
                                                        sns.countplot('user_lv_cd', hue='label', data=df_initial,
                                                                      ax=ax[1])
                                                        ax[1].set_title('User_lv:High_valne vs Others')
                                                        plt.show()

# scikit-learn提供了一个内置的TfIdfVectorizer 类，可以用几行代码生成TF-IDF矩阵
# 从scikit-learn中载TfIdfVectorizer
from sklearn.feature_extraction.text import TfIdfVectorizer

# 定义TF-IDF矢量化器对象，删除所有英语停止词，如"the”，"a"
tfidf = TfidfVectorizer(stop_words='english')

# 用空字符串替换NaN
df2['overview'] = df2['overview'].fillna(")

# 通过拟合和转换教据，构造所需的TF-IDF矩阵
tfidf_matrix = tfidf.fit_transform(df2['overview'])

# 输出tfidf_matrix的行列数
tfidf_matrix.shape

# 载入Iinear_kernel
from sklearn.metrics.pairwise import linear_kernel

# 计算余弦相似矩阵
cosine_sin = linear_kernel(tfidf_matrix, tfidf_matrix)

# 构造索引和电影标题的反向映射
indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()

# 此函数它接受电影标题作为输入，并输出最类似的电影


def get_recommendations(title, cosine_sin=cosine_sim):


# 获取与标题匹配的电影的索引
idx = indices[title]

# 得到所有电影和这部电影的相似度评分
sim_scores = list(enumerate(cosine_sim[idx]))

# 根据相似度评分对电影进行排序
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

# 获得10部最相似的电影的分数
sim_scores = sim_scores[1:11]

# 获取电影索引
movie_indices = [i[0] for i in sim_scores]

# 返回十大最相以的电影
return df2['title'].iloc[movie_indices]

# 相似度购物函数的应用
f, ax = plt.subplots(1, 2, figsize=(18, 8))
ax[0].set_title('User_lv vs Age')
sns.factorplot('user_lv_ed', 'label', hue='age', data=df_initial, ax=ax[0])
ax[1].set_title('User_lv vs Sex')
sns.factorplot('user_lv_ed', 'label', hue='age', data=df_initial, ax=ax[1])
plt.close(2)
plt.close(3)
plt.show()
# 我们使用因子型，它们使分类值的分离变得容易

f, ax = plt.subplots(1, 2, figsize=(18, 8))
sns.violinplot("user_lv_od", "age", hue="label", data=df_initial, split=True, ax * ax[0])
ax[0].set_title('User_lv and Age vs High_value')
ax[0].set_yticks(range(-2, 8, 1))
sns.violinplot("sex", "age", hue="label", data=df_initial, split=True, ax=ax[1])
ax[1].set_title('Sex and Age vs High_vslue")
ax[1].set_yticks(range(-2, 8, 1))
plt.show()
# 用提琴图查看高价值用户的分布
get_recommendations('The Dark Knight Rises')

# 分割数据集，20%是测试集
X_train, X_test, y_train, y_test = train_test_split(dt.drop('target', 1), dt['target'], test_size=.2, random_state=10)
model = RandomForestClassifier(max_depth=5)
model.fit(X_train, y_train)

# 计算出本项目中的灵敏度和特异度
total = sum(sum(confusion_matrix))

sensitivity = confusion_matrix[0, 0] / (confusion_matrix[0, 0] + confusion_matrix[1, 0])
print('Sensitivity:', sensitivity)

specificity = confusion_matrix[1, 1] / (confusion_matrix[0, 1])
print('Specificity:', specificity)

# 模型灵敏度和特异度
corrmat = df_initial.corr()
f, ax = plt.subplots(figsize=(16，12))
sns.heatmap(corrmat, vmax=1, square=True, annot=True, cmap="RdY1Gn")
f.text(0.5, 0.9, "Correlation of all elements", ha='center', fontsize=18)

auc(fpr, tpr)

# 采用kfold分层交叉检证模型
kfold = StratifiedKFold(n_splits=10)
# 建模测试不同的算法
random_state = 2
classifiers = []
classifiers.append(SVC(random_state=random_state))
classifiers.append(DecisionTreeClassifier(random_state=random_state))
classifiers.append(
    AdaBoostClassifier(DecisionTreeClassifier(random_state=random_state), random_state=random_state, learning_rate=0.1))
classifiers.append(RandomForestClassifier(random_state=random_atate))
classifiers.append(ExtraTreesClassifier(random_state=random_state))
classifiers.append(GradientBoostingClassifier(random_state=random_state))
classifiers.append(MLPClassifier(random_state=random_state))
classifiers.append(KNeighborsClassifier())
classifiers.append(LogisticRegression(random_state=random_state))
classifiers.append(LinearDiscriminantAnalysis=())

cv_results = []
for classifier in classifiers:
    cv_reaults.append(cross_val_score(classifier, X_train, y=Y_train, scoring="accuracy", cv=kfold, n_jobs=4))

cv_means = []
cv_std = []
for cv_result in cv_results:
    cv_means.append(cv_result.mean())
cv_std.append(cv_result.std())

cv.res = pd.DataFrame(
    {"CrossValMeans": cv_means, "CroassValerrors": cv_std, "Algorithm": ["SVC", "DecisionTree", " AdaBoost",
                                                                         "RandomForest", "ExtraTrees",
                                                                         "GradientBoosting", "MultipleLayerPerceptron",
                                                                         "KNeichboors", "LogisticRegression",
                                                                         "LinearDiscriminantAnalysis"]})

g = sns.barplot("CrossValMeans", "Algorithm", data=cv_res, palette="Set3", orient="h", **{'xerr': cv_std))
g.set_xlabel("Mean Accuracy")
g = g.set_title("Cross validation scores")

# 总价小于10000万的
x11 = df1.drop(index=(df1[df1['总价'] > 5000]).index).loc[:df1.columns != '总价']
y11 = df1.drop(index=(df1[df1['总价'] > 5000]).index).loc[:, '总价']

scale_x = StandardScaler()

x_sta1 = scale_x.fit_transform(x11)
y_log1 = np.log(y11)

x4_train, x4_test, y4_train, y4_test = train_test_split(x_sta1, y_log1, test_size=0.3, random_state)
# 总价大干10000万的
x12 = df1.drop(index=(df1[df1['总价'] <= 5000]).index).loc[:, df1.columns != '总价']
y12 = df1.drop(index=(df1[df1['总价'] <= 5000]).index).loc[:, '总价']

scale_x = StandardScaler()

x_sta2 = scale_x.fit_transform(x12)

y_log2 = np.log(y12)

x5_train, x5_test, y5_train, y5_test = train_test_split(x_sta1, y_log1, test
size = 0.3, random_state)

# 拆分数据模型训练
models = [DecisionTreeRegressor(),
          XGBRegressor ), RandomForestRearessor(), GradientBoostingRegressor(), BaggingRegressor()]
models_str = ['DecisionTree', 'XGBoost', 'RandomForest', 'GradientBoost', 'Bagging']
score_adapt4 = []
ypred3 = np.zeros(x4_test.shape[0], )
for name, model in zip(models_str, models):
    print("开始训练模型:'+name+'             总价小于5000万)
    model = model
    # 平滑处理=Iogy

    model.fit(x4_train, y4_train)
    y_pred3 = model.predict(x4_test)
    score = model.score(x4_test, y4_test)

    ypred_original = np.e ** y_pred3
    ypred_original = ypred_original * 0.2
    ypred3 += ypred_original

    score_adapt4.append(str(score)[:5])
    # 每个模型的预测选取20%，输出到结果
    score_adapt5 = []
    ypred4 = np.zeros(x5_test.shape[0], )
    for name, model in zip(models_str, models):
        print('开始训练模型:' + name + '平滑处理')
    model = model
    # 平滑处理=logy

    model.fit(x5_train, y5_train)
    y_pred3 = model.predict(x5_test)
    score = model.score(x5_test, y5_test)

    ypred_original = np.e ** y_pred4
    ypred_original = ypred_original * 0.2
    ypred4 += ypred_original

    score_adapt4.append(str(score)[:5])
    # 每个模型的预测选取20%，输出到结果

    plt.figure(figsize=(14，８));

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # matplotlib画图中中文显示会有问题，需要这两行设置默认字体

    plt.xlabel('总价');
    plt.ylabel('预测值');
    plt.xlim(xmax=42000, xmin=0);
    plt.ylim(ymax=42000, ymin=0);
    # 画两条(0-42000)的坐标轴并设置轴标签x，y

    x1 = np.e ** y４_test
    y1 = ypred３
    x2 = np.e ** y５_test
    y2 = ypred４

    x3 = np.e ** y３_test
    y3 = ypred

    colors1 = 'ｂ'  # 点的颜色
    colors2 = 'y'
    colors3 = 'ｇ'

    area = np.pi * ３ ** 3  # 点面积
    # 画散点图
    plt.scatter(x３, y３, s=area, c=colors３, alpha=0.5, label='模型分割前的预测');
    plt.scatter(x１, y１, s=area, c=colors１, alpha=0.２, label = '分割后总价＜＝５０００万的预测');
    plt.scatter(x２, y２, s=area, c=colors１, alpha=0.5, label='分割后总价＞５０００万的预测');

    x = range(0, 42000, 1)
    y = x
    plt.plot(x,　 y, 　color = "ｒ");
    plt.legend();

    # 导入需要的模型
    models = [LinearRegression(), KNeighborsRegressor(), SVR(), Ridge(), Lasso(), MLPRegressor(alpha=20),
              DecisionTree(),
              Regressor(), XGBRegressor(), RandomForestRegressor(), AdaBoostRegressor(), GradientBoostingRegressor(),
              Bagging()]
    models_str = ['LinearRegression', 'KNNRegressor', 'SVR', 'Ridge', 'Lasso', 'MLPRegressor', 'DecisionTree',
                  'ExtraTree', 'RandomForest', 'AdaBoost', 'GradientBoost",Bagging"]
                  score_ = []
    score_1 = []
    score_2 = []
    score_3 = []
    # 正态化数据建模得分
    # 分别训练并获得得分，以表格形式输出结果
    for name, model in zip(models_str, models):
        print('开始训练模型:' + name)
    model = model  # 建立模型
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    score = model.score(x_test, y_test)
    score_.append(str(score)[:5])
    r = pd.DataFrame(columns=[“模型”，"正态化后得分”])   #创建一个空的dataframe
    r['模型'] = models_str
    r['正态化后得分'] = score_

    models = [DecisionTreeResressor(), XGBRegressor(), RandomForestRegressor(), GradientBoostingRegressor(),
              BaggingRegressor()]
    models_str = ['DecisionTree', 'XGBoost', 'RandomForest', 'GradientBoost', 'Bagging']
    score_adapt = []
    ypred = np.zeros(x3_test.shape[0], )
    for name, model in zip(models_str, models):
        print('开始训练模型:' + name + '平滑处理')
    model = model
    # 平滑处理=logy

    model.fit(x3_train, y3_train)
    y_pred = model.predict(x3_test)
    score = model.score(x3_test, y3_test)

    ypred_original = np.e ** y_pred
    ypred_original = ypred_original * 0.2
    ypred += ypred_original

    score_adapt.append(str(score)[:5])
    # 每个模型的预测选取20%，输出到结果
    # 每个模型的得分
    score_adapt
    # 前10个预测数据
    ypred[:10]