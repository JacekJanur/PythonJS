# -*- coding: utf-8 -*-

class AbstractGraph:
    """Klasa będąca bazową reprezentacją grafu.
    Zawiera w sobie wszelkie potrzebne metody, np. pobranie sąsiadów danej krawędzi."""
   
    def __init__(self, vertices, edges):
        self.__vertices = vertices
        self.__edges = edges
        self.__graf = {x.getId():x.getName() for x in vertices}
    
    def getVertices(self):
        """Zwraca miasta (wierzcholki)"""
        return self.__vertices
    
    def addVertices(self, c):
        """Dodaje miasto (wierzcholek)"""
        self.__vertices.append(c)
        self.__graf[c.getId()] = self.__graf[c.getName()]
    
    def getEdges(self):
        """Zwraca polaczenia miedzy miastami (krawedzie grafu)"""
        return self.__edges
    
    def addEdges(self, e):
        """Dodaje polaczenie miedzy miastami (krawedzie grafu)"""
        self.__edges.append(e)
        
    def delEdge(self, e):
        """Usuwa polaczenie miedzy miastami (krawedzie grafu)"""
        self.__edges.remove(e)
    
    def edgeExist(self, e):
        """Sprawdza czy polaczenie miedzy miastami (krawedzie grafu) istnieje"""
        return (e in self.__edges)
    
    
    def getGraf(self):
        """Zwraca graf w postaci slownika"""
        return self.__graf
    
    def getNeighbours(self, a):
        """Zwraca miasta do ktorych mozna dojechac z miasta a"""
        neighbours = []
        for x in self.getEdges():
            if x.getStart() == a:
                neighbours.append(x.getEnd())
        return neighbours
        
    def getFrom(self, a):
        """Zwraca miasta z ktorych mozna dojechac z miasta a"""
        neighbours = []
        for x in self.getEdges():
            if x.getEnd() == a:
                neighbours.append(x.getStart())
        return neighbours

 
    def BFS(self, start, goal): #0-ten same node, -1 - nie ma trasy
        """Implementacja algorytmu BFS. Zwraca najkrótszą drogę między miastami, lub:
        0 - miasto poczatkowe i koncowe jest tym samym miastem
        -1 - nie istnieje trasa miedzy miastami"""
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