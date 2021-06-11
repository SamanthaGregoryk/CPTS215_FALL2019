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

class Graph(object):
    def __init__(self, graph):
        '''
        Initializes the graph and takes in an object.
        '''
        self.graph_dict = graph

    def vertices(self):
        '''
        Prints the vertices of the graph.
        '''
        return list(self.graph_dict.keys())

    def edges(self):
        '''
        Prints out the edges connected
        to the correlating vertices.
        '''
        edges = []
        for v in self.graph_dict:
            for n in self.graph_dict[v]:
                if {n, v} not in edges:
                    edges.append({v, n})
        return edges

    def add_vertex(self, v):
        '''
        Adds a vertex to the graph if 
        it is not already in the graph. 
        '''
        if v not in self.graph_dict:
            self.graph_dict[v] = []
            
    def add_edge(self, e):
        '''
        Adds an edge to the graph. 
        '''
        e = set(e)
        (v1, v2) = tuple(e)
        if v1 in self.graph_dict:
            self.graph_dict[v1].append(v2)
        else:
            self.graph_dict[v1] = [v2]