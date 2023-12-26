-- 0-privileges.sql
-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on localhost

-- Display privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Display privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
