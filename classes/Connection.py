# -*- coding: utf-8 -*-

class Connection:
    def __init__(self, a, b):
        self.__start = a
        self.__end = b
        
    def getStart(self):
        return self.__start     
        
    def getEnd(self):
        return self.__end
         
    def getConnection(self):
        return self.__start, self.__end
