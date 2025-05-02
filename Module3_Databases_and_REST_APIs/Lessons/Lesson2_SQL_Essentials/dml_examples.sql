-- Insert new records into 'users'
INSERT INTO users (username, email)
VALUES ('john_doe', 'john@example.com'),
       ('jane_doe', 'jane@example.com');

-- Update a record's email
UPDATE users SET email = 'new_email@example.com' WHERE user_id = 1;

-- Delete a specific user
DELETE FROM users WHERE user_id = 2;
