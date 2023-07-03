# SQL - Structured Query Language

## Słownik

1. RDBMS - Relational Database Management System
    - serwer z oprogramowaniem (silnik db, storage connection, communication system, user management)
2. ORM - Object Relational Mapper
    - do manipulacji bazą danych i jej strukturą
    - oparte o obiekty i klasy
    - klasa -> tabela, kolumna -> pole klasy, typ kolumny -> definiowany przez obiekt pola klasy, wiersz -> obiekt,
      komórka -> pole obiektu
    - ORM in python -> SQLAlchemy (the best), Django Models
3. DML - Data Manipulation Language
    - podzbiór SQL, zestaw operacji potrafiący manipulować danymi (SELECT, INSERT, UPDATE, DELETE)
4. DDL - Data Definition Language
    - służy do modyfikowania struktury db (tj. schema)
    - np. CREATE, ALTER, DROP
5. DCL - Data Control Language
    - służy do kontrolowania dostępu do danych
    - np. GRANT, REVOKE (nadawanie/usuwanie uprawnień)
6. CRUD - Create Read Update Delete tj. operacje na danych
7. Rodzaje baz danych:
    - Relacyjne bazy danych: dane są podzielone na tabele i posiadają relacje pomiędzy sobą. Postgresql, MySQL, MariaDB,
      Oracle, Microsoft SQL Server, SQLite3, DB2
    - NoSQL (Not only SQL): brak ustalonej struktury/dynamiczna struktura. MongoDB, Redis, Cassandra
    - Hierarchiczne: oparte o strukturę danych drzewa. IMS (Information Management System from IBM). Zazwyczaj używane
      do transakcji.
    - Obiektowe: przechowywanie danych jako obiekty zgrupowane w klasy, trzymają dane i metody. ObjectDB (ObjectDB
      Software -> for Java)
    - Sieciowe: używają grafów, połączenie danych podobne do drzewa. DataStore (Computer Corporation of America, CCA)
8. Rodzaje nośników używanych do baz danych:
    - Dyskowe: trwałe, HDD, SDD, taśmy, BlueRay. Prawie wszystkie relacyjne. 
    - In-memory: oparte o RAM. Szybki zapis/odczyt. Redis, Memcache.
    - Chmurowe: rozproszone po serwerach. Amazon RDS, Google Cloud SQL, Microsoft Azure SQL Database.
    - Mobilne: przystosowane do działania na urządzeniach mobilnych. SQLite3, Realm.
9. Sposoby połączenia: CLI, GUI (DataGrip), język programowania.
10. Wejście do kontenera i bazy danych
```bash 
#service program U user d database h host W prosi o hasło
docker compose exec postgres_db psql -U postgres -d postgres -h localhost -W
# wyświetlanie komend: \?

```




