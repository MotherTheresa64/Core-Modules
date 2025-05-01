import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Provide feedback
if guess == secret_number:
    print("Congratulations, You guessed the secret number!")
elif guess < secret_number:
    print("Too low!")
else:
    print("Too high!")
