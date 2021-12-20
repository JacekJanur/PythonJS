# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:35:05 2021

@author: adoso
"""

from tkinter import *
from tkinter import ttk
from .Connection import Connection
from .AbstractGraphMatrix import AbstractGraphMatrix
from .AbstractGraphList import AbstractGraphList

class GUI:
    def __init__(self):
        self.__root = Tk()
        self.__frm = ttk.Frame(self.__root, padding=10)
        self.__frm.grid()
        self.__listboxes = []
        self.__radio = IntVar(self.__root, 1)
        self.__textRep = StringVar()

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
        
        return selection
            
    def addConnection(self, graf):
        
        citiesSelected = self.getSelection()
              
        cities = graf.getVertices()
    
        
        graf.addEdges(Connection(cities[citiesSelected[0]], cities[citiesSelected[1]]))
        
        self.refresh(graf)

    def addChoose(self, graf):
        r1 = Radiobutton(self.__root, text="Matrix", value=1, variable=self.__radio,
                         command = lambda : self.showMatrix(graf, 3))
        r2 = Radiobutton(self.__root, text="List", value=2, variable=self.__radio,
                         command = lambda : self.showList(graf, 3))
        r1.grid(column=0, row=2)
        r2.grid(column=0, row=3)



    def new_window(self):
        self.__newWindow = Toplevel(self.__root) 
        
    def showMatrix(self, graf, r):
        
        tekst = "Legenda: \n"+str(graf.getGraf())+"\n"
        
        matrix = AbstractGraphMatrix(graf.getVertices(), graf.getEdges()).getMatrix()
        dl_matrix = range(len(matrix))
        tekst+="M"+str([x+1 for x in dl_matrix])+"\n"
        for x in dl_matrix:
            tekst+=str(x+1)+" "+str(matrix[x])+"\n"
        
        self.__textRep.set(tekst)
        ttk.Label(self.__root, textvariable=self.__textRep).grid(column = 1, columnspan=2, row=r)
        
       
            
    def showList(self, graf, r):
        tekst = ""
        matrix = AbstractGraphList(graf.getVertices(), graf.getEdges()).getList()
        dl_matrix = range(len(matrix))
        for x in dl_matrix:
            tekst+=str(x+1)+" "+str([c.getName() for c in matrix[x]])+"\n"
        
        self.__textRep.set(tekst)
        
    def refresh(self, graf):
        if self.__radio.get() == 1:
            self.showMatrix(graf, 3)
        else:
            self.showList(graf, 3)
         
        