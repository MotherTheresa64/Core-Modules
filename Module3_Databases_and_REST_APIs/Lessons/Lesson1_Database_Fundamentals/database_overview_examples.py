# database_overview_examples.py

# Example of relational database logic with customers and orders

# Simulated table: Customers
customers = [
    {"CustomerID": 1, "Name": "Alice", "Email": "alice@example.com"},
    {"CustomerID": 2, "Name": "Bob", "Email": "bob@example.com"},
]

# Simulated table: Orders
orders = [
    {"OrderID": 101, "CustomerID": 1, "Total": 59.99},
    {"OrderID": 102, "CustomerID": 1, "Total": 24.99},
    {"OrderID": 103, "CustomerID": 2, "Total": 120.00},
]

# Simulated JOIN: Print orders with customer names
print("Customer Orders:")
for order in orders:
    customer = next(c for c in customers if c["CustomerID"] == order["CustomerID"])
    print(f"Order #{order['OrderID']} by {customer['Name']} — Total: ${order['Total']}")

# Example of NoSQL-style structure (document-based)
document_db = {
    "customers": [
        {
            "CustomerID": 1,
            "Name": "Alice",
            "Orders": [
                {"OrderID": 101, "Total": 59.99},
                {"OrderID": 102, "Total": 24.99},
            ],
        }
    ]
}

print("\nNoSQL-style Document:")
print(document_db["customers"][0])
