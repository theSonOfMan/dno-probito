import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def features(df_titanic):
	clf = DecisionTreeClassifier(random_state=241)

	x = df_titanic[['Sex', 'Age', 'Pclass', 'Fare']].values
	y = df_titanic['Survived'].values

	clf.fit(x, y)
	importances = clf.feature_importances_

	d = {
		importances[0]: 'Sex',
		importances[1]: 'Age',
		importances[2]: 'Pclass',
		importances[3]: 'Fare',
	}

	importances = sorted(importances)[2:]
	print(d[importances[1]] + ": " + str(importances[1]))
	print(d[importances[0]] + ": " + str(importances[0]))
	

def accuracy(df_titanic):
	clf = DecisionTreeClassifier(random_state=241)

	simple_train = df_titanic[columns][:535]
	simple_test = df_titanic[columns][535:]

	x_train = simple_train[['Sex', 'Age', 'Pclass', 'Fare']].values
	x_test = simple_test[['Sex', 'Age', 'Pclass', 'Fare']].values
	y_train = simple_train['Survived'].values
	y_test = simple_test['Survived'].values

	clf.fit(x_train, y_train)
	print("Accuracy: " + str(clf.score(x_test, y_test)))

df_titanic = pd.read_csv('titanic.csv')

columns = ['Sex', 'Age', 'Pclass', 'Fare', 'Survived']
df_titanic = df_titanic[columns].dropna()
df_titanic.Sex = df_titanic.Sex.apply(lambda x: 1 if x.strip() == 'male' else 0)

features(df_titanic)
accuracy(df_titanic)
