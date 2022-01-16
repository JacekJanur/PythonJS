# -*- coding: utf-8 -*-
import unittest

from classes.City import City
from classes.Connection import Connection
from classes.AbstractGraph import AbstractGraph
from classes.AbstractGraphMatrix import AbstractGraphMatrix
from classes.AbstractGraphList import AbstractGraphList
from iterators.ITcityId import ITcityId
from classes.GUI import GUI

cityId = ITcityId()

cities = []
cities.append(City("Kraków", cityId.__next__()))
cities.append(City("Nowy Sącz", cityId.__next__()))
cities.append(City("Rytro", cityId.__next__()))
cities.append(City("Piwniczna", cityId.__next__()))
cities.append(City("Warszawa", cityId.__next__()))
cities.append(City("Gdańsk", cityId.__next__()))
cities.append(City("Wałbrzych", cityId.__next__()))
cities.append(City("Berlin", cityId.__next__()))
cities.append(City("Sosnowiec", cityId.__next__()))
cities.append(City("Las Vegas", cityId.__next__()))

connections = []
connections.append(Connection(cities[0], cities[1]))
connections.append(Connection(cities[1], cities[2]))
connections.append(Connection(cities[2], cities[3]))
connections.append(Connection(cities[2], cities[4]))
connections.append(Connection(cities[3], cities[4]))
connections.append(Connection(cities[4], cities[5]))
connections.append(Connection(cities[4], cities[3]))
connections.append(Connection(cities[5], cities[6]))
connections.append(Connection(cities[6], cities[7]))
connections.append(Connection(cities[7], cities[8]))
connections.append(Connection(cities[8], cities[9]))
connections.append(Connection(cities[9], cities[0]))

graf = AbstractGraph(cities, connections)
graf2 = AbstractGraphMatrix(cities, connections)
graf3 = AbstractGraphList(cities, connections)

x = GUI()
x.addListBox(cities, 0, 1)
x.addListBox(cities, 0, 2)
x.addButton("Dodaj połączenie", 0, 0, 0, lambda:x.adConnection(graf))
x.addButton("Usuń połączenie", 0, 1, 0, lambda:x.adConnection(graf,1))
x.addChoose(graf)
x.showMatrix(graf, 3)
x.new_window()
x.addButton("Wyszukaj połączenie", 0, 0, 1, lambda:x.search(graf))
x.addListBox(cities, 0, 1, 1)
x.addListBox(cities, 0, 2, 1)
x.addSearchLabel()


class Testy(unittest.TestCase):
    """Klasa zawierajaca podstawowe testy"""
    def test1(self):
        """Wyszukanie polaczenia miedzy dwoma miastami"""
        self.assertEqual(type(graf2.BFS(cities[2], cities[3])), type(cities[2:4]))
    
    def test2(self):
        """Wyszukanie polaczenia miedzy dwoma miastami z przynajmniej dwoma przystankami"""
        self.assertEqual(type(graf2.BFS(cities[2], cities[9])), type(cities[2:10]))
        
    def test3(self):
        """Dodanie połączenie bezporedniego między dwoma miastami z test2.
        Oczekiwana informacja o połączeniu bezposrednim"""
        graf2.addEdges(Connection(cities[2], cities[9]))
        self.assertEqual(len(graf2.BFS(cities[2], cities[9])), 2) 
        #2 poniewaz algorytm zwraca liste 2 miast - poczatkowe i koncowe
        
    def test4(self):
        """Usuniecie bezposredniego polaczenia miedzy miastami z test1.
        Oczekiwana informacja o przesiadce"""
        graf2.delEdge(Connection(cities[2], cities[3]))
        self.assertGreater(len(graf2.BFS(cities[2], cities[3])), 2)
        #wiecej niz 2, czyli algorytm dodaje inne posrednie miasta
    
    def test5(self):
        """Usuniecie wszystkich polaczen do danego miasta.
        Oczekiwana informacja o braku polaczenia"""
        graf2.delEdge(Connection(cities[8], cities[9]))
        self.assertEqual(graf2.BFS(cities[8], cities[0]), -1)
        #algorytm zwraca -1 w przypadku braku polaczenia
        
    def test6(self):
        """test2 w drugiej reprezentacji grafu"""
        self.assertEqual(type(graf3.BFS(cities[2], cities[9])), type(cities[2:10]))
        
    def test7(self):
        """test3 w drugiej reprezentacji grafu"""
        graf3.addEdges(Connection(cities[5], cities[9]))
        self.assertEqual(len(graf3.BFS(cities[5], cities[9])), 2)
                   
        
if __name__ == '__main__':
    unittest.main()
