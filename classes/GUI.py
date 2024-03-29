# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:35:05 2021

@author: adoso
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from .Connection import Connection
from .AbstractGraphMatrix import AbstractGraphMatrix
from .AbstractGraphList import AbstractGraphList
from .Errors import ConnectionNotExist
from .Errors import ConnectionExist

class GUI:
    """Klasa odpowiadajaca za graficzna reprezentacje programu, 
    oraz dzialnia na tej warstwie"""
    def __init__(self):
        self.__root = Tk()
        self.__frm = ttk.Frame(self.__root, padding=10)
        self.__frm.grid()
        self.__listboxes = []
        self.__radio = IntVar(self.__root, 1)
        self.__textRep = StringVar()
        self.__textSearch = StringVar()

    def run(self):
        """Uruchamia glowna petle, czyli mainloop()"""
        self.__root.mainloop()
        
    def addLabel(self, tekst, c, r, g=0):
        """Dodaje w wskazanym miejscu i oknie (g) Label"""
        where = self.__frm if g==0 else self.__newWindow
        ttk.Label(where, text=tekst).grid(column=c, row=r)
        
    def addButton(self, tekst, c, r, g=0, lam=lambda:print("Clicked!")):
        """Dodaje w wskazanym miejscu i oknie (g) przycisk, 
        który uruchamia funkcje lam przy kliknieciu"""
        where = self.__frm if g==0 else self.__newWindow
        ttk.Button(where, text=tekst, command=lam).grid(column=c, row=r)
        
    
    def addListBox(self, items, r, c, okno=0):
        """Dodaje w wskazanym miejscu i oknie (okno) listbox """
        if okno==0:
            listbox = Listbox(self.__root, exportselection=0)
        else:
            listbox = Listbox(self.__newWindow, exportselection=0)
        for x in items[::-1]:
            listbox.insert(0, x)
        listbox.grid(column=c, row=r)
        listbox.select_set(0)
        self.__listboxes.append(listbox)
            
    def getSelection(self):
        """Zwraca wybrane miasta w listboxach"""
        selection = []
        for x in self.__listboxes:
            selection.append(x.curselection())
            
        for x in range(len(selection)):
            selection[x] = selection[x][0]
        
        return selection
            
    def adConnection(self, graf, delete=0):
        """Dodaje lub usuwa (delete=0 lub =1) polaczenie miedzy zaznaczonymi miastami w listboxie"""
        citiesSelected = self.getSelection()
              
        cities = graf.getVertices()
    
        e = Connection(cities[citiesSelected[0]], cities[citiesSelected[1]])
        if(cities[citiesSelected[0]] != cities[citiesSelected[1]]):
            exist = graf.edgeExist(e)
            try:
                if not exist and delete:
                    raise ConnectionNotExist
                if delete:
                    graf.delEdge(e)
                elif not exist:
                    graf.addEdges(e)
                else:
                    raise ConnectionExist
            
                self.refresh(graf)
            except ConnectionNotExist:
                self.showError("Połączenie nie istnieje!")
            except ConnectionExist:
                self.showError("Połączenie już istnieje!")
        else:
            self.showError("To jest to samo miasto!")
        
    def showError(self, tekst):
        """Wywoluje messagebox.showerror z konkretnym tekstem"""
        messagebox.showerror(title="Error",
                             message=tekst)
        
    def addChoose(self, graf):
        """Dodaje wybor reprezentacji grafu w postaci radio buttonow"""
        r1 = Radiobutton(self.__root, text="Matrix", value=1, variable=self.__radio,
                         command = lambda : self.showMatrix(graf, 3))
        r2 = Radiobutton(self.__root, text="List", value=2, variable=self.__radio,
                         command = lambda : self.showList(graf, 3))
        r1.grid(column=0, row=2)
        r2.grid(column=0, row=3)



    def new_window(self):
        """Tworzy nowe okno programu (program dziala na 2 oknach)"""
        self.__newWindow = Toplevel(self.__root) 
        
    def showMatrix(self, graf, r):
        """Wyswietla reprezentacje macierzowa grafu"""
        tekst = "Legenda: \n"+str(graf.getGraf())+"\n"
        
        matrix = AbstractGraphMatrix(graf.getVertices(), graf.getEdges()).getMatrix()
        dl_matrix = range(len(matrix))
        tekst+="M"+str([x+1 for x in dl_matrix])+"\n"
        for x in dl_matrix:
            tekst+=str(x+1)+" "+str(matrix[x])+"\n"
        
        self.__textRep.set(tekst)
        ttk.Label(self.__root, textvariable=self.__textRep).grid(column = 1, columnspan=2, row=r)
        
       
            
    def showList(self, graf, r):
        """Wyswietla reprezentacje listy grafu"""
        tekst = ""
        matrix = AbstractGraphList(graf.getVertices(), graf.getEdges()).getList()
        cities = graf.getVertices()
        dl_matrix = range(len(matrix))
        for x in dl_matrix:
            tekst+=cities[x].getName()+"\n"+str([c.getName() for c in matrix[x]])+"\n\n"
        
        self.__textRep.set(tekst)
        
    def refresh(self, graf):
        """Odswieza liste/macierz grafu po zmianie polaczen"""
        if self.__radio.get() == 1:
            self.showMatrix(graf, 3)
        else:
            self.showList(graf, 3)
         
    def addSearchLabel(self):
        ttk.Label(self.__newWindow, textvariable=self.__textSearch).grid(
            column = 1, columnspan=2, row=3)

    #wyszukuje polaczenia i wyswietla najkrotsza droge
    def search(self, graf):
        """Wyszukuje polaczenie miedzy wybranymi miastami w listboxie i wyswietla je"""
        tekst = ""
        self.__textSearch.set("")
        citiesSelected = self.getSelection()
        cities = graf.getVertices()
        road = graf.BFS(cities[citiesSelected[2]], cities[citiesSelected[3]])
        if road == -1:
            self.__textSearch.set("Brak połączeń!")
        elif road == 0:
            self.__textSearch.set("To jest to samo miasto!")
        else:
            for x in range(len(road)):
                tekst+=road[x].getName()
                if not x == len(road)-1:
                    tekst+="->"
            self.__textSearch.set(tekst)
        
        