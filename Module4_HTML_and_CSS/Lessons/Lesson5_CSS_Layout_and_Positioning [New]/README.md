# Lesson 5: CSS Layout and Positioning

## 📄 Overview
In this lesson, you'll learn how to control the visual structure and alignment of your web pages using layout and positioning tools in CSS. Layout is fundamental to user experience: it ensures that elements are logically arranged and visually appealing across different screen sizes.

---

## 🧪 Key Concepts

### Block vs. Inline Elements
- **Block Elements**: Take up full width and start on a new line. Ex: `<div>`, `<p>`, `<h1>`
- **Inline Elements**: Sit inline with other content. Ex: `<span>`, `<a>`, `<strong>`

### The `display` Property
Controls how elements are rendered:
- `block`
- `inline`
- `inline-block`
- `none`

### Spacing: Margin, Padding, Border
- **Margin**: Space outside the element
- **Padding**: Space inside the element between content and border
- **Border**: The visible edge of the element

### The `position` Property
- `static`: default
- `relative`: offset relative to normal position
- `absolute`: positioned relative to nearest non-static ancestor
- `fixed`: stays in place on scroll
- `sticky`: toggles between relative and fixed based on scroll

### Float
- `float: left` or `float: right` allows side-by-side positioning
- Requires clearfix technique or modern layout replacements like Flexbox

### Flexbox (Intro Level)
- `display: flex` creates a flex container
- `justify-content`, `align-items` control layout direction and spacing

---

## 📁 Included Files
| Filename                | Description                                 |
|-------------------------|---------------------------------------------|
| `two_column_layout.html` | Float-based two-column layout example       |
| `two_column_layout.css`  | CSS file for two-column float styling       |
| `resume_layout.html`     | Challenge: Resume layout using float/flex   |
| `resume_layout.css`      | CSS for resume layout styling               |

---

## 🎯 Learning Outcomes
By the end of this lesson, you will be able to:
- Distinguish between block and inline elements
- Use `display` and `position` to control element layout
- Apply margin, padding, and border for visual spacing
- Create two-column layouts using float
- Use Flexbox to align and space content

---

## 🔧 Engage & Apply

### Example: Two-Column Layout with Floats
```html
<div class="container">
  <div class="left-column">Left Content</div>
  <div class="right-column">Right Content</div>
</div>
```
```css
.container {
  width: 100%;
}

.left-column {
  float: left;
  width: 50%;
  background-color: #f0f0f0;
  padding: 20px;
}

.right-column {
  float: right;
  width: 50%;
  background-color: #ddd;
  padding: 20px;
}
```

---

## 🔮 Practice Challenge: Resume Layout
Create a simple resume layout:
- **Left Column**: Name and Contact Info
- **Right Column**: Experience and Education
- Use `float` or `Flexbox`
- Add padding, margin, and border to distinguish sections

---

## ✅ Best Practices
- Use **Flexbox** for flexible, responsive layouts
- Avoid using floats for major layouts when possible
- Always clear floats or use layout-safe methods like Flexbox/Grid
- Use spacing (padding/margin) to improve visual hierarchy
- Use semantic HTML tags to help structure your layout

---

## 🎉 Congratulations!
You've completed Lesson 5: CSS Layout and Positioning. You've learned how to organize page content effectively using floats, position properties, and the fundamentals of Flexbox.

Next Lesson: (Second Lesson 5) Advanced CSS and Responsive Design ➡️