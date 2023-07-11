# Django Fundamentals

Framework do tworzenia aplikacji webowych. 
Architektura MTV Model Template View. W nie-pythonie MVC.

Trzy warstwy są w miarę niezależne, można je łatwiej modyfikować/podmieniać. 

a) Model - dane i ich struktura. ORM Django Models. 
Można też SQLAlchemy, ale CMS (Django Admin), user i migracje mogą nie działać.
Można używać NoSQL, np. PyMongo.

b) Template - warstwa prezentacji. System templatek Django Templates. 
Można też Jinja2 (faster, safer), ale admina trzeba ustawić na Templates, bo nie będzie działać. 

c) View - logika łącząca model i warstwę prezentacji. Funkcje i klasy w widokach Django. 
Używamy klas, bo zmniejszają ilość kodu do implementacji (widoki są podobne).

Inne architektury:
MVVM - Model View ViewModel modyfikacja widoku zmienia dane i na odwrót
MV* - Model View Whatever (MVPresenter, MVController, MVAdapter)

To są kombajny, a dzisiaj pisze się raczej mikroserwisy, żeby oddzielać backend od frontendu. 
Potrzeba między nimi połączenia (protokołu komunikacji:
- RESTAPI - zestaw zasad do wymiany danych między frontem a backendem. Restful API - spełnia zasady REST.
- GraphQL - oparte na grafach, wymaga więcej pracy, ma sens w apkach, które robią dużo requestów do serwera. 
- SOAP - w oparciu o XML, raczej niespotykany dzisiaj. 
- AJAX - Asynchronous JavaScript and XML, umożliwia robienie zapytań w tle. Dzięki temu powstał Web2.0, bo nie trzeba już przeładowywać całych stron.


### Mikroserwisy 
Rozbicie monolitu na wiele aplikacji i komunikacji pomiędzy nimi

Komunikacja: gRPC (korzysta z HTTP2.x) albo REST API

Systemy rozproszone (distributed systems): 
- każda apka może znajdować się w innej części świata (różne serwery), 
- łatwo się skalują, 
- odporne na awarie, 
- bardziej bezpieczne (jedna pada, inne działają).

ACID Atomicity Consistency Isolation Durability (tj. zarządzanie bazami danych):
- A: możliwe najmniejsze operacje na danych (niepodzielna jednostka), więc ich cofnięcie jest proste.
- C: dane są spójne, brak desynchronizacji. 
- I: każda transakcja jest odseparowana od innych. 
- D: wprowadzone zmiany są trwałe. 

ACID jest trudny w systemach rozproszonych, głównie chodzi o spójność (np. opóźniona synchronizacja).
W takich systemach da się osiągnąć trzy z czterech cech, jedną trzeba poświęcić.

### Django c.d.

Konkurencja do Django:
1. Flask
    - mikroframework, ma tylko niezbędne funkcjonalności, resztę trzeba samemu lub pluginy, daje elastyczność.
2. FastAPI
    - służy do tworzenia API
3. Pyramid
    - mało popularny


Budowa Django:
1. Część konfiguracyjna (settings, router, asgi, wsgi)
2. Django Apps 
    - models.py ORM
    - admin.py CMS
    - views.py logika
    - forms.py DjangoForms (dla monolitu)
    - urls.py router dla konkretnej apki
    - apps.py konfiguracja apki
    - tests.py unittests
    - migrations/ trackowanie zmian w strukturze bazie danych
    - templates/ lokalne templatki dla apki
    - validators.py
    - permissions.py
