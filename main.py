from classes.City import City
from classes.Connection import Connection
from classes.AbstractGraph import AbstractGraph
from classes.AbstractGraphMatrix import AbstractGraphMatrix
from classes.AbstractGraphList import AbstractGraphList
from classes.GUI import GUI
from iterators.ITcityId import ITcityId

cityId = ITcityId()

nazwy = ["Kraków", "Nowy Sącz", "Ryto", "Piwniczna", "Warszawa", "Gdańsk"
         ,"Wałbrzych", "Berlin", "Sosnowiec", "Las Vegas"]

cities = [City(nazwa, cityId.__next__()) for nazwa in nazwy]

connections = []
connections = [Connection(cities[i%10], cities[(i+1)%10]) for i in range(10)]

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

x.run()