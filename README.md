
**Jacek Janur GL.01**

**Projekt z Języków Symbolicznych**
**Dokumentacja**

# Temat projektu
Projekt jest programem do wyszukiwania połączeń kolejowych między miastami. Aplikacja uruchamia się w dwóch osobnych oknach, w pierwszym ustawiamy połączenia a w drugim wyszukujemy je. Program domyślnie ma 10 zdefiniowanych miast, gdzie z każdego można dojechać do dowolnego miasta (z przesiadkami). Wyszukiwanie połączeń i znajdowanie najkrótszej drogi jest realizowane za pomocą algorytmu BFS. Reprezentacja grafu połączeń jest realizowana poprzez macierz i listę. Użytkownik w dowolnym momencie może wybierać między tymi dwoma reprezentacjami.
# Klasy
## [AbstractGraph](https://github.com/JacekJanur/PythonJS/blob/main/classes/AbstractGraph.py)
### Zmienne:
- __vertices
- __edges
- __graf
#### __init __(vertices, edges)
Pobiera dwa argumenty: listę złożoną z obiektów klasy [City](https://github.com/JacekJanur/PythonJS/blob/main/classes/City.py) i listę złożoną z obiektów klasy [Connection](https://github.com/JacekJanur/PythonJS/blob/main/classes/Connection.py). Przypisuje je do swoich zmiennych, tworzy również zmienną __graf będącą słownikiem.

#### getVertices()
Zwraca listę złożoną z obiektów klasy [City](https://github.com/JacekJanur/PythonJS/blob/main/classes/City.py)
#### addVertices(City)
Dodaje do zmiennej __vertices, i słownika __graf nowy obiekt klasy [City](https://github.com/JacekJanur/PythonJS/blob/main/classes/City.py)
#### getEdges()
Zwraca listę złożoną z obiektów klasy [Connection](https://github.com/JacekJanur/PythonJS/blob/main/classes/Connection.py)
#### addEdges(Connection)
Dodaje do zmiennej __edges nowe połączenie (obiekt klasy [Connection](https://github.com/JacekJanur/PythonJS/blob/main/classes/Connection.py))
#### delEdge(Connection)
Usuwa konkretne połączenie
#### edgeExists(Connection)
Zwraca prawdę/fałsz w zależności czy istnieje dane połączenie
#### getGraf()
Zwraca zmienną __graf
#### getNeighbours(City)
Zwraca listę miast do których można dojechać z konkretnego miasta
#### getFrom(City)
Zwraca listę miast z których można dojechać z konkretnego miasta
#### BFS(start, goal)
Implementacja algorytmu BFS. Zwraca najkrótszą trasę między miastami jeżeli istnieje, w przeciwnym  przypadku zwraca 0 (jeżeli start=goal) lub -1 (nie ma trasy między miastami)

## [AbstractGraphList](https://github.com/JacekJanur/PythonJS/blob/main/classes/AbstractGraphList.py)
### Zmienne:
- __vertices
- __edges
- __graf
- __list
#### __init __(vertices, edges)
Pobiera dwa argumenty: listę złożoną z obiektów klasy [City](https://github.com/JacekJanur/PythonJS/blob/main/classes/City.py) i listę złożoną z obiektów klasy [Connection](https://github.com/JacekJanur/PythonJS/blob/main/classes/Connection.py). Wywołuje konstruktor klasy AbstractGraph i dodatkowo tworzy zmienną __list będącą reprezentacją grafu poprzez listę
#### getList()
Zwraca zmienną __list
## [AbstractGraphMatrix](https://github.com/JacekJanur/PythonJS/blob/main/classes/AbstractGraphMatrix.py)
### Zmienne:
- __vertices
- __edges
- __graf
- __matrix
#### __init __(vertices, edges)
Pobiera dwa argumenty: listę złożoną z obiektów klasy [City](https://github.com/JacekJanur/PythonJS/blob/main/classes/City.py) i listę złożoną z obiektów klasy [Connection](https://github.com/JacekJanur/PythonJS/blob/main/classes/Connection.py). Wywołuje konstruktor klasy AbstractGraph i dodatkowo tworzy zmienną __matrix będącą macierzową reprezentacją grafu
#### getMatrix()
Zwraca zmienną __matrix
## [City](https://github.com/JacekJanur/PythonJS/blob/main/classes/City.py)
### Zmienne:
- __name
- __id
#### __init __(name, id)
Tworzy miasto o podanej nazwie i numerze id
#### __getName()
Zwraca nazwę miasta
#### __getId()
Zwraca id miasta
#### __str __()
Definiuje w jaki sposób miasto powinno być wyświetlane

## [Connection](https://github.com/JacekJanur/PythonJS/blob/main/classes/Connection.py)
### Zmienne:
- __start
- __end
#### __init __(a, b)
Tworzy połączenie z miasta a do miasta b
#### __getStart()
Zwraca początkowe miasto
#### __getEnd()
Zwraca końcowe miasto
#### getConnection()
Zwraca miasto początkowe i końcowe
#### __str __()
Definiuje w jaki sposób połączenie powinno być wyświetlane
#### __init __()
Definiuje przypadek kiedy połączenia są sobie równe
## [Error](https://github.com/JacekJanur/PythonJS/blob/main/classes/Errors.py)
Klasa bazowa dla błędów
## [ConnectionExist](https://github.com/JacekJanur/PythonJS/blob/main/classes/Errors.py)
Wyjątek gdy istnieje dane połączenie
## [ConnectionNotExist](https://github.com/JacekJanur/PythonJS/blob/main/classes/Errors.py)
Wyjątek gdy nie istnieje dane połączenie
## [GUI](https://github.com/JacekJanur/PythonJS/blob/main/classes/GUI.py)
### Zmienne:
- __root
- __frm
- __listboxes
- __radio
- __textRep
- __textSearch
#### __init __()
Definiuje powyższe zmienne, tworzy okno.
####  run()
Uruchamia polecenie __root.mainloop()
####  addLabel(tekst, column, row, okno)
Dodaje pole Label z określonym tekstem, określonym miejscu i oknie (program działa w dwóch oknach)
####  addButton(tekst, column, row, okno, lambda)
Dodaje przycisk z określonym tekstem, określonym miejscu i oknie. Dodatkowo przyjmuje jako argument anonimową funkcję, która działa w momencie naciśnięcia przycisku
####  addListBox(items, row, column, okno)
Dodaje pole listbox z określonymi przedmiotami, określonym miejscu i oknie
####  getSelection()
Zwraca listę aktualnie wybranych opcji w listboxach
####  adConnection(graf, delete)
Dodaje (delete =0) lub usuwa (delete=1) połączenie na podanym grafie. Miasta wybiera korzystając z metody getSelection()
####  showError(tekst)
Wyświetla okienko błędu z określonym tekstem
####  AddChoose(graf)
Dodaje wybór reprezentacji grafu jako listę lub macierz
####  new_window()
Tworzy nowe okno aplikacji
####  showMatrix(graf, row)
Wyświetla macierzową reprezentacje podanego grafu na podanym miejscu
####  showList(graf, row)
Wyświetla listową reprezentacje podanego grafu na podanym miejscu
####  refresh()
Odświeża reprezentacje grafu przy jakiejkolwiek zmianie połączeń
####  search(graf)
Wyszukuje połączenie między zaznaczonymi miastami (getSelection()) i wyświetla najkrótszą drogą między nimi, lub zwraca napis, że dane połączenie nie istnieje.
