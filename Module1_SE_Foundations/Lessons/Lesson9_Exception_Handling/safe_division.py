# Program to safely divide two user-provided numbers
# Handles invalid input and division by zero using exception handling

try:
    # Prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform division
    result = num1 / num2

except ValueError:
    # Handles non-numeric input
    print("Invalid input. Please enter numeric values.")

except ZeroDivisionError:
    # Handles division by zero
    print("You can't divide by zero!")

else:
    # Executes only if no exception was raised
    print(f"The result is: {result}")

finally:
    # Always runs, no matter what
    print("Thank you for using the division tool.")
