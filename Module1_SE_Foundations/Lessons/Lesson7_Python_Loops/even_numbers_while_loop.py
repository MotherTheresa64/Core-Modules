# Program to print all even numbers from 1 to 20 using a while loop

# Step 1: Initialize the starting number
num = 1

# Step 2: Use a while loop to go through numbers from 1 to 20
while num <= 20:
    # Step 3: Check if the number is even
    if num % 2 == 0:
        print(num)
    # Step 4: Increment the number to avoid infinite loop
    num += 1
