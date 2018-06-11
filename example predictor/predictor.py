from sklearn import tree

#[height,weight,shoe size]
X = [[181,80,44], [117,70,43],[160,60,38], 
	[154,54,37], [166,65,40], [190,90,47], [175,64,39]]
Y = ['male', 'female', 'male', 'male', 'female', 'female', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)
prediction = clf.predict([[190,74,53]])
print(prediction)
