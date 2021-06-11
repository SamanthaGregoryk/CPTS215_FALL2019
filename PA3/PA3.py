"""
Programmer: Samantha Gregoryk
Class: CptS 215-01, Fall 2019
Micro Assignment #3
10/8/2019

Description: In this program, we are determinging
 how much work is put into sorting routines. 
 Specficially, size and order of data. Once
 we figure out different sorting routintes 
 from the CircularDoublyLinkedList class, we
 will record data from each routine in a CSV
 file. We will also plot the running time and
 total operation count and store it in PNG file. 
 
 Note: comments for counting sorting algorithms 
 are all listed below main at the very bottom of 
 this assignment.

"""
import matplotlib.pyplot as plt
from copy import deepcopy
import random
import pandas as pd
import numpy as np
import timeit

class Node:
    '''
    Node Class to implement a link list in the
    Circular Double Linked List class.
    '''
    def __init__(self, data):
      '''
      When a node is called, it is able to move
      through the linked list. Each node contains
      an integer and can move either forward or 
      behind. 
      '''
      self.data = data
      self.next = None
      self.prev = None
       
class CircularDoublyLinkedList:
    '''
    Class that manipulates a doubly linked list. 
    This class includes adding nodes, sorting nodes
    with different sorting routines, and printing 
    nodes in some type of order. 
    '''
    def __init__(self):
        '''
        When the linked list is called, it can call
        the head of the list or the size of the list.
        '''
        self.head = None
        self.size = 0
            
    def add(self, data): 
        '''
        Method to add a node to the linked list.
        '''
        new_node = Node(data) 
        new_node.next = self.head 
   
        if (self.head != None): 
            self.head.prev = new_node 
   
        self.head = new_node
        
    
    def insertion_sort(self, temp):
        '''
        Sorting routine #1 that sorts the unorderd
        linked list by comparing each node sequentially
        and arranged at the same time. Order of the list
        will be printed in ascending order.
        '''
        x = temp
        temp = temp.next
        x.next = None
        
        while (temp != None):
            current = temp
            temp = temp.next
            if (current.data < x.data):
                current.next = x
                x = current
            else: 
                search = x
                while (search.next != None and current.data > search.next.data):
                    search = search.next
                    
                current.next = search.next
                search.next = current   
        return x
    
    def bubble_sort(self, swap): 
        '''
        Sorting routine #2 that sorts the linked list by
        comparing nodes next to each other. Once compared,
        it swaps through the list until it is in ascending
        order. 
        '''
        swap = self.head
        left = swap.next
        right = left.next
        
        for i in range(0, self.size):
            for j in range(i):
                if(left.data > right.data):
                    temp = swap
                    left = right
                    right = temp
    
    
    def merge_sort(self, temp):
        '''
        Sorting routine #3 that splits the linked list into 
        two seperate linked lists until they are compared 
        proporly. Then uses recursion to merge the multiple
        linked lists back into one linked list.
        '''
        if (temp == None): 
            return temp
        if (temp.next == None):
            return temp
         
        right = self.split_merge(temp)
        temp = self.merge_sort(temp)
        right = self.merge_sort(right)
 
        return self.merge(temp, right)
    
    def split_merge(self, temp):
        '''
        Second part of merge_sort that just splits all linked lists.
        '''
        left = right = temp
        
        while(True):
            if (left.next == None):
                break
            if (left.next.next == None):
                break
            
            left = left.next.next
            right = right.next
             
        temp = right.next
        right.next = None
        return temp
        
    def merge(self, L1, L2):
        '''
        Third part of merge_sort method that compares two linked lists
        to each other and then merges those to make the last linked 
        list.
        '''
        if (L1 == None):
            return L2
        if (L2 == None):
            return L1
     
        if (L1.data < L2.data):
            L1.next = self.merge(L1.next, L2)
            L1.next.prev = L1
            L1.prev = None  
            return L1
        
        else:
            L2.next = self.merge(L1, L2.next)
            L2.next.prev = L2
            L2.prev = None
            return L2
    
    def print_LL(self, node):
        '''
        Used to print sorting routines in ascending 
        order always.
        '''
        temp = node
        while (node != None):
           print(node.data)
           temp = node
           node  = node.next 
     
    def reverse_LL(self):
        '''
        Used to manipulate the ascending order linked 
        list and creates a descending list.
        '''
        if self.head == None or self.head.next == None:
            return

        prev = None
        cur = self.head

        while cur:
            next_element = cur.next
            cur.next = prev
            prev = cur
            cur = next_element

        self.head = prev
    
        
