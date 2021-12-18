import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from IPython.display import display
import datetime

df1 = pd.read_csv('tmdb_5000_credits.csv')
df2 = pd.read_csv('tmdb_5000_movies.csv')
display(df1.head())
df1.head()

df1.columns = ['id','title','cast','crew']
df= df2.merge(df1,on='id',how = "right")

# df = df.drop(['imdb_id'],axis=1)
# df[df['original_title'] != df['title']][['title','original_title']].head()

df = df.drop('original_title',axis=1)
df[df['revenue'] == 0].shape


df['revenue'] = df['revenue'].replace(0,np.nan)
print(df.head())

df['budget'] = pd.to_numeric(df['budget'],errors='coerce')
df['budget'] = df['budget'].replace(0,np.nan)
df[df['budget'].isnull()].shape

df['return'] = df['revenue'] / df['budget']
df[df['return'].isnull()].shape

df['year'] = pd.to_datetime(df['release_date'],errors='coerce')
df['budget'] = df['budget'].replace(0,np.nan)
df[df['budget'].isnull()].shape

df['return'] = df['revenue'] / df['budget']
df[df['return'].isnull()].shape

df['year'] = pd.to_datetime(df['release_date'],errors='coerce').apply(lambda x:str(x).split('-')[0] if x != np.nan else np.nan)
df['adult'].value_counts()

month_order = ['Jan','Feb','Mar ','Apr ','May','Jun','Ju1','Aug','Sep','Oct','Nov ', 'Dec']
day_order = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

def get_month(x):
    try:
        return month_order[int(str(x).split('-')[1])-1]
    except:
        return np.nan

def get_day(x):
    try:
        year,month,day = (int(i) for i in x.aplit('-'))
        answer = datetime.date(year,month,day).weekday()
        return day_order[answer]
    except:
        return np.nan

df2['day'] = df['release_date'].apply(get_day)
df2['month'] = df['release_date'].apply(get_month)

plt.figure(figsize=(12,6))
plt.title('Number of Movies released in a particular month')
sns.countplot(x='month',data=df,order = month_order);
