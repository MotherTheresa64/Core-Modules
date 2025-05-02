# Lesson 1: Database Fundamentals

## 📌 Overview
This lesson introduces the core concepts of databases, including structured data storage, database management systems (DBMS), data integrity, relational vs. non-relational models, and how ERDs help in designing relational databases.

---

## 🔑 Key Concepts

- What is a database and why they matter
- Structured vs unstructured data
- Tables, rows, and columns
- Relational (SQL) vs Non-relational (NoSQL) databases
- DBMS examples (MySQL, PostgreSQL, MongoDB)
- Data operations: Create, Read, Update, Delete (CRUD)
- Primary vs foreign keys
- ERDs: entities, attributes, relationships, cardinality, and ordinality

---

## 📂 Included Files

| File                          | Purpose                                             |
|-------------------------------|-----------------------------------------------------|
| `database_overview_examples.py` | Demonstrates core DB concepts, ERD logic, and CRUD |

---

## ✅ Learning Outcomes

By completing this lesson, you will:
- Understand what a database is and how it stores data
- Compare relational and non-relational database models
- Recognize the importance of keys and relationships
- Read and interpret ERDs
- Understand real-world use cases and structure of databases

---

## 🧭 ERD Visual Mockup

### Example: One-to-Many — Customers & Orders

```text
+------------+          +------------+
| Customers  |          | Orders     |
+------------+          +------------+
| CustomerID |◄─────────| CustomerID |
| Name       |          | OrderID    |
| Email      |          | Total      |
+------------+          +------------+
       PK                     FK

+---------+           +--------------+           +--------+
| Orders  |           | order_items  |           | Items  |
+---------+           +--------------+           +--------+
| OrderID |◄────────┐ | OrderID      | ┌───────►| ItemID |
| CustID  |         └►| ItemID       |◄────────┘| Name   |
+---------+           +--------------+           | Price  |
     PK                    PK, FK                +--------+
                           PK, FK
