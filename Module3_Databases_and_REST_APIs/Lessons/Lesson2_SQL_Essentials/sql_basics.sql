-- Create a new database
CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

-- Create a 'users' table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id)
);

-- Alter the 'users' table to add a new column
ALTER TABLE users ADD last_login TIMESTAMP;

-- Modify an existing column
ALTER TABLE users MODIFY email VARCHAR(150) NOT NULL;

-- Drop a table (irreversible!)
-- DROP TABLE users;
