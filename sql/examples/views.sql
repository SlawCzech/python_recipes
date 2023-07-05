SELECT * FROM actor ORDER BY actor_id;

CREATE VIEW all_actors
AS
SELECT * FROM actor;

SELECT * FROM all_actors ORDER BY actor_id;

UPDATE actor
SET first_name = 'Peppa'
WHERE actor_id = 1;

DROP VIEW all_actors;