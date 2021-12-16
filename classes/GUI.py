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
        self.__listboxes = []

    def run(self):
        self.__root.mainloop()
        
    def addLabel(self, tekst, c, r, g=0):
        where = self.__frm if g==0 else self.__newWindow
        ttk.Label(where, text=tekst).grid(column=c, row=r)
        
    def addButton(self, tekst, c, r, g=0, lam=lambda:print(1)):
        where = self.__frm if g==0 else self.__newWindow
        ttk.Button(where, text=tekst, command=lam).grid(column=c, row=r)
        
    
    def addListBox(self, items, r, c):
        listbox = Listbox(self.__root, exportselection=0)
        for x in items[::-1]:
            listbox.insert(0, x)
        listbox.grid(column=c, row=r)
        self.__listboxes.append(listbox)
            
    def getSelection(self):
        selection = []
        for x in self.__listboxes:
            selection.append(x.curselection())
            
        for x in range(len(selection)):
            selection[x] = selection[x][0]
        
        print(selection)
            
        
        
    
    def new_window(self):
        self.__newWindow = Toplevel(self.__root) 
        