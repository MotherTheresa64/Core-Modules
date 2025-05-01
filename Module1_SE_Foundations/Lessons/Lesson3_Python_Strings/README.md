# Lesson 3: Mastering Python Strings

## 📌 Overview
This lesson covers the fundamentals of Python strings including creation, indexing, slicing, manipulation using methods, formatting, and common pitfalls. Strings are a core part of Python programming and essential for processing text data.

---

## 🧠 Key Concepts

### 🔤 String Basics

- **Creating Strings**: Enclose text in single (`'`) or double (`"`) quotes.
- **Multiline Strings**: Use triple quotes (`'''` or `"""`).
- **Indexing**: `word[0]` gives the first character.
- **Slicing**: `word[0:3]` returns a substring.

### ⚙️ String Operations

- **Concatenation**: `'Hello ' + 'World'`
- **Repetition**: `'Ha' * 3` → `'HaHaHa'`
- **Length**: `len("Python")` → `6`

---

## 🧪 String Methods (see `string_methods_demo.py`)
| Method        | Description                            |
|---------------|----------------------------------------|
| `.upper()`    | Converts to uppercase                  |
| `.lower()`    | Converts to lowercase                  |
| `.strip()`    | Trims whitespace                       |
| `.replace()`  | Replaces part of a string              |
| `.split()`    | Splits string into a list              |
| `.join()`     | Joins a list into a string             |
| `.startswith()` / `.endswith()` | Checks how a string begins or ends |

---

## 🧠 Practice Activity
```python
my_string = '            Coding temple is the best bootcamp ever!      '
