-- 4-never_empty.sql
-- Creates the table id_not_null on the specified MySQL database

-- Create table id_not_null if not exists
USE hbtn_0d_2;

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
