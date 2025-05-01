class Car:
    total_cars = 0  # Class attribute

    def __init__(self, model, year):
        self.model = model
        self.year = year
        Car.total_cars += 1

    @classmethod
    def from_csv(cls, csv_data):
        model, year = csv_data.split(',')
        return cls(model, int(year))

    @classmethod
    def total_produced(cls):
        return cls.total_cars


# Test
car1 = Car("Toyota Corolla", 2020)
car2 = Car.from_csv("Honda Accord,2018")
print(Car.total_produced())  # Output: 2
