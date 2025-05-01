# Function that squares each number in a list and returns a new list
def square_numbers(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

# Test input
list_of_numbers = [3, 99, 12, 1, 7]

# Call the function and print the result
print(square_numbers(list_of_numbers))
