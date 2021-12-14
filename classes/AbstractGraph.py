# -*- coding: utf-8 -*-

class AbstractGraph:
    def __init__(self, vertices, edges):
        self.__vertices = vertices
        self.__edges = edges
        self.__graf = {x.getId():x.getName() for x in vertices}
    
    def getVertices(self):
        return self.__vertices
    
    def getEdges(self):
        return self.__edges
    
    def getGraf(self):
        return self.__graf
    
    def getNeighbours(self, a): #wszyscy sąsiedzi danej krawędzi
        neighbours = []
        for x in self.getEdges():
            if x.getStart() == a:
                neighbours.append(x.getEnd())
        return neighbours
        
    def getFrom(self, a): # skąd do danej krawędzi możemy dotrzeć
        neighbours = []
        for x in self.getEdges():
            if x.getEnd() == a:
                neighbours.append(x.getStart())
        return neighbours
    
    def BFS(self, skad, do):    
        for x in self.getVertices():
            x.visited = False
            
        queue = []
 
        queue.append(skad)
        skad.visited = True
 
        while queue:
 
            skad = queue.pop(0)

            for i in self.getNeighbours(skad):
                if i.visited == False:
                    queue.append(i)
                    i.visited = True
                    if i.getId() == do.getId():
                        print("jest połączenie")
                    
            