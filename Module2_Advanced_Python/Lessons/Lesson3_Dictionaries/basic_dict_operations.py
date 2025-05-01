# Create a basic dictionary
book = {
    'title': '1984',
    'author': 'George Orwell',
    'year': 1949,
    'genre': 'Dystopian'
}

# Add a new key-value pair
book['publisher'] = 'Secker & Warburg'

# Modify an existing value
book['year'] = 1950

# Accessing values safely
print(book.get('title'))  # 1984
print(book.get('isbn', 'Not Available'))  # Key doesn't exist

# Remove using del and pop
del book['genre']
removed = book.pop('publisher')

# Display final dictionary
print(book)
