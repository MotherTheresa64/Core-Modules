# List of dictionaries
students = [
    {'name': 'Alice', 'age': 25, 'major': 'Physics'},
    {'name': 'Bob', 'age': 22, 'major': 'Computer Science'},
    {'name': 'Charlie', 'age': 23, 'major': 'Mathematics'}
]

# Access and loop
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# Accessing specific item
print(students[0]['major'])  # Output: Physics
