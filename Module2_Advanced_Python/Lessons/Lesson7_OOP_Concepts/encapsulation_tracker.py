class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name  # Public attribute
        self.__steps = 0            # Private attribute
        self.__calories = 0.0       # Private attribute

    def add_steps(self, steps):
        if steps > 0:
            self.__steps += steps
            print(f"Added {steps} steps. Total: {self.__steps}")

    def get_steps(self):
        return self.__steps

    def add_calories(self, cal):
        if cal > 0:
            self.__calories += cal
            print(f"Added {cal} calories. Total: {self.__calories}")

    def get_calories(self):
        return self.__calories

    def reset(self):
        self.__steps = 0
        self.__calories = 0.0
        print("Tracker reset.")


tracker = FitnessTracker("John")
tracker.add_steps(3000)
tracker.add_calories(200)
print(tracker.get_steps())
print(tracker.get_calories())
