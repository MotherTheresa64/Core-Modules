# Final Challenge: Tuple Mastery

# Step 1: Create a mixed-data tuple
my_tuple = (10, "Python", 3.14, "Code", 5, "Immutable")

# Step 2: Indexing
print("Third element:", my_tuple[2])
print("Fifth element:", my_tuple[4])

# Step 3: Slicing
sliced_tuple = my_tuple[1:5]
print("Sliced tuple:", sliced_tuple)

# Step 4: Count occurrences
count_code = my_tuple.count("Code")
print("Count of 'Code':", count_code)

# Step 5: Unpacking
a, b, c, d, e, f = my_tuple
print("Unpacked values:", a, b, c, d, e, f)

# Step 6: Concatenation
new_tuple = my_tuple + ("New", "Tuple")
print("Concatenated tuple:", new_tuple)
