#Jake Edwards
#HW5 #6 - DFS Implementation
#CSC 342_001
#4/18/2019

import sys
from collections import defaultdict
import time

def loadFile(fname):
    with open(fname) as file:
        num_verts = file.readline() #number of vertices in graph
        num_edges = file.readline() #number of edges in graph
        edges = list() #Hold edges as tuple of vertices(source, destination)

        for line in file:
            source, destination = line.rstrip().split(',')
            edges.append((source, destination))

        return (num_verts, num_edges, edges)

class Vertex():
    def __init__(self, number):
        self.number = number
        self.color = 'white'
        self.parent = None
        self.d = None
        self.f = None

class Graph():
    def __init__(self, num_verts, num_edges, edges):
        self.num_verts = num_verts
        self.num_edges = num_edges
        self.vertices = dict()
        self.adj = defaultdict(list)
        self.time = 0

        #Get distinct vertices
        temp_vert = set()
        for source, dest in edges:
            temp_vert.add(source)
            temp_vert.add(dest)

        #Now create vertex objects from temp_vert and store in self.vertices
        for vertex_num in temp_vert:
            vert_obj = Vertex(vertex_num)
            self.vertices[vertex_num] = vert_obj

        #Create adjacency list to hold edges between vertices
        for source, dest in edges:
            self.adj[source].append(dest)
            self.adj[dest].append(source)
            
            #remove duplicate destination vertices
            self.adj[source] = list(dict.fromkeys(self.adj[source]))
            self.adj[dest] = list(dict.fromkeys(self.adj[dest]))

    def dfs(self):
        for vertex in self.vertices:
            vertex = self.vertices[vertex]
            if vertex.color == 'white':
                self.dfs_visit(vertex)

    def dfs_visit(self, u):
        #print("Visited: " + str(u.number))
        self.time = self.time + 1  #white vertex u has just been discovered
        u.d = time
        u.color = 'black'
        for v in self.adj[u.number]: #explore edge (u,v)
            v = self.vertices[v]
            if v.color == 'white':
                v.parent = u
                print(str(u.number) + ' to ' + str(v.number))
                self.dfs_visit(v)
        u.color = 'black' #blacken u, it is finished
        print(str(u.number) + ' fully explored')
        self.time = self.time + 1
        u.f = time

    

if __name__ == "__main__":
    #If no command line arg is provided
    if len(sys.argv) == 1:
        print("Must enter a filename containing graph information...closing")
        sys.exit(1)

    print("Author: Jake Edwards\n")
    num_verts, num_edges, edges = loadFile(sys.argv[1])

    #Create graph g
    g = Graph(num_verts, num_edges, edges)    

    print("DFS Visitation Order:")
    g.dfs() #Call Depth First Search on graph g

    print('\nTree edges:\n' + str(edges))
