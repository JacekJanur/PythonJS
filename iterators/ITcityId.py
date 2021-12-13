# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 08:04:54 2021

@author: adoso
"""

class ITcityId:  
    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 1
        return self.index