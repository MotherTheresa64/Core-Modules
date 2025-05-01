# Lesson 9: Python Exception Handling – Safeguarding Your Code

## 📌 Overview
This lesson focuses on how to write robust Python programs by using `try`, `except`, `else`, and `finally` blocks to handle errors gracefully. You’ll learn to handle common exceptions like `ZeroDivisionError`, `ValueError`, and create user-friendly error handling experiences.

---

## 🧠 Key Concepts

### ❗ Common Exceptions
- `ZeroDivisionError`: Dividing by zero.
- `ValueError`: Invalid value (e.g., letters instead of numbers).
- `TypeError`: Operation on incompatible data types.

---

### 🔐 Basic Try/Except

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
