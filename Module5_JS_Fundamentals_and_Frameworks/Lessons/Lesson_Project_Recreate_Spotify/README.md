# 🎵 Spotify Recreate – Bootstrap & JavaScript Project

This project is a responsive recreation of a Spotify-inspired webpage, completed as part of **Module 5: JavaScript Fundamentals & Frameworks** for the Coding Temple Software Engineering program. It demonstrates proficiency in Bootstrap layout, components, responsive design, forms, utility classes, and JavaScript fundamentals including DOM manipulation and event handling.

---

## 📁 Project Structure

Lesson_Project_Recreate_Spotify/
│
├── assets/
│ ├── background.jpg # Hero banner image
│ ├── user.png # Rounded-circle avatar
│ ├── spotify-logo-yellow.png # Footer logo
│ ├── spotify-logo-white.png # Navbar logo
│
├── index.html # Main HTML file
├── styles.css # Custom styling
├── script.js # JavaScript logic
└── README.md # Project description


---

## 🖥️ Live Preview

Features include:
- Hero banner and branding
- Responsive registration form with validation
- User data table with hardcoded entries
- Responsive images using `img-fluid` and `rounded-circle`
- Utility button examples (including responsive visibility)
- Fully responsive Bootstrap navbar

---

## ✅ Bootstrap Components & Utilities Used

| Feature | Usage |
|--------|-------|
| **Navbar** | Responsive `navbar-expand-md`, collapses into hamburger menu |
| **Form** | Inputs for name, email, password, checkbox, validation classes, `btn-success` submit |
| **Table** | `table`, `table-striped`, `table-hover`, wrapped in `table-responsive` |
| **Images** | `img-fluid` hero image and `rounded-circle` avatar |
| **Buttons** | Utility classes: `d-none d-md-block`, `btn`, `btn-primary`, etc. |
| **Layout** | Containers, rows, columns using Bootstrap Grid system |

---

## 🧠 JavaScript Functionality

The form submission is handled with JavaScript. It validates required fields and displays a success or error message:

```js
document.addEventListener('DOMContentLoaded', () => {
  const feedbackForm = document.getElementById('feedback-form');
  const messageArea = document.getElementById('message-area');

  feedbackForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const name = feedbackForm.elements['name'].value;
    const email = feedbackForm.elements['email'].value;
    const message = feedbackForm.elements['message'].value;

    if (name && email && message) {
      feedbackForm.reset();
      messageArea.textContent = "✅ Feedback submitted successfully!";
      messageArea.style.color = "#1DB954";
    } else {
      messageArea.textContent = "⚠️ Please fill out all fields.";
      messageArea.style.color = "#ff4d4d";
    }
  });
});
```



## 📱 Responsiveness & Layout
Bootstrap’s grid system ensures consistent layout across desktop, tablet, and mobile.

Custom CSS tweaks style and spacing while retaining responsiveness.

Form fields adapt to screen width and table reflows gracefully.



## 🚀 How to Run Locally
Clone this repository or download the folder.

Open index.html in your browser.

Ensure all images inside the /assets/ folder remain in the same relative structure.

View form interaction in browser console for feedback.

## 🙌 Acknowledgments
This project was completed individually as part of the Coding Temple curriculum.
Inspired by Spotify for Artists design language.
All assets used are for educational purposes only.
