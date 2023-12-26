-- 9-cities_by_state_join.sql
-- Lists all cities in the database hbtn_0d_usa with corresponding state names

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Select cities.id, cities.name, and states.name
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
