"""
Programmer: Samantha Gregoryk
Class: CptS 215-01, Fall 2019
Micro Assignment #6
11/14/19

Description: Referencing the K-means algorithm in PA2, 
we are using hierarchial clustering items that are very
similar (lower down the tree) or less similar (higher up the tree). 
"""
import numpy as np
import pandas as pd
import math

class Pair:
    '''
    Keeps track of distances between a 
    pair of clusters.
    '''
    def __init__(self, data, k):
        '''
        '''
        self.data = data
        self.k = k
        self.clusters = []
        
    def __lt__(self, other):
        '''
         Compares Pair objects for heap
         ordering purposes.
        '''
        ds = self.data < other.data
        k = self.num_k < other.num_k
        return ds, k
        
    def euclidean_distance(self, d1, d2):
        '''
        Distance between two points.
        '''  
        result = 0
        
        for i in range(len(d1)):
            f1 = d1[i] 
            f2 = d2[i]   
            tmp = f1 - f2
            result += pow(tmp, 2)
            
        result = math.sqrt(result)
        
        return result
    
    def closest_pair(self, data):
        '''
        Using the length of two different 
        datasets, we apply euclidean 
        distance. 
        '''
        for i in range(len(data) - 1): 
            for j in range(i + 1, len(data)):    
                dist = self.euclidean_distance(data[i], data[j])
                
            return dist

    def weighted_centroids(self, data, clusters, k):
        '''
        Weighting the average of the centroids
        of the two clusters by the number of 
        leaves.
        '''
        results=[]
        for i in range(k):
            results.append(np.average(data[clusters == i], 
                                      weights = np.squeeze(np.array(data[clusters == i][:,0:1])),
                                      axis = 0))
        return results
    
class Node:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node
    
    def is_empty(self):
        return self.root == None
    
    def pre_order_traversal(self):
        if not self.is_empty():
            self.pre_order_helper(self.root)
            print()
        else:
            print("Empty tree")
            
    def pre_order_helper(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order_helper(node.left_child)
            self.pre_order_helper(node.right_child)
            
    def post_order_traversal(self):

        if not self.is_empty():
            self.post_order_helper(self.root)
            print()
        else:
            print("Empty tree")
            
    def post_order_helper(self, node):
        if node is not None:
            self.post_order_helper(node.left_child)
            self.post_order_helper(node.right_child)
            print(node.data, end=" ")
            
    def level_order_traversal(self):
        if not self.is_empty():
            queue = [self.root]
            self.level_order_helper(self.root, queue)
            for node in queue:
                print(node.data, end=" ")
            print()
        else:
            print("Empty tree")
            
    def level_order_helper(self, node, queue):
        if node is not None:
            if node.left_child is not None:
                queue.append(node.left_child)
            if node.right_child is not None:
                queue.append(node.right_child)
            self.level_order_helper(node.left_child, queue)
            self.level_order_helper(node.right_child, queue)
            
    def in_order_traversal(self):
        if not self.is_empty():
            self.in_order_helper(self.root)
            print()
        else:
            print("Empty tree")
            
    def in_order_helper(self, node):
        if node is not None:
            self.in_order_helper(node.left_child)
            print(node.data, end=" ")
            self.in_order_helper(node.right_child)
            

class HierarchicalCluster(BinaryTree):
    '''
    Inheriting from the Binary Tree class, 
    this is a binary tree representing the 
    hierarchical clusters. 
    '''
    def hierarchal_cluster(self):
        '''
        This tree builds from the bottom-up. 
        It finds the closest pair of clusters
        and makes them children of new clusters.
        Then, it repeats until it is left wit
        h just a single object. 
        '''
        pass

class BinaryMinHeap:
    '''
    Priority queue used to find
    the closest pair of clusters.
    '''
    def __init__(self):
        '''
        heap_list[0] = 0 is a dummy value (not used)
        '''
        self.heap_list = [0]
        self.size = 0
        
    def __str__(self):
        '''
        
        '''
        return str(self.heap_list)
    
    def __len__(self):
        '''
        
        '''
        return self.size
    
    def __contains__(self, item):
        '''
        
        '''
        return item in self.heap_list
    
    def is_empty(self):
        '''
        compare the size attribute to 0
        '''
        return self.size == 0
    
    def find_min(self):
        '''
        the smallest item is at the root node (index 1)
        '''
        if self.size > 0:
            min_val = self.heap_list[1]
            return min_val
        return None
        
    def insert(self, item):
        '''
        append the item to the end of the list (maintains complete tree property)
        violates the heap order property
        call percolate up to move the new item up to restore the heap order property
        '''
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)
        
    def del_min(self):
        '''
        min item in the tree is at the root
        replace the root with the last item in the list (maintains complete tree property)
        violates the heap order property
        call percolate down to move the new root down to restore the heap property
        '''
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size = self.size - 1
        self.heap_list.pop()
        self.percolate_down(1)
        return min_val

    def min_child(self, index):
        '''
        return the index of the smallest child
        if there is no right child, return the left child
        if there are two children, return the smallest of the two
        '''
        if index * 2 + 1 > self.size:
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1
            
    def build_heap(self, alist):
        '''
        build a heap from a list of keys to establish complete tree property
        starting with the first non leaf node 
        percolate each node down to establish heap order property
        '''
        index = len(alist) // 2 # any nodes past the half way point are leaves
        self.size = len(alist)
        self.heap_list = [0] + alist[:]
        while (index > 0):
            self.percolate_down(index)
            index -= 1
        
    def percolate_up(self, index):
        '''
        compare the item at index with its parent
        if the item is less than its parent, swap!
        continue comparing until we hit the top of tree
        (can stop once an item is swapped into a position where it is greater than its parent)
        '''
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                temp = self.heap_list[index // 2]
                self.heap_list[index // 2] = self.heap_list[index]
                self.heap_list[index] = temp
            index //= 2
            
    def percolate_down(self, index):
        '''
        compare the item at index with its smallest child
        if the item is greater than its smallest child, swap!
        continue continue while there are children to compare with
        (can stop once an item is swapped into a position where it is less than both children)
        '''
        while (index * 2) <= self.size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = temp
            index = mc
              
def read_data(file):
    df = pd.read_csv(file)
    df = np.array(df)
    return df
                
f = read_data('simple.csv')

h = BinaryMinHeap()
h.insert(f)
print(h)
print(h.is_empty())
h.find_min()
print(h)
print(h.is_empty())
print(len(h))


# Initialize the priority queue (BinaryMinHeap) with all pairs (Pair) of trees
# Then when a new cluster is formed, create new pairs between it and the remaining
# clusters (not its children!) and add them to the queue









