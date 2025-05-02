-- Create the 'customers' table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    address VARCHAR(200),
    PRIMARY KEY (customer_id)
);

-- Insert customers
INSERT INTO customers (name, email, address)
VALUES ('Alice', 'alice@gmail.com', '123 Maple Street'),
       ('Bob', 'bob@gmail.com', '456 Oak Avenue'),
       ('Charlie', 'charlie@yahoo.com', '789 Pine Road');

-- Query customers with Gmail addresses
SELECT * FROM customers WHERE email LIKE '%gmail.com';

-- Update address
UPDATE customers SET address = '999 Cedar Lane' WHERE customer_id = 1;

-- Delete a customer
DELETE FROM customers WHERE customer_id = 3;
