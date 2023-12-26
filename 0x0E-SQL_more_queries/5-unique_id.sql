-- 5-unique_id.sql
-- Creates the table unique_id on the specified MySQL database

-- Create table unique_id if not exists
USE hbtn_0d_2;

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
