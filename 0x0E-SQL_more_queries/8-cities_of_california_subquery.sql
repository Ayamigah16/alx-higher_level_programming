-- 8-cities_of_california_subquery.sql
-- Lists all the cities of California in the database hbtn_0d_usa without using JOIN

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Select cities.id and cities.name for California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
