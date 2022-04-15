import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=['SimHei']
plt.rcParams["axes.unicode_minus"]=False

apple = pd.read_csv("D:/Desktop/meal_order_info.csv")
df = pd.DataFrame(apple)
df['lock_time'] = pd.to_datetime(df['lock_time'])
print(df.dtypes)
print(df.head(5))
df.sort_values(by='lock_time',inplace=True)
print(df['lock_time'].head(16))

plt.figure(figsize=(10, 10))
plt.scatter(df['lock_time'],df['accounts_payable'])

plt.figure(figsize=(20,5),dpi=90)
 
plt.plot(df['lock_time'],df['accounts_payable'])
plt.show()