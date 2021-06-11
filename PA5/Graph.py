import numpy as np
import pandas as pd
import sys
import seaborn as sns
from sklearn.model_selection import KFold
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import networkx as nx

def build_graph(tree, G, parent=None, value=None):
    '''
    tree is the decision tree format used by Joel Grus
    in Data Science from Scratch:
    leaf node: True/False
    decision node: tuple of (attribute, subtree_dict)
    '''
    if tree in [True, False]:
        G.add_node(tree) # add leaf node
        G.add_edge(parent, tree, label=value)
    else:
        attribute, subtree_dict = tree
        attribute = str(attribute)
        G.add_node(attribute) # add attribute node

        if parent is not None:
            G.add_edge(parent, attribute, label=value)

        for attribute_value, subtree in subtree_dict.items():
            attribute_value = str(attribute_value)
            build_graph(subtree, G, attribute, attribute_value)

# tree built previously for candidate hire classification problem
tree = ['level', \
        {None: True, \
         'Senior': ('tweets', \
                    {'no': False, None: False, 'yes': True}), \
         'Junior': ('phd', \
                    {'no': True, None: True, 'yes': False}), \
         'Mid': True}]

G = nx.DiGraph()
build_graph(tree, G)
pos = nx.spring_layout(G)
# draw nodes and edges
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)

# add node and edge labels
labels = {node:str(node) for i, node in enumerate(G.nodes())}
elabels = {edge:G[edge[0]][edge[1]]["label"] for i, edge in enumerate(G.edges())}
nx.draw_networkx_labels(G, pos, labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=elabels)
plt.axis('off')

import matplotlib.pyplot as plt
import networkx as nx

def get_number():
    '''
    
    '''
    num = 0
    while True:
        yield num
        num += 1

def build_graph(tree, G, parent=None, value=None, gen=get_number()):
    '''
    
    '''
    if tree in [True, False]:
        unique_label = str(tree) + str(next(gen))
        G.add_node(unique_label) # add leaf node
        G.add_edge(parent, unique_label, label=value)
    else:
        attribute, subtree_dict = tree
        attribute = str(attribute)
        G.add_node(attribute) # add attribute node

        if parent is not None:
            G.add_edge(parent, attribute, label=value)

        for attribute_value, subtree in subtree_dict.items():
            attribute_value = str(attribute_value)
            build_graph(subtree, G, attribute, attribute_value, gen)

tree = ['level', \
        {None: True, \
         'Senior': ('tweets', \
                    {'no': False, None: False, 'yes': True}), \
         'Junior': ('phd', \
                    {'no': True, None: True, 'yes': False}), \
         'Mid': True}]

G = nx.DiGraph()
build_graph(tree, G)
pos = nx.spring_layout(G)
# draw nodes and edges
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)

# add node and edge labels
labels = {node:str(node) for i, node in enumerate(G.nodes())}
elabels = {edge:G[edge[0]][edge[1]]["label"] for i, edge in enumerate(G.edges())}
nx.draw_networkx_labels(G, pos, labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=elabels)
plt.axis('off')

G = nx.DiGraph()
build_graph(tree, G)
p=nx.drawing.nx_pydot.to_pydot(G) # will need to install pydot and pydotplus
p.write_png(r'figures\example.png')
from IPython.display import Image
Image(r"figures\example.png")