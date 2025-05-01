# Step 1: Define the initial list
fruits = ["apple", "banana", "cherry", "date"]

# Step 2: Accessing elements
print("First fruit:", fruits[0])       # Expected: "apple"
print("Last fruit:", fruits[-1])       # Expected: "date"

# Step 3: Add and insert items
fruits.append("elderberry")
print("After append:", fruits)         # Expected: [..., "elderberry"]

fruits.insert(1, "blueberry")
print("After insert:", fruits)         # Expected: "blueberry" at index 1

# Step 4: Remove items
fruits.remove("banana")
print("After remove:", fruits)         # Expected: "banana" removed

del fruits[0]
print("After delete:", fruits)         # Expected: "apple" (index 0) removed

# Step 5: Slice the list
# Should now be: ["blueberry", "cherry", "date", "elderberry"]
citrus_fruits = fruits[1:3]            # Slicing index 1 to 2
print("Citrus fruits:", citrus_fruits) # Expected: ["cherry", "date"]
