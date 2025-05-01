# Handling multiple exceptions in different ways

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"Success! Result is: {result}")
finally:
    print("Program has finished running.")
