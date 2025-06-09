# Lesson 5: Integrating Bootstrap with React | Part 1

## Overview

In this lesson, we integrated **React Bootstrap** into our existing JSONPlaceholder user app to enhance its UI with professionally styled, responsive components. We used layout components (`Container`, `Row`, `Col`), navigation (`Navbar`, `NavDropdown`), feedback elements (`Spinner`, `Badge`), and content containers (`Card`, `ListGroup`) to style all primary views of the app. This was our first step toward creating a fully polished user interface using React Bootstrap.

## Key Concepts

- Installing and importing **React Bootstrap** and **Bootstrap CSS**
- Preferred import patterns to reduce bundle size
- Layout components: `Container`, `Row`, `Col`
- Navigation components: `Navbar`, `Nav.Link`, `NavDropdown`
- Feedback and content components: `Spinner`, `Badge`, `Card`, `ListGroup`
- Routing with `react-router-dom`
- API integration with `axios`

## Included Files

| File                            | Description                                               |
|---------------------------------|-----------------------------------------------------------|
| `main.jsx`                      | React root with Router and Bootstrap imports              |
| `App.jsx`                       | Route controller and layout wrapper                       |
| `index.css` / `App.css`         | Wiped styles for Bootstrap override                       |
| `HomePage.jsx`                  | Home screen with Bootstrap `Carousel` layout              |
| `NavBar.jsx`                    | Responsive navbar using React Bootstrap                   |
| `NotFound.jsx`                  | 404 view with redirect countdown and `Badge`              |
| `Users.jsx`                     | API user list styled with `Card` and `Spinner`            |
| `UserTodos.jsx`                 | User todos list styled with `ListGroup` and `Spinner`     |
| `FormModal.jsx`                 | Placeholder for modal form component (to be built later)  |
| `OffCanvas.jsx`                 | Placeholder for off-canvas menu (to be built later)       |
| `UserForm.jsx`                  | Placeholder for user form logic (to be built later)       |

## Learning Outcomes

By the end of this lesson, you will be able to:

- Install and configure React Bootstrap into a Vite React project
- Create professional UI layouts using grid and display components
- Use React Router to manage view switching
- Handle loading and error states using Bootstrap `Spinner` and messages
- Display lists and user information in responsive Bootstrap `Cards` and `ListGroups`
- Prepare placeholder components for modal-based forms

