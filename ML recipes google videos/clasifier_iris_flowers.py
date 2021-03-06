# Tutorial goals:
# 1- Import database
# 2- Train a Classifier
# 3- Predict label for new flower
# 4- Visualize the tree
 
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

iris = load_iris()
# print iris.feature_names
# print iris.target_names
# print iris.data[0]
# print iris.target[0]

# remove one from each kind
test_idx = [0, 50, 100]

# train data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print "Target: ", test_target
print "Result: ", clf.predict(test_data)

# viz code
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         impurity=False)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
print type(graph[0])
graph[0].write_pdf("iris.pdf")

