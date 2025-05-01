class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Duck(Animal):
    def speak(self):
        return "Quack!"


def animal_sound(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()
duck = Duck()

animal_sound(dog)
animal_sound(cat)
animal_sound(duck)
