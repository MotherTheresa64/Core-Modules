-- Select all users
SELECT * FROM users;

-- Select specific columns
SELECT username, email FROM users;

-- Filter results with WHERE
SELECT * FROM users WHERE username = 'john_doe';

-- Sort by newest users
SELECT * FROM users ORDER BY created_at DESC;

-- Pattern match using LIKE
SELECT * FROM users WHERE email LIKE '%example.com';
