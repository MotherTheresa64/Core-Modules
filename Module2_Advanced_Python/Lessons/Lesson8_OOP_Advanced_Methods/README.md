# Lesson 8: Advanced OOP Methods (Optional)

## 📌 Overview
This optional lesson explores advanced class features in Python OOP: special (dunder) methods like `__repr__` and `__str__`, `@classmethod` for class-level behavior, and `@staticmethod` for utility functions. These tools provide more control, flexibility, and expressiveness in object-oriented design.

---

## 🔑 Key Concepts

- **__repr__ vs __str__**: Debug vs user-friendly string output
- **@classmethod**: Operate at the class level (e.g., alternative constructors)
- **@staticmethod**: Attach utility functions to classes that don't modify or depend on instance/class state

---

## 📂 Included Files

| File                    | Purpose                                                        |
|-------------------------|----------------------------------------------------------------|
| `product_repr_str.py`   | Demonstrates `__repr__` and `__str__` for a Product class       |
| `car_classmethods.py`   | Shows `@classmethod` for tracking car production and CSV input  |
| `weather_station_static.py` | Uses `@staticmethod` to convert between Fahrenheit and Celsius |

---

## ✅ Learning Outcomes

By completing this lesson, you will:
- Customize how your objects are printed or represented in code
- Use class methods for alternative constructors and shared class logic
- Use static methods for reusable, context-related utility functions
