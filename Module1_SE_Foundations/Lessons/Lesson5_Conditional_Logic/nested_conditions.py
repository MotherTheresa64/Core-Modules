# Ask the user for a number
num = int(input("Enter a number: "))

# Check positive/negative and even/odd
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")
