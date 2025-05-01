class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"

    def __str__(self):
        return f"{self.name}: ${self.price} (Quantity: {self.quantity})"


# Developer view
p = Product("Laptop", 999.99, 5)
print(repr(p))  # Product(name='Laptop', price=999.99, quantity=5)

# User view
print(p)  # Laptop: $999.99 (Quantity: 5)
