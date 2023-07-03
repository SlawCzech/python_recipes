
## psql

\? - general help
\q - quit
\d - list tables
\d table_name - info o tabeli
\du - info o userach
\dp - info o uprawnieniach


CREATE TABLE my_table (first_col VARCHAR, second_col INTEGER);
INSERT INTO my_table (first_col, second_col) VALUES ('kasia', 18);

CREATE USER saek WITH PASSWORD 'pass';
ALTER USER saek SUPERUSER;
GRANT SELECT ON my_table TO saek;
GRANT INSERT ON my_table TO saek;
GRANT DELETE ON my_table TO saek;
REVOKE DELETE ON my_table FROM saek;


SELECT * FROM my_table;

DELETE FROM my_table WHERE second_col = 18;

CREATE USER jarek;

ALTER USER jarek WITH PASSWORD 'elo';

GRANT SELECT ON my_table TO jarek;

