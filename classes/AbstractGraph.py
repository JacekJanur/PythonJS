# -*- coding: utf-8 -*-

class AbstractGraph:
    def __init__(self, vertices, edges):
        self.__vertices = vertices
        self.__edges = edges
        self.__graf = {x.getId():x.getName() for x in vertices}
    
    def getVertices(self):
        return self.__vertices
    
    def addVertices(self, c):
        self.__vertices.append(c)
        self.__graf[c.getId()] = self.__graf[c.getName()]
    
    def getEdges(self):
        return self.__edges
    
    def addEdges(self, e):
        self.__edges.append(e)
    
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

 
    def BFS(self, start, goal): #0-ten same node, -1 - nie ma trasy
        visited = []
         
        queue = [[start]]

        if start == goal:
            return 0

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in visited:
                neighbours = self.getNeighbours(node)

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        return new_path
                visited.append(node)
     
        return -1