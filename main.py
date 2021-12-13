from classes.City import City
from classes.Connection import Connection
from iterators.ITcityId import ITcityId

cityId = ITcityId()

Krakow = City("Kraków", cityId.__next__())
Sacz = City("Nowy Sącz", cityId.__next__())

connections = []
connections.append(Connection(Krakow, Sacz))

