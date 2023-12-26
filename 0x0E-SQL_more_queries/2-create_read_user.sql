-- 2-create_read_user.sql
-- Creates the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege

-- Create database hbtn_0d_2 if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user user_0d_2 if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant USAGE privilege on all databases to user_0d_2
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- Grant SELECT privilege on hbtn_0d_2 database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
