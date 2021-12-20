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


    def __str__(self):
        return self.getStart().getName()+"->"+self.getEnd().getName()
    
    def __eq__(self, e):
        return self.getStart() == e.getStart() and self.getEnd() == e.getEnd()