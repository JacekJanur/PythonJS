from classes.City import City
from classes.Connection import Connection
from classes.AbstractGraph import AbstractGraph
from classes.AbstractGraphMatrix import AbstractGraphMatrix
from classes.AbstractGraphList import AbstractGraphList
from classes.GUI import GUI
from iterators.ITcityId import ITcityId

cityId = ITcityId()

cities = []
cities.append(City("Kraków", cityId.__next__()))
cities.append(City("Nowy Sącz", cityId.__next__()))
cities.append(City("Rytro", cityId.__next__()))
cities.append(City("Piwniczna", cityId.__next__()))
cities.append(City("Warszawa", cityId.__next__()))
cities.append(City("Gdańsk", cityId.__next__()))
cities.append(City("Wałbrzych", cityId.__next__()))

connections = []
connections.append(Connection(cities[0], cities[1]))
connections.append(Connection(cities[0], cities[2]))
connections.append(Connection(cities[0], cities[3]))
connections.append(Connection(cities[2], cities[3]))
connections.append(Connection(cities[1], cities[4]))
connections.append(Connection(cities[5], cities[2]))
connections.append(Connection(cities[5], cities[3]))

connections.append(Connection(cities[4], cities[5]))

graf = AbstractGraph(cities, connections)


#graf.BFS(cities[0], cities[3])

#print(graf.BFS(cities[0], cities[2]))

graf2 = AbstractGraphMatrix(cities, connections)
print(graf2.getMatrix())

graf3 = AbstractGraphList(cities, connections)
print(graf3.getList())


x = GUI()

x.addButton("Wyjdź", 0, 0)
x.new_window()
x.addLabel("Drugie okno", 0, 1, 1)
x.addListBox(cities, 2, 2)
x.run()