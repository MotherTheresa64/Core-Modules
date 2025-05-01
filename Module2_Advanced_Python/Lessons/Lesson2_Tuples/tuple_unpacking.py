# Packing a tuple
person_info = "Alice", 30, "Developer"

# Unpacking the tuple
name, age, profession = person_info
print(name, age, profession)

# Extended unpacking
numbers = (1, 2, 3, 4, 5)

first, *rest = numbers
print("First:", first)
print("Rest:", rest)

*start, last = numbers
print("Start:", start)
print("Last:", last)

# Ignoring values with _
info = ("Eve", 35, "Artist", "New York")
name, _, profession, _ = info
print(name, profession)
