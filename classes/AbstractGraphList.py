# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:10:49 2021

@author: adoso
"""
from .AbstractGraph import AbstractGraph

class AbstractGraphList(AbstractGraph):
    """Klasa dziedziczaca po AbstractGraph, odpowiada ze reprezentacje grafu poprzez liste"""
    def __init__(self, vertices, edges):
        super().__init__(vertices, edges)
        lista = []
       
        for vi in vertices:
            row = []
            for n in self.getNeighbours(vi):
                row.append(n)
            lista.append(row)
            
            
        self.__list = lista
        
        
    def getList(self):
        """Zwraca liste polaczen grafu"""
        return self.__list