# -*- coding: utf-8 -*-

class City:
    """Klasa bedaca reprezentacja miasta"""
    def __init__(self, name, nr):
        self.__name = name
        self.__id = nr
        
    
    def getName(self):
        return self.__name
    def getId(self):
        return self.__id
    
    def __str__(self):
        return str(self.getId())+ "."+self.getName()
