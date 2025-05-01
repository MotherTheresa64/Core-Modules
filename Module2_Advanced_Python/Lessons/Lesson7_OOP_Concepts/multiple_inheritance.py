class Flyer:
    def fly(self):
        print("Flying through the sky!")


class Swimmer:
    def swim(self):
        print("Swimming in the water!")


class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")


donald = Duck()
donald.fly()
donald.swim()
donald.quack()

print(Duck.__mro__)
