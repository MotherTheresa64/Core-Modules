# Define two integer variables
x = 10
y = 5

# Basic arithmetic operations
print("Addition:", x + y)            # 15
print("Subtraction:", x - y)         # 5
print("Multiplication:", x * y)      # 50
print("Division (/):", x / y)        # 2.0 (float result)
print("Floor Division (//):", x // y) # 2 (integer result)
print("Modulus (%):", x % y)         # 0

# Exponentiation
print("Exponentiation (**):", x ** 2)    # 100
print("Using pow():", pow(x, 2))         # 100

# Absolute value
negative_num = -7
print("Absolute value of -7:", abs(negative_num))  # 7

# Rounding numbers
print("Round 3.14:", round(3.14))        # 3
print("Round 3.56:", round(3.56))        # 4

# Type conversion: string to integer
num_str = "123"
num = int(num_str)
print("String to int + 1:", num + 1)     # 124

# Mixed int + float operation
print("3 + 2.0 =", 3 + 2.0)              # 5.0
