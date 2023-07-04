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
#docker compose exec service program U user d database h host W prosi o hasło
docker compose exec postgres_db psql -U postgres -d postgres -h localhost -W
# wyświetlanie komend: \?

```
---
## FULL CRUD:

## SELECT
Full select in correct order.
```sql
SELECT column1, column2 
FROM table_name
WHERE condition 
GROUP BY column1
HAVING condition
WINDOW window_name AS (PARTITION BY column1 ORDER BY column2) 
UNION 
SELECT column3, column4
FROM table2
ORDER BY column3
LIMIT 10
OFFSET 5
FOR UPDATE;
```

1. Select -> kolumny lub wyniki (np. CONCAT(), AVG() itp.), które mają być zwrócone.
2. From -> tabela lub zestaw tabel.
3. Where -> filtrowanie wierszy.
4. Group by -> grupowanie po wierszach. 
5. Having -> filtrowanie grup wynikowych. 
6. Window -> do funkcji analitycznych.
7. Union/Intersect/Except -> łączenie wyników z kilku zapytań.
8. Order by -> sortowanie. 
9. Limit -> liczba wyników.
10. Offset -> ile wierszy pomija, przesunięcie.
11. For Update/For Share -> blokuje wybrane wiersze w celu modyfikacji. 


## INSERT

```sql
INSERT INTO table_name (column1, column2, column3) 
VALUES (value1, value2, value3)
RETURNING column1, column2;
```

1. Insert Into -> wskazuje na tabelę, do której dodajemy dane.
2. column list (optional) -> lista kolumn do wypełnienia
   - można opuścić column list, jeżeli wypełniamy wszystkie kolumny tabeli
3. Values -> wartości pozycyjne do wstawienia, może ich być wiele (od razu na kilka wierszy, taki bulk_insert)
4. Returning (optional) -> zwraca dane (wiersze), które dodaliśmy, np. żeby pozyskać id


## UPDATE 

```sql
UPDATE table_name 
SET column1 = new_value, column2 = new_value_2
FROM other_table 
WHERE table_name.column3 = other_table.column3
RETURNING column1, column2;
```

1. Update -> wskazuje na tabelę do modyfikacji
2. Set -> wskazuje na kolumny i nowe wartości do aktualizacji
3. From (optional) -> wskazuje na inną tabelę, z której weźmiemy dane do aktualizacji
4. Where (optional) -> określam które wiersze są do modyfikacji
5. Returning (optional) -> zwraca dane (wiersze), które dodaliśmy, np. żeby pozyskać id


## DELETE

```sql
DELETE FROM table_name
USING other_table
WHERE table_name.column1 = other_table.column1
RETURNING column1, column2;
```

1. Delete From -> wskazuje na tabelę, z które będziemy coś usuwać
2. Using (optional) -> wskazuje na tabelę, z której będziemy używać dane, po których będziemy usuwać z pierwsze tabeli
3. Where -> wskazuje wiersze do usunięcia
4. Returning (optional) -> zwraca dane (wiersze), które usunęliśmy


---

## CREATE TABLE

```sql
CREATE TABLE IF NOT EXISTS table_name(
    column1 datatype constraints, 
    column2 datatype constraints 
);

CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,  
    last_name VARCHAR(30) NOT NULL, 
    age INTEGER,
    department_id INTEGER REFERENCES departments(id), 
    hire_date DATE DEFAULT CURRENT_DATE 
);
```

1. Create Table -> klauzula rozpoczynająca tworzenie tabeli
2. If Not Exists -> nie powoduje błędu jeśli tabela istnieje, ale nie tworzy nowej
3. column_1, column_2, column_n -> nazwy kolumn
4. datatype -> typ kolumny, np. varchar, boolean, integer etc.
5. constraints (optional) -> ograniczenia, np. foreign key, unique, not null, etc.


## DROP TABLE

```sql
DROP TABLE IF EXISTS table_name;
```

## ALTER TABLE


```sql
ALTER TABLE table_name 
    action_1, 
    action_2,
    action_n;
    

ALTER TABLE employees
    ADD COLUMN email VARCHAR(100),
    ALTER COLUMN age SET DEFAULT 0,
    DROP COLUMN department_id;


ALTER TABLE table_name RENAME TO staff;  # zmieni nazwę tabeli
```

---

## DCL - Data Controlled Language

## GRANT/REVOKE

```sql
GRANT SELECT, INSERT, UPDATE ON table_name TO user_name;

GRANT ALL ON table_name TO user_name; # daje wszystkie uprawnienia
```


## JOINS

1. Inner Join -> intersection, przecięcie tabel dla których spełniony jest warunek.
2. Left Join/Left Outer Join -> cała tabela pierwsza i dopasowania z drugiej.
3. Right Join/Right Outer Join -> cała tabela druga i dopasowania z pierwszej.
4. Full Join/Full Outer Join -> cała tabela pierwsze i dopasowania + cała tabela druga i dopasowania.
5. Self Join -> połączenie danych z wielu kolumn z jednej tabeli.
6. Cross Join/Cartesian Join -> iloczyn kartezjański z dwóch tabel, tj. każdy rekord z każdym

Bonusy: 
- Natural Join (połączenie na podstawie kolumn o tych samych nazwach), 
- Theta Join (łączenie na podstawie dowolnego warunku logicznego).