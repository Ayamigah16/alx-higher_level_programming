-- 3-force_name.sql
-- Creates the table force_name on the specified MySQL database

-- Create table force_name if not exists
USE hbtn_0d_2;

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
