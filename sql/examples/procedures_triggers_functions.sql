-- # Procedural language

SELECT *
FROM language;

CREATE PROCEDURE GetLanguage()
    LANGUAGE plpgsql
AS
$$
BEGIN
    PERFORM *
    FROM language;
END;
$$;

CALL GetLanguage();

SELECT current_user;

DROP PROCEDURE GetLanguage();


CREATE OR REPLACE FUNCTION ConcatName(FirstName VARCHAR(100), LastName VARCHAR(100)) RETURNS VARCHAR
    LANGUAGE plpgsql
AS
$$
DECLARE
    FullName VARCHAR(200);
BEGIN
    FullName := FirstName || ' ' || LastName;
    RETURN FullName;
END
$$;

SELECT ConcatName('jarek', 'duck');

DROP PROCEDURE ConcatName(FirstName VARCHAR(100), LastName VARCHAR(100));

CREATE OR REPLACE PROCEDURE GetCustomerDetails(CustomerId INTEGER)
    LANGUAGE plpgsql
AS
$$
DECLARE
    CustomerFirstName VARCHAR(100);
    CustomerLastName  VARCHAR(100);
    CustomerEmail     VARCHAR(200);
BEGIN
    SELECT first_name, last_name, email
    INTO CustomerFirstName, CustomerLastName, CustomerEmail
    FROM customer
    WHERE customer_id = GetCustomerDetails.CustomerId;

    RAISE NOTICE 'Customer data: % %, email: %', CustomerFirstName, CustomerLastName, CustomerEmail;
end;
$$;

CALL GetCustomerDetails(30);


CREATE OR REPLACE PROCEDURE GetRentedFilmsByCustomer(CustomerId INTEGER)
    LANGUAGE plpgsql
AS
$$
DECLARE
    ROW RECORD;
BEGIN
    RAISE NOTICE 'Rented movie: ';
    FOR ROW IN
        (SELECT f.title, r.rental_date
         FROM rental r
                  INNER JOIN inventory i on r.inventory_id = i.inventory_id
                  INNER JOIN film f on i.film_id = f.film_id
         WHERE r.customer_id = CustomerId)
        LOOP
            RAISE NOTICE 'Movie: %, rental date: %.', ROW.title, ROW.rental_date;
        end loop;
END;
$$;

CALL GetRentedFilmsByCustomer(1);

CREATE OR REPLACE FUNCTION UpdateLastUpdatedColumn() RETURNS TRIGGER
AS
$$
BEGIN
    NEW.last_update := NOW();
    RETURN NEW;
END;
$$
    LANGUAGE plpgsql;

CREATE TRIGGER UpdateFilmLastUpdate
    BEFORE INSERT OR UPDATE
    ON film
    FOR EACH ROW
EXECUTE FUNCTION UpdateLastUpdatedColumn();

SELECT *
FROM film
ORDER BY film_id;

UPDATE film
SET replacement_cost = 6.66
WHERE film_id = 1;

ALTER TABLE inventory
    ADD COLUMN availability BOOLEAN;

UPDATE inventory
SET availability = False;


CREATE FUNCTION CheckAvailability() RETURNS TRIGGER
AS
$$
DECLARE
    InventoryCount INTEGER;
BEGIN
    SELECT count(*) INTO InventoryCount
    FROM inventory
    WHERE inventory_id = NEW.inventory_id AND availability = True;

    IF InventoryCount = 0 THEN
        RAISE EXCEPTION 'Not available.';
    end if;
    RETURN NEW;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER CheckInventoryAvailability
    BEFORE INSERT
    ON rental
    FOR EACH ROW
EXECUTE FUNCTION CheckAvailability();


INSERT INTO rental VALUES (100002, NOW(), 367, 130, NOW(), 1, NOW());
