# 🎧 Recreate Spotify with Bootstrap & JavaScript

This project is a simplified recreation of a Spotify-themed website. It demonstrates modern front-end development skills using **Bootstrap** for layout and styling, along with **JavaScript** to simulate interactive features.

The assignment was completed as part of the **Module 5: Frameworks & Intro to JavaScript** curriculum for Coding Temple.

---

## 🛠 Features Implemented

### 🔷 Bootstrap Components
- **Responsive Navigation Bar** with collapsing hamburger menu on smaller screens
- **Hero Section** with fluid background banner
- **Registration Form** using:
  - Bootstrap form controls and grid layout
  - Required fields with validation
  - `btn-success` styled submit button
- **Responsive Table** to simulate user data submissions
  - Styled with `table-striped` and `table-hover`
  - Wrapped in `table-responsive`
- **Image Utilities**
  - `img-fluid` full-width banner
  - `rounded-circle` image displayed below
- **Buttons with Utility Classes**
  - One button is always visible
  - Another hidden on small screens using `d-none d-md-block`

---

## 💻 JavaScript Functions

Although this assignment doesn’t require backend integration, JavaScript was used to simulate basic interactivity:

- **Form Validation Handler** for a feedback section
  - Ensures all fields are filled before submission
  - Displays a status message on success or error
  - Logs form input to the browser console

All form logic is contained in [`script.js`](script.js) and executed on `DOMContentLoaded`.

---

## 📁 File Structure

Lesson_Project_Recreate_Spotify/
├── assets/
│ ├── background.jpg
│ ├── spotify-logo-dark.png
│ ├── spotify-logo-green.png
│ ├── spotify-logo-white.png
│ ├── spotify-logo-pink.png
│ ├── album1.jpg
│ ├── album2.jpg
│ ├── user1.png
│ └── user2.png
├── index.html
├── styles.css
├── script.js
└── README.md


---

## 🌐 How to Run the Project

1. Clone this repository to your local machine.
2. Open the `index.html` file in any web browser.
3. Interact with the form and observe console logs.
4. Resize the window to test responsive design features.

No server or backend setup is required.

---

## ✅ Completion Status

All requirements from the [Module 5 Knowledge Check: Bootstrap Basics, Utilities, Forms, and Components] assignment have been met or exceeded.

---

## 🧪 Testing Suggestions

- Verify responsive behavior across different screen sizes.
- Submit the feedback form with all fields filled and observe the console output.
- Resize the window to see visibility changes in the utility buttons.

---

© 2025 Spotify Recreate — Educational Use Only
