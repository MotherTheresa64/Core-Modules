# Ask the user for weather and mood input
weather = input("What is the weather like? (sunny/raining): ").lower()
mood = input("How are you feeling? (happy/tired): ").lower()

# Conditional logic to suggest an activity
if weather == "sunny":
    if mood == "happy":
        print("Go for a hike!")
    else:
        print("Relax indoors.")
elif weather == "raining":
    print("Relax indoors.")
else:
    print("Invalid input. Try sunny or raining.")
