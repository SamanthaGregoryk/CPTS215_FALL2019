'''
Programmer: Samantha Gregoryk     
Class: CptS 215-01, Fall 2019     
Programming Assignment #6   
11/6/2019   
 
Description: Once the user has inputted their actor
 or actress of choice, the game will find the 
 correlating bacon number they have. The bacon number
 is determined by how many movies they have been in
 with costars who circle back to Kevin Bacon.  
'''

class Queue:
    def __init__(self):
        '''
        Creates an empty queue.
        '''
        self.items = []
        
    def is_empty(self):
        '''
        Checks to see if queue
        is empty or not. 
        '''
        return self.items == []

    def enqueue(self, item):
        '''
        Adds an item to the stack.
        '''
        self.items.insert(0,item)

    def dequeue(self):
        '''
        Deletes the first item
        from the stack. 
        '''
        return self.items.pop()

    def size(self):
        '''
        Returns the size of the
        stack.
        '''
        return len(self.items)
    
def BFS(graph, root):
        '''
        Finds the shortest path 
        to reach the root and prints
        out all the edges along the 
        way.
        '''
        Q = Queue()
        Q.enqueue(root)
        
        G = Graph()
        T = G.add_vertex(root)
        
        while Q:
          v = Q.dequeue()
          for edge in graph[v]:
              if edge not in T:
                T.append(edge)
                Q.enqueue(edge)
 
        return T