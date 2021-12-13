from classes.City import City
from classes.Connection import Connection
from classes.AbstractGraph import AbstractGraph
from iterators.ITcityId import ITcityId

cityId = ITcityId()

cities = []
cities.append(City("Kraków", cityId.__next__()))
cities.append(City("Nowy Sącz", cityId.__next__()))

connections = []
connections.append(Connection(cities[0], cities[1]))

graf = AbstractGraph(cities, connections)
print(graf.getFrom(cities[0]))