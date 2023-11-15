-- 11-best_score.sql

-- Listing records from the second_table with a score >= 10 ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
