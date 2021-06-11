import pydotplus
from sklearn import tree

X =[[0.0, 0.1, 0.2, 0.0, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
 [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.0, 0.1],
 [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
 [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
 [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0],
 [0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]]

Y = ['g0', 'g1', 'g2', 'g3', 'g4', 'g5']

data_feature_names = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

# Visualize data
dot_data = tree.export_graphviz(clf,
                                feature_names=data_feature_names,
                                out_file=None,
                                filled=True,
                                rounded=True)

graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('tree.png')