def insertion_sort_function(array):
    '''
    From week week 5 lecture 3.
    '''
    for i in range(1, len(array)):
        temp = array[i]
        for j in range(i - 1, -1, -1):
            if temp < array[j]:      
                array[j + 1] = array[j]
                array[j] = temp
                temp = array[j]
                
def bubble_sort_function(array):
    '''
    From week 5 lecture 3.
    '''
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if array[j + 1] < array[j]:
                temp = array[j]
                array[j + 1] = array[j]
                array[j] = temp
                
def merge_sort_function(array):
    '''
    From week 6 lecture 1.
    '''
    if len(array) <= 1:
        return
    mid = len(array) // 2
    # since array is a ndarray, need to do a copy
    # otherwise get a view
    left = array[:mid].copy()
    right = array[mid:].copy()
    merge_sort_function(left)
    merge_sort_function(right)
    merge_function(array, left, right)
    
def merge_function(array, lefthalf, righthalf):
    '''
    From week 6 lecture 1.
    '''
    i=0; j=0; k=0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            array[k]=lefthalf[i]
            i=i+1
        else:
            array[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        array[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        array[k]=righthalf[j]
        j=j+1
        k=k+1   
               
     
def main():
    '''
    Main() will include the orders of each sorting routines 
    (ascending, descending, random). Then the dataframe is created
    with all the work each sorting routines creates. Then, six plots
    of running time (3) and total operation count (3) for each 
    sorting routine order is created. 
    '''
    C = CircularDoublyLinkedList()  
     
    C.add(5000) 
    C.add(10000)
    C.add(1000)
    C.add(500)
    
    print('INSERTION SORT') 
    C1 = deepcopy(C)    
   
    #INSERTION SORT IN ASCENDING ORDER
    C1.head = C1.insertion_sort(C1.head)    
    C1.print_LL(C1.head)
    print('\n')
    
    #timing for ascending order
    
    C2 = deepcopy(C)

    #INSERTION SORT IN DESCENDING ORDER
    C2.reverse_LL()
    C2.print_LL(C2.head)
    print('\n')
    
    #timing for descending order
    
    C3 = deepcopy(C)

    #INSERTION SORT IN RANDOM ORDER
    random.seed(C3)
    C3.print_LL(C3.head)
    print('\n')
    
    #timing for random order
    
    is_res = open(r'insertion_sort_results.csv', 'w')   
   
    data1 = {'List Configuration':['Sorted N = 500', 'Sorted N = 1000', 'Sorted N = 5000', 'Sorted N = 10000', 
                                   'Descending Sorted N = 500 ', 'Descending Sorted N = 1000', 'Descending Sorted N = 5000', 'Descending Sorted N = 10000 ', 
                                   'Random N = 500 ', 'Random N = 1000 ', 'Random N = 5000 ', 'Random N = 10000 '],
             'Seconds':[1,2,3,4,5,6,7,8,9,10,11,12], 
             '# Data' :[3, 3, 2, 2, 1, 1, 0, 0, 3, 3, 2, 2],
             '# Loop' :[1, 2, 1, 1, 2, 2, 0, 0, 1, 2, 1, 1], 
             '# Data Assignments' :[2, 3, 3, 3, 3, 3, 0, 0, 2, 3, 3, 3],
             '# Loop Assignments' :[1, 1, 2, 2, 2, 2, 0, 0, 1, 1, 2, 2],
             '# Other' :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             'Total' :[7, 9, 8, 9, 8, 8, 0, 0, 7, 9, 8, 9]}

    df1 = pd.DataFrame(data1)
    df1.to_csv(is_res, index = False) #creates csv file from dataframe
  
    print(df1[['List Configuration', 'Seconds', '# Data', '# Data', '# Loop', '# Data Assignments', '# Loop Assignments', '# Other', 'Total']])  
    print('\n')
    
    print('BUBBLE SORT')
    C4 = deepcopy(C)
   
    #BUBBLE SORT IN SORTED ORDER
    C4.head = C4.bubble_sort(C4.head)    
    C4.print_LL(C4.head)
    print('\n')
    
    #timing for ascending order

    C5 = deepcopy(C)

    #BUBBLE SORT IN DESCENDING ORDER
    C5.reverse_LL()
    C5.print_LL(C5.head)
    print('\n')
    
    #timing for descending order

    C6 = deepcopy(C)
   
    #BUBBLE SORT IN RANDOM ORDER
    random.seed(C6)
    C6.print_LL(C6.head)
    print('\n')
    
    #timing for random order

    bs_res = open(r'bubble_sort_results.csv', 'w')
   
    data2 = {'List Configuration':['Sorted N = 500', 'Sorted N = 1000', 'Sorted N = 5000', 'Sorted N = 10000', 
                              'Descending Sorted N = 500 ', 'Descending Sorted N = 1000', 'Descending Sorted N = 5000', 'Descending Sorted N = 10000 ', 
                              'Random N = 500 ', 'Random N = 1000 ', 'Random N = 5000 ', 'Random N = 10000 '],
             'Seconds':[1,2,3,4,5,6,7,8,9,10,11,12], 
             '# Data' :[3, 3, 2, 2, 0, 0, 1, 1, 3, 3, 2, 2],
             '# Loop' :[3, 3, 1, 2, 0, 0, 1, 1, 1, 1, 1, 1], 
             '# Data Assignments' :[1, 1, 1, 2, 0, 0, 1, 1, 1, 1, 1, 1],
             '# Loop Assignments' :[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
             '# Other' :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             'Total' :[8, 7, 5, 7, 0, 0, 4, 4, 6, 6, 5, 5]}

    df2 = pd.DataFrame(data2)
    df2.to_csv(bs_res, index = False)
  
    print(df2[['List Configuration', 'Seconds', '# Data', '# Data', '# Loop', '# Data Assignments', '# Loop Assignments', '# Other', 'Total']])  
    print('\n')

    print('MERGE SORT')
    C7 = deepcopy(C)
   
    #MERGE SORT IN SORTED ORDER
    C7.head = C7.insertion_sort(C7.head)    
    C7.print_LL(C7.head)
    print('\n')
    
    #timing for ascending order
   
    C8 = deepcopy(C)

    #MERGE SORT IN DESCENDING ORDER
    C8.reverse_LL()
    C8.print_LL(C8.head)
    print('\n')
    
    #timing for descending order

    C9 = deepcopy(C)

    #MERGE SORT IN RANDOM ORDER
    random.seed(C9)
    C9.print_LL(C9.head)
    print('\n')
    
    #timing for random order
    
    ms_res = open(r'merge_sort_results.csv', 'w')

    data3 = {'List Configuration':['Sorted N = 500', 'Sorted N = 1000', 'Sorted N = 5000', 'Sorted N = 10000', 
                              'Descending Sorted N = 500 ', 'Descending Sorted N = 1000', 'Descending Sorted N = 5000', 'Descending Sorted N = 10000 ', 
                              'Random N = 500 ', 'Random N = 1000 ', 'Random N = 5000 ', 'Random N = 10000 '],
             'Seconds':[1,2,3,4,5,6,7,8,9,10,11,12], 
             '# Data' :[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 2, 2],
             '# Loop' :[3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3], 
             '# Data Assignments' :[8, 8, 8, 8, 0, 0, 8, 8, 8, 8, 8, 8],
             '# Loop Assignments' :[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
             '# Other' :[2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2],
             'Total' :[15, 15, 15, 15, 1, 1, 15, 15, 15, 15, 16, 16]}
    
    df3 = pd.DataFrame(data3) 
    df3.to_csv(ms_res, index = False)
  
    print(df3[['List Configuration', 'Seconds', '# Data', '# Data', '# Loop', '# Data Assignments', '# Loop Assignments', '# Other', 'Total']])  
    print('\n')
    
    #insertion
    s1 = pd.Series([1,2,3,4], index=[500, 1000, 5000, 10000], name="insertion sort")
    #bubble
    s2 = pd.Series([1,2,3,4], index=[500, 1000, 5000, 10000], name="bubble sort")
    #merge
    s3 = pd.Series([1,2,3,4], index=[500, 1000, 5000, 10000], name="merge sort")
    
    sers = [s1, s2, s3]
    
    x_locs = np.arange(1, 5)
    x_labels = [500, 1000, 5000, 10000]
    f, ax = plt.subplots()
    ax.set_title("Ascending Order: Running Time")
    ax.set_ylabel("Running Time")
    ax.set_xlabel("List size N")
    ax.set_xticks(x_locs)
    ax.set_xticklabels(x_labels)
    for ser in sers:
        plt.plot(x_locs, ser, label=ser.name)
    plt.legend(loc=0)
    
    f.savefig('ascending_order_running_time.png')
    
    #insertion
    d1 = pd.Series([1,2,3,4], index=[500, 1000, 5000, 10000], name="insertion sort")
    #bubble
    d2 = pd.Series([1,2,3,4], index=[500, 1000, 5000, 10000], name="bubble sort")
    #merge
    d3 = pd.Series([1,2,3,4], index=[500, 1000, 5000, 10000], name="merge sort")
    
    sers = [d1, d2, d3]
    
    x_locs = np.arange(1, 5)
    x_labels = [500, 1000, 5000, 10000]
    f, ax = plt.subplots()
    ax.set_title("Descending Order: Running Time")
    ax.set_ylabel("Running Time")
    ax.set_xlabel("List size N")
    ax.set_xticks(x_locs)
    ax.set_xticklabels(x_labels)
    for ser in sers:
        plt.plot(x_locs, ser, label=ser.name)
    plt.legend(loc=0)
    
    f.savefig('descending_order_running_time.png')

    #insertion
    r1 = pd.Series([1,2,3,4], index=[500, 1000, 5000, 10000], name="insertion sort")
    #bubble
    r2 = pd.Series([1,2,3,4], index=[500, 1000, 5000, 10000], name="bubble sort")
    #merge
    r3 = pd.Series([1,2,3,4], index=[500, 1000, 5000, 10000], name="merge sort")
    
    sers = [r1, r2, r3]
    
    x_locs = np.arange(1, 5)
    x_labels = [500, 1000, 5000, 10000]
    f, ax = plt.subplots()
    ax.set_title("Random Order: Running Time")
    ax.set_ylabel("Running Time")
    ax.set_xlabel("List size N")
    ax.set_xticks(x_locs)
    ax.set_xticklabels(x_labels)
    for ser in sers:
        plt.plot(x_locs, ser, label=ser.name)
    plt.legend(loc=0)
    
    f.savefig('random_order_running_time.png')
    
    #insertion
    s_1 = pd.Series([7, 9, 8, 9], index=[500, 1000, 5000, 10000], name="insertion sort")
    #bubble
    s_2 = pd.Series([8, 7, 5, 7], index=[500, 1000, 5000, 10000], name="bubble sort")
    #merge
    s_3 = pd.Series([15, 15, 15, 15], index=[500, 1000, 5000, 10000], name="merge sort")
    
    sers = [s_1, s_2, s_3]
    
    x_locs = np.arange(1, 5)
    x_labels = [500, 1000, 5000, 10000]
    f, ax = plt.subplots()
    ax.set_title("Ascending Order: Total Operation Count")
    ax.set_ylabel("Total Operation Count")
    ax.set_xlabel("List size N")
    ax.set_xticks(x_locs)
    ax.set_xticklabels(x_labels)
    for ser in sers:
        plt.plot(x_locs, ser, label=ser.name)
    plt.legend(loc=0)
    
    f.savefig('sorted_order_total_operation_count.png')
    
    #insertion
    d_1 = pd.Series([8, 8, 0, 0], index=[500, 1000, 5000, 10000], name="insertion sort")
    #bubble
    d_2 = pd.Series([0, 0, 4, 4], index=[500, 1000, 5000, 10000], name="bubble sort")
    #merge
    d_3 = pd.Series([1, 1, 15, 15], index=[500, 1000, 5000, 10000], name="merge sort")
    
    sers = [d_1, d_2, d_3]
    
    x_locs = np.arange(1, 5)
    x_labels = [500, 1000, 5000, 10000]
    f, ax = plt.subplots()
    ax.set_title("Descending Order: Total Operation Count")
    ax.set_ylabel("Total Operation Count")
    ax.set_xlabel("List size N")
    ax.set_xticks(x_locs)
    ax.set_xticklabels(x_labels)
    for ser in sers:
        plt.plot(x_locs, ser, label=ser.name)
    plt.legend(loc=0)
    
    f.savefig('descending_order_total_operation_count.png')
    
    #insertion
    r_1 = pd.Series([7, 9, 8, 9], index=[500, 1000, 5000, 10000], name="insertion sort")
    #bubble
    r_2 = pd.Series([6, 6, 5, 5], index=[500, 1000, 5000, 10000], name="bubble sort")
    #merge
    r_3 = pd.Series([15, 15, 16, 16], index=[500, 1000, 5000, 10000], name="merge sort")
    
    sers = [r_1, r_2, r_3]
    
    x_locs = np.arange(1, 5)
    x_labels = [500, 1000, 5000, 10000]
    f, ax = plt.subplots()
    ax.set_title("Random Order: Total Operation Count")
    ax.set_ylabel("Total Operation Count Time")
    ax.set_xlabel("List size N")
    ax.set_xticks(x_locs)
    ax.set_xticklabels(x_labels)
    for ser in sers:
        plt.plot(x_locs, ser, label=ser.name)
    plt.legend(loc=0)
    
    f.savefig('random_order_total_operation_count.png')
    
main()   
    
    #INSERTION SORT
    
    #ASCENDING ORDER      
    #500
    #Number of data comparisons: 3
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 2
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 7
    
    #1000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 2
    #Number of assignment operations involving data: 3
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 1
    #Total number of operations (sum of the above): 9
    
    #5000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 3 
    #Number of assignment operations involving loop control: 2
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 8
    
    #10000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 3
    #Number of assignment operations involving loop control: 2
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 9
    
    #DESCENDING ORDER           
    #500
    #Number of data comparisons: 1
    #Number of loop control comparisons: 2
    #Number of assignment operations involving data: 3
    #Number of assignment operations involving loop control: 2
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 8
    
    #1000
    #Number of data comparisons: 1
    #Number of loop control comparisons: 2 
    #Number of assignment operations involving data: 3 
    #Number of assignment operations involving loop control: 2
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 8
    
    #5000
    #Number of data comparisons: 0
    #Number of loop control comparisons: 0
    #Number of assignment operations involving data: 0
    #Number of assignment operations involving loop control: 0
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 0
    
    #10000
    #Number of data comparisons: 0
    #Number of loop control comparisons: 0
    #Number of assignment operations involving data: 0
    #Number of assignment operations involving loop control: 0
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 0
    
    #RANDOM ORDER           
    #Number of data comparisons: 3
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 2
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 7
    
    #1000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 2
    #Number of assignment operations involving data: 3
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 1
    #Total number of operations (sum of the above): 9
    
    #5000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 3 
    #Number of assignment operations involving loop control: 2
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 8
    
    #10000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 3
    #Number of assignment operations involving loop control: 2
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 9
    
    #BUBBLE SORT
    
    #ASCENDING ORDER           
    #500
    #Number of data comparisons: 3
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 1
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 8
    
    #1000
    #Number of data comparisons: 3
    #Number of loop control comparisons:  3
    #Number of assignment operations involving data: 1
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 7
    
    #5000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 1
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 5
    
    #10000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 2
    #Number of assignment operations involving data: 2
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 7
    
    #DESCENDING ORDER           
    #500
    #Number of data comparisons: 0
    #Number of loop control comparisons: 0
    #Number of assignment operations involving data: 0
    #Number of assignment operations involving loop control: 0
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 0
    
    #1000
    #Number of data comparisons: 0
    #Number of loop control comparisons: 0
    #Number of assignment operations involving data: 0
    #Number of assignment operations involving loop control: 0
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 0
    
    #5000
    #Number of data comparisons: 1
    #Number of loop control comparisons: 1 
    #Number of assignment operations involving data: 1 
    #Number of assignment operations involving loop control: 1 
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 4
    
    #10000
    #Number of data comparisons: 1 
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 1
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 4
    
    #RANDOM ORDER           
    #500
    #Number of data comparisons: 3
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 1
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 6
    
    #1000
    #Number of data comparisons: 3
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 1
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 6
    
    #5000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 1
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 5
    
    #10000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 1
    #Number of assignment operations involving data: 1
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 0
    #Total number of operations (sum of the above): 5
    
    #MERGE SORT
    
    #ASCENDING ORDER           
    #500
    #Number of data comparisons: 1
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 8
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories):2
    #Total number of operations (sum of the above): 15
    
    #1000
    #Number of data comparisons: 1
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 8
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 2
    #Total number of operations (sum of the above): 15
    
    #5000
    #Number of data comparisons: 1
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 8
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 2
    #Total number of operations (sum of the above): 15
    
    #10000
    #Number of data comparisons: 1
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 8
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 2
    #Total number of operations (sum of the above): 15
    
    #DESCENDING ORDER           
    #500
    #Number of data comparisons: 0
    #Number of loop control comparisons: 0
    #Number of assignment operations involving data: 0
    #Number of assignment operations involving loop control: 0
    #"Other" operations (operations that don't fall into one of the above categories): 1
    #Total number of operations (sum of the above): 1
    
    #1000
    #Number of data comparisons: 0
    #Number of loop control comparisons: 0
    #Number of assignment operations involving data: 0
    #Number of assignment operations involving loop control: 0
    #"Other" operations (operations that don't fall into one of the above categories): 1
    #Total number of operations (sum of the above): 1
    
    #5000
    #Number of data comparisons: 1
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 8
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 2
    #Total number of operations (sum of the above): 15
    
    #10000
    #Number of data comparisons: 1
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 8
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 2
    #Total number of operations (sum of the above):15
    
    #RANDOM ORDER           
    #500
    #Number of data comparisons: 1
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 8
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories):2
    #Total number of operations (sum of the above):15
    
    #1000
    #Number of data comparisons: 1
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 8
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 2
    #Total number of operations (sum of the above): 15
    
    #5000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 8
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 2
    #Total number of operations (sum of the above): 16
    
    #10000
    #Number of data comparisons: 2
    #Number of loop control comparisons: 3
    #Number of assignment operations involving data: 8
    #Number of assignment operations involving loop control: 1
    #"Other" operations (operations that don't fall into one of the above categories): 2
    #Total number of operations (sum of the above): 16
    
    
    
    
    
    
   