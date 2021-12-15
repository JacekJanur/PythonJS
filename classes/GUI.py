# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:35:05 2021

@author: adoso
"""

from tkinter import *
from tkinter import ttk


class GUI:
    def __init__(self):
        self.__root = Tk()
        self.__frm = ttk.Frame(self.__root, padding=10)
        self.__frm.grid()

    def run(self):
        self.__root.mainloop()
        
    def addLabel(self, tekst, c, r, g=0):
        where = self.__frm if g==0 else self.__newWindow
        ttk.Label(where, text=tekst).grid(column=c, row=r)
        
    def addButton(self, tekst, c, r, g=0):
        where = self.__frm if g==0 else self.__newWindow
        ttk.Button(where, text=tekst, command=self.__root.destroy).grid(column=c, row=r)
        
        
    def new_window(self):
        self.__newWindow = Toplevel(self.__root) 
        