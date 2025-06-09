# 🧭 Lesson 4 - Single Page Applications (SPAs), Axios, and React Routing

This project demonstrates how to build a Single Page Application (SPA) using **React Router**, **Axios**, and **JSONPlaceholder**. It includes dynamic routing, API data fetching, user-specific pages, error handling, and a custom 404 page with a redirect.

## 📦 Overview

The app fetches and displays a list of users from [JSONPlaceholder](https://jsonplaceholder.typicode.com/), allows navigation to view each user's todo list, and handles undefined routes with a countdown-based redirect to the homepage.

## 🧠 Key Concepts Covered

- React Router (SPA navigation without page reloads)
- Dynamic routing with URL parameters (`/user-todos/:userId`)
- Axios for HTTP requests
- useEffect and useState for managing async data and reactivity
- useParams and useNavigate from `react-router-dom`
- Conditional rendering with loading/error states
- Reusable NavBar component
- Custom 404 page with redirect timer

## 📁 File Structure

Lesson4_SPAs_Axios_ReactRouting/
├── public/
├── src/
│ ├── components/
│ │ ├── HomePage.jsx
│ │ ├── NavBar.jsx
│ │ ├── NotFound.jsx
│ │ ├── UserTodos.jsx
│ │ └── Users.jsx
│ ├── App.jsx
│ ├── index.css
│ ├── main.jsx
├── index.html
├── package.json
├── vite.config.js
└── README.md


## 🚀 Running the App

1. **Install dependencies**
   ```bash
   npm install
2. **Start the development server**
  ```bash
   npm run dev
3. **Open your browser and go to your localhost page

✅ Learning Outcomes
By completing this project, I have demonstrated the ability to:

Build a fully functional SPA using React Router

Fetch data from a public API using Axios

Display conditional content based on dynamic route parameters

Implement programmatic navigation with useNavigate()

Create a user-friendly navigation system and fallback UI

