-- Regular inserts + select
INSERT INTO force_name (id, name) VALUES (1, "Holberton School");
INSERT INTO force_name (id, name) VALUES (2, "Holberton");
INSERT INTO force_name (id, name) VALUES (3, "School");
INSERT INTO force_name (id, name) VALUES (4, "C is fun");
INSERT INTO force_name (id, name) VALUES (1, "Python is cool");

SELECT * FROM force_name ORDER BY id, name ASC;
