# Global variable
x = 10

def print_local():
    x = 5  # Local variable
    print("Inside function:", x)

# Call the function
print_local()

# Outside the function
print("Outside function:", x)
