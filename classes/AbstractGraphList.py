# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:10:49 2021

@author: adoso
"""
from .AbstractGraph import AbstractGraph

class AbstractGraphList(AbstractGraph):
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
        return self.__list