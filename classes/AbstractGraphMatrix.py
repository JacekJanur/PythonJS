# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 08:07:00 2021

@author: adoso
"""

from .AbstractGraph import AbstractGraph

class AbstractGraphMatrix(AbstractGraph):
    """Klasa dziedziczaca po AbstractGraph, odpowiada ze reprezentacje grafu poprzez macierz"""
    def __init__(self, vertices, edges):
        super().__init__(vertices, edges)
        matrix = []
        for vi in vertices:
            row = [0 for x in vertices]
            for n in self.getNeighbours(vi):
                row[n.getId()-1] = 1
            matrix.append(row)
            
            
        self.__matrix = matrix
        
        
    def getMatrix(self):
        """Zwraca macierz polaczen grafu"""
        return self.__matrix