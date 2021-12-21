import pandas as pd
from sklearn.tree import DecisionTreeClassifier

iris_train = pd.read_csv('iris_train.csv')
iris_test = pd.read_csv('iris_test.csv')

model = DecisionTreeClassifier()
model.fit(iris_train.iloc[:, :-1], iris_train.iloc[:, -1])
predicted = model.predict(iris_test.iloc[:, :-1])

iris_test['label'] = predicted
iris_test.to_csv('iris_test_predicted.csv', index=None)

print(pd.read_csv('iris_test_predicted.csv').head(20))