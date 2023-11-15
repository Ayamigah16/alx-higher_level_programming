-- 16-no_link.sql

-- Listing records from the second_table excluding rows without a name value, ordered by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
