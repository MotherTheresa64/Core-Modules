# Initialize an empty list
books = []

# Get user input
books.append(input("Enter your first favorite book: "))
books.append(input("Enter your second favorite book: "))
books.append(input("Enter your third favorite book: "))

# Sort the list
books.sort()

# Display the sorted list
print("Your favorite books in sorted order:")
print(books)
