import random

first_names = ["Christian", "Dylan", "Travis", "Katelyn"]
last_names = ["Sachs", "Katina", "Peck", "Mehner"]

first = random.choice(first_names)
last = random.choice(last_names)

full_name = f"{first} {last}"
print("Generated Name:", full_name)
