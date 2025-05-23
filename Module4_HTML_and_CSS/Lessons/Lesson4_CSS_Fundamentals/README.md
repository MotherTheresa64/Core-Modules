# Lesson 4: CSS Fundamentals

## 📄 Overview
In this lesson, you'll learn how to style your HTML pages using CSS (Cascading Style Sheets). CSS allows you to control the visual appearance of your webpages including color, layout, fonts, spacing, and responsiveness. You’ll also explore the CSS Box Model, selectors, and pseudo-classes to make your pages more dynamic and engaging.

---

## 🧪 Key Concepts

### ✨ CSS Syntax
```css
selector {
  property: value;
}
```
- **Selector** targets HTML elements
- **Property** defines what to style
- **Value** sets how to style it

### Types of CSS
- **Inline CSS**: Uses `style` attribute directly in HTML
- **Internal CSS**: Uses `<style>` in `<head>`
- **External CSS**: Links to a `.css` file (preferred)

### CSS Selectors
- **Element selector** (`p`) — styles all `<p>` tags
- **Class selector** (`.classname`) — styles elements with that class
- **ID selector** (`#idname`) — styles a unique element by ID
- **Group selector** (`h1, h2, p`) — styles multiple tags
- **Descendant selector** (`div p`) — selects nested elements
- **Child selector** (`div > p`) — selects direct child elements

### Pseudo-classes
- `:hover`, `:focus`, `:active`, `:first-child`, `:last-child`, `:nth-child()`

---

## 📁 Included Files

| Filename     | Description                                  |
|--------------|----------------------------------------------|
| `index.html` | Sample page with semantic HTML structure      |
| `styles.css` | External CSS file applying lesson techniques |

---

## 🎯 Learning Outcomes
By the end of this lesson, you will be able to:

- Understand the role of CSS in web development
- Write and link internal and external CSS
- Use various CSS selectors and apply styles
- Implement the box model and spacing principles
- Enhance UI with pseudo-classes like `:hover` and `:focus`

---

## 🔍 CSS Box Model

Every HTML element is treated as a box:
- **Content**: Actual element data
- **Padding**: Space around content
- **Border**: Wraps the padding
- **Margin**: Space outside the element

Example:
```css
.box {
  width: 200px;
  padding: 20px;
  border: 2px solid black;
  margin: 30px;
}
```

---

## 🤖 Learn & Engage: Basic External Styling

### Step 1: Create an `index.html` file
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Styled Webpage</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <h1>Welcome to My Webpage</h1>
  <p>This is a paragraph of text.</p>
  <div class="container">
    <p>This paragraph is inside a div.</p>
  </div>
</body>
</html>
```

### Step 2: Create `styles.css`
```css
h1 {
  color: darkblue;
  text-align: center;
}

p {
  color: green;
  font-size: 18px;
}

.container {
  background-color: lightgray;
  padding: 20px;
  border: 1px solid black;
}
```

---

## 🤖 Wrap-Up Challenge: Personal Styling
Apply these in `styles.css`:

```css
body {
  background-color: beige;
  font-family: Arial, sans-serif;
}

a {
  color: blueviolet;
  text-decoration: none;
}

a:hover {
  color: green;
}

.content {
  padding: 20px;
  border: 1px solid black;
  border-radius: 5px;
  background-color: lightgray;
}
```

---

## ✅ Best Practices
- Use **external stylesheets** for reusable styles
- Use **class selectors** for grouping styles
- Use **semantic HTML** with scoped CSS classes
- Keep CSS organized and well-indented

---

## 🎉 Congratulations!
You've now mastered the foundations of CSS styling. In the next lesson, you’ll dive deeper into layout, positioning, and how to build responsive designs!

Next Lesson: CSS Layout and Positioning ➡️