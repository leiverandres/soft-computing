from sklearn import tree
# first classifier using decision tree, for apples and oranges
# features[x, y]-- x: weigth y: texture
# labels -- 0: orange 1: apple
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = ["apple", "apple", "orange", "orange"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[150, 0]])
