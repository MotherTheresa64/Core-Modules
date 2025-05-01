# Dictionary of users with nested details
users = {
    'user1': {
        'name': 'Alice',
        'age': 25,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'zipcode': '10001'
        }
    },
    'user2': {
        'name': 'Bob',
        'age': 30,
        'address': {
            'street': '456 Elm St',
            'city': 'San Francisco',
            'zipcode': '94107'
        }
    }
}

# Access nested data
print(users['user1']['address']['city'])

# Modify nested data
users['user2']['address']['zipcode'] = '94109'

# Add new nested value
users['user1']['phone'] = '555-1234'

# Loop through nested dictionary
for user, info in users.items():
    print(f"User ID: {user}")
    for key, value in info.items():
        print(f"  {key}: {value}")
