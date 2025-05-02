# Lesson 3: Intro to ORMs

## 📌 Overview
This lesson introduces Object-Relational Mapping (ORM), which allows Python developers to interact with relational databases using object-oriented syntax. You'll learn how to define models, perform basic CRUD operations, and represent relationships between tables using SQLAlchemy 2.0.

---

## 🔑 Key Concepts

- What is an ORM and why use one
- SQLAlchemy 2.0 setup and virtual environments
- Defining models as Python classes
- Performing CRUD operations using SQLAlchemy sessions
- One-to-Many and Many-to-Many relationships with SQLAlchemy

---

## 📂 Included Files

| File                      | Purpose                                                              |
|---------------------------|----------------------------------------------------------------------|
| `sqlalchemy_setup.py`     | Boilerplate code to connect to a MySQL database using SQLAlchemy     |
| `models_one_to_many.py`   | Example of a one-to-many relationship (User → Pets)                  |
| `models_many_to_many.py`  | Example of a many-to-many relationship (Users ⇄ Pets)                |
| `relationship_examples.py`| Code snippets that demonstrate inserting and querying related models |

---

## ✅ Learning Outcomes

By completing this lesson, you will:
- Set up SQLAlchemy to work with a MySQL database
- Define Python classes as database models
- Use sessions to create, read, update, and delete data
- Build one-to-many and many-to-many relationships between models
- Understand how to use SQLAlchemy relationships to simplify complex queries
