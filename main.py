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
cities.append(City("Berlin", cityId.__next__()))
cities.append(City("Sosnowiec", cityId.__next__()))
cities.append(City("Las Vegas", cityId.__next__()))



connections = []
connections.append(Connection(cities[0], cities[1]))
connections.append(Connection(cities[1], cities[2]))
connections.append(Connection(cities[2], cities[3]))
connections.append(Connection(cities[3], cities[4]))
connections.append(Connection(cities[4], cities[5]))
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

x.run()