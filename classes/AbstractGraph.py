# -*- coding: utf-8 -*-

class AbstractGraph:
    def __init__(self, vertices, edges):
        self.__vertices = vertices
        self.__edges = edges
    
    def getVertices(self):
        return self.__vertices
    
    def getEdges(self):
        return self.__edges
    
    def getNeighbours(self, a):
        neighbours = []
        for x in self.getEdges():
            if x.getStart() == a:
                neighbours.append(x.getEnd())
        return neighbours
        
    def getFrom(self, a):
        neighbours = []
        for x in self.getEdges():
            if x.getEnd() == a:
                neighbours.append(x.getStart())
        return neighbours