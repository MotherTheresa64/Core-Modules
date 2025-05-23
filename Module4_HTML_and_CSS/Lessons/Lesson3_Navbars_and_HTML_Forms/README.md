# Lesson 3: Navigation Bars & HTML Forms

## 🧠 Overview

In this lesson, you'll learn how to build navigation bars and HTML forms — two fundamental tools in web development. Navigation bars help users explore different parts of a site, and forms allow users to submit information like contact details, preferences, and feedback.

---

## 📘 Key Concepts

- `<nav>`, `<ul>`, `<li>`, and `<a>` for creating navigation bars
- href="#id" for linking within a page
- href="file.html" for linking between pages
- Structure of basic and advanced HTML forms
- Common form input types: text, password, email, number, date
- Form groupings using `<fieldset>` and `<legend>`
- HTML5 form attributes like `required`, `placeholder`, `disabled`, and `value`

---

## 📁 Included Files

| Filename           | Description                                      |
|--------------------|--------------------------------------------------|
| `index.html`       | Homepage with navigation and multiple sections   |
| `about.html`       | About page with its own sections and nav         |
| `contact-form.html`| Standalone contact form to collect user input    |

---

## 🎯 Learning Outcomes

By the end of this lesson, you will be able to:

- Create a navigation bar with internal and external links  
- Link to specific sections using `id` references  
- Build HTML forms with text inputs, radio buttons, checkboxes, and more  
- Organize forms using semantic elements like `<fieldset>` and `<legend>`  
- Apply best practices for usability and accessibility  

---

## ⚖️ Navigation Bar Syntax

```html
<nav>
  <ul>
    <li><a href="#home">Home</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>
```

To link to another page:
```html
<a href="about.html">About</a>
```

To link to a section on another page:
```html
<a href="about.html#team">Team</a>
```

---

## 💼 Common Form Elements

```html
<form action="#" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required placeholder="Enter your name">

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>

  <label for="message">Message:</label>
  <textarea id="message" name="message"></textarea>

  <input type="submit" value="Send">
</form>
```

---

## 🔧 Advanced Inputs

- Radio Buttons:
```html
<input type="radio" name="gender" value="male"> Male
<input type="radio" name="gender" value="female"> Female
```

- Checkboxes:
```html
<input type="checkbox" name="hobby" value="reading"> Reading
```

- Dropdown:
```html
<select name="country">
  <option value="usa">United States</option>
</select>
```

- Fieldset:
```html
<fieldset>
  <legend>Personal Info</legend>
  <!-- grouped inputs here -->
</fieldset>
```

---

## 🛠️ Engage & Apply Activities

### 1. Multi-Page Navigation
- Build `index.html` and `about.html`
- Include shared nav bar with links to sections and other pages

### 2. Contact Form
- Create `contact-form.html`
- Collect name, email, message, and submit via a button

### 3. Survey Form (Challenge)
- Use text, radio, checkbox, date, number inputs
- Group sections using `<fieldset>`

---

## ✅ Best Practices

- Use `label` and `for` attributes for accessibility
- Group inputs with `<fieldset>`
- Validate forms using `required`, `type`, and placeholders
- Keep navigation consistent across pages

---

## 🎉 Congratulations!

You built a working multi-page website with nav bars and functional HTML forms! Next up: **Styling your pages with CSS** ➡️