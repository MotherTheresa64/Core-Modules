# Dictionary with list values
favorite_books = {
    'Alice': ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice'],
    'Bob': ['The Great Gatsby', 'Catch-22', 'Moby Dick'],
    'Charlie': ['The Hobbit', 'Harry Potter', 'War and Peace']
}

# Accessing a list inside a dictionary
print(favorite_books['Alice'])
print(favorite_books['Bob'][1])  # Catch-22

# Looping through lists inside dictionary
for person, books in favorite_books.items():
    print(f"{person}'s favorite books:")
    for book in books:
        print(f" - {book}")
