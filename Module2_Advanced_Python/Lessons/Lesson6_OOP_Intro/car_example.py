class Car:
    wheels = 4  # Class attribute shared by all instances

    def __init__(self, make, model):
        self.make = make      # Instance attribute
        self.model = model    # Instance attribute

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(f"{car1.make} {car1.model} with {car1.wheels} wheels")
print(f"{car2.make} {car2.model} with {car2.wheels} wheels")
