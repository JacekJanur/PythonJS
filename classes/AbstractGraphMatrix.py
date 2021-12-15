# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 08:07:00 2021

@author: adoso
"""

from .AbstractGraph import AbstractGraph

class AbstractGraphMatrix(AbstractGraph):
    def __init__(self, vertices, edges):
        super().__init__(vertices, edges)
        matrix = []
       
        for vi in vertices:
            row = [0 for x in vertices]
            #gen = (x for x in edges if x.getStart().getId() == vi.getId())
            #for e in gen:
            #    if e.getStart().getId() == 
            for n in self.getNeighbours(vi):
                row[n.getId()-1] = 1
            matrix.append(row)
            
            
        self.__matrix = matrix
        
        
    def getMatrix(self):
        return self.__matrix