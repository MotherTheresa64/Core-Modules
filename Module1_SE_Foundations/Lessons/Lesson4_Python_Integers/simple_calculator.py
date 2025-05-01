# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Handle division by zero
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero.")
