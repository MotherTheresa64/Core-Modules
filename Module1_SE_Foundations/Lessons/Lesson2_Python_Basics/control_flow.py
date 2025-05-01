# Ask user for their age
age = int(input("Enter your age: "))

if age > 0 and age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
