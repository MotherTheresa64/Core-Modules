# Creating a tuple with different data types
my_tuple = (42, "hello", 3.14, True)

# Accessing elements by index
print("First element:", my_tuple[0])     # Output: 42
print("Last element:", my_tuple[-1])     # Output: True

# Slicing the tuple
sliced = my_tuple[1:3]
print("Sliced tuple (index 1 to 2):", sliced)  # Output: ('hello', 3.14)

# Attempting to modify a tuple element (will raise TypeError)
try:
    my_tuple[1] = "world"
except TypeError as e:
    print("Error: Tuples are immutable.")
    print("Exception:", e)

# Confirming original tuple is unchanged
print("Original tuple:", my_tuple)
