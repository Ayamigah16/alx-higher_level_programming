-- 6-states.sql
-- Creates the database hbtn_0d_usa and the table states on the specified MySQL server

-- Create database hbtn_0d_usa if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create table states if not exists
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Insert data into the states table
INSERT INTO states (name) VALUES
    ('California'),
    ('Arizona'),
    ('Texas');
