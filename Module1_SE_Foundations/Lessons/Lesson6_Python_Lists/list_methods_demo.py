# Create a list of numbers
numbers = [4, 1, 7, 3]

# Sort the list
numbers.sort()
print("Sorted:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed:", numbers)

# Extend one list with another
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print("Extended list:", list1)

# Concatenate lists using +
combined = list1 + ["extra", 99]
print("Concatenated:", combined)

# Nested list example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix element [0][1]:", matrix[0][1])
