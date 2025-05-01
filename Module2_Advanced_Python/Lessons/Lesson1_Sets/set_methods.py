# Create and modify a set
foods = {'pizza', 'sushi', 'pasta', 'ice cream'}
foods.add('burger')

# Membership test
print('pasta' in foods)
print(foods)

# Compare sets
set1 = {'basketball', 'soccer', 'tennis'}
set2 = {'basketball', 'soccer'}

print("Subset:", set2.issubset(set1))
print("Superset:", set1.issuperset(set2))

# Set operations
vacay1 = {'Paris', 'Tokyo', 'New York'}
vacay2 = {'London', 'Paris', 'Rome'}

print("Union:", vacay1.union(vacay2))
print("Intersection:", vacay1.intersection(vacay2))
print("Difference:", vacay1.difference(vacay2))
print("Symmetric Difference:", vacay1.symmetric_difference(vacay2))
