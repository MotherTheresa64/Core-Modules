# Lesson 6: Integrating Bootstrap with React | Part 2

## Overview

In this lesson, we expanded on our React Bootstrap knowledge by building a complete user form. We focused on React Bootstrap form components like `FloatingLabel`, `InputGroup`, `Form.Select`, and enhanced user interaction with `Modal` and `Offcanvas`. We also implemented custom validation using the `validated` prop and `Form.Control.Feedback`.

By the end of this lesson, we had a fully styled and functional form with success feedback, validation indicators, and dynamic modal/offcanvas interactions — all built using React Bootstrap.

## Key Concepts

- Creating styled forms with `Form.Control`, `FloatingLabel`, and `InputGroup`
- Using `Form.Select` and `Form.Check` for dropdowns and radio buttons
- Displaying dynamic messages with `Alert` and `Form.Control.Feedback`
- Handling `noValidate` and `validated` for Bootstrap-friendly validation
- Passing props to and managing state across components
- Integrating modals (`Modal`) and slide panels (`Offcanvas`) for UI feedback

## Included Files

| File Name         | Description                                               |
|------------------|-----------------------------------------------------------|
| `App.jsx`         | Added route for the new user form page                   |
| `UserForm.jsx`    | Main form component with validation and submission logic |
| `FormModal.jsx`   | Modal that displays returned form data                   |
| `OffCanvas.jsx`   | Slide-out drawer with supplemental info                  |

## Learning Outcomes

By the end of this lesson, you will be able to:

- Create and style interactive forms using React Bootstrap components
- Implement validation with `validated`, `checkValidity()`, and feedback messages
- Control modal visibility using props and state
- Render Offcanvas panels as optional guides or info boxes
- Manage user submission states (success, error, and feedback)
- Use conditional rendering to control UI based on validation and submission state
