
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


SELECT * FROM postgres.public.my_table;

INSERT INTO my_table (first_col, second_col) VALUES ('basia', 20) RETURNING first_col, second_col;

DELETE FROM my_table WHERE first_col = 'basia' RETURNING first_col;

ALTER TABLE my_table RENAME TO fancy_name;

ALTER TABLE fancy_name
    ADD COLUMN id SERIAL PRIMARY KEY;

SELECT * FROM postgres.public.fancy_name;

ALTER TABLE fancy_name
    RENAME COLUMN first_col TO nick;

ALTER TABLE fancy_name
    RENAME COLUMN second_col TO score;

SELECT * FROM postgres.public.fancy_name;

INSERT INTO fancy_name
    VALUES ('basia', 10), ('tomek', 23), ('misiek', 5);

UPDATE fancy_name SET score = 10 WHERE nick = 'misiek';

SELECT fn.score, COUNT(*)
FROM fancy_name AS fn
GROUP BY fn.score;

SELECT score, count
FROM (
  SELECT fn.score, COUNT(*) AS count
  FROM fancy_name AS fn
  GROUP BY fn.score
) subquery
WHERE count > 1;

WITH grouped_players AS (
  SELECT score, COUNT(*) AS count
  FROM fancy_name
  GROUP BY score
)
SELECT score, count
FROM grouped_players
WHERE count > 1;

GRANT ALL ON fancy_name TO jarek;

GRANT SELECT ON fancy_name TO jarek WITH GRANT OPTION;

SELECT grantor, table_schema, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE grantee = 'jarek';
