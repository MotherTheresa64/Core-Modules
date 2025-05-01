class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}!"

    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! You are now {self.age} years old."

# Example usage
person1 = Person("Alice", 25)
print(person1.greet())
print(person1.have_birthday())
