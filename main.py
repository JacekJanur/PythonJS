from classes.City import City
from classes.Connection import Connection
from classes.AbstractGraph import AbstractGraph
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
connections.append(Connection(cities[5], cities[2]))

connections.append(Connection(cities[4], cities[5]))

graf = AbstractGraph(cities, connections)


#graf.BFS(cities[0], cities[3])

print(graf.BFS(cities[0], cities[2]))