# 🛒 E-Commerce API Project

**Author:** Noah Ragan  
**Date:** May 19th, 2025

---

## 📋 Overview

This project is a RESTful E-Commerce API built using **Flask**, **SQLAlchemy**, **Marshmallow**, and **MySQL**. The API manages **Users**, **Products**, and **Orders**, including full CRUD operations and proper database relationships like **One-to-Many** (Users → Orders) and **Many-to-Many** (Orders ↔ Products).

---

## 🚀 Features

- ✅ User CRUD (Create, Read, Update, Delete)
- ✅ Product CRUD
- ✅ Order creation tied to a user
- ✅ Add/remove products to/from orders
- ✅ View all orders for a user
- ✅ View all products in an order
- ✅ Input validation with Marshmallow
- ✅ MySQL for data persistence
- ✅ Manual testing with Postman

---

## ⚙️ Technologies Used

- Python 3.11
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- Marshmallow-SQLAlchemy
- MySQL (`mysql-connector-python`)
- Postman

---

## 🗃 Database Models

### User
- `id` (Primary Key)
- `name` (String)
- `address` (String)
- `email` (String, unique)

### Product
- `id` (Primary Key)
- `product_name` (String)
- `price` (Float)

### Order
- `id` (Primary Key)
- `order_date` (DateTime)
- `user_id` (ForeignKey to User)

### Order_Product (Association Table)
- `order_id` (ForeignKey to Order)
- `product_id` (ForeignKey to Product)

---

## 📦 API Endpoints

### 🧍‍♂️ Users
| Method | Endpoint          | Description                |
|--------|-------------------|----------------------------|
| GET    | `/users`          | Get all users              |
| GET    | `/users/<id>`     | Get a specific user        |
| POST   | `/users`          | Create a new user          |
| PUT    | `/users/<id>`     | Update an existing user    |
| DELETE | `/users/<id>`     | Delete a user              |

### 📦 Products
| Method | Endpoint             | Description               |
|--------|----------------------|---------------------------|
| GET    | `/products`          | Get all products          |
| GET    | `/products/<id>`     | Get a specific product    |
| POST   | `/products`          | Create a new product      |
| PUT    | `/products/<id>`     | Update an existing product|
| DELETE | `/products/<id>`     | Delete a product          |

### 📦 Orders
| Method | Endpoint                                         | Description                        |
|--------|--------------------------------------------------|------------------------------------|
| POST   | `/orders`                                        | Create a new order                 |
| PUT    | `/orders/<order_id>/add_product/<product_id>`    | Add product to an order            |
| DELETE | `/orders/<order_id>/remove_product/<product_id>` | Remove product from an order       |
| GET    | `/orders/user/<user_id>`                         | Get all orders for a user          |
| GET    | `/orders/<order_id>/products`                    | Get all products in a specific order |

---

## 💾 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ecommerce-api
cd ecommerce-api
