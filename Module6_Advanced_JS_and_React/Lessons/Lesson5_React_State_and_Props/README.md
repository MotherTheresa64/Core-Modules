# Lesson 5: React State and Props

## Overview
This lesson explores two foundational concepts in React: **state** and **props**. You will learn how to manage local component state using the `useState` hook, pass data between components using props, and combine both to build responsive and interactive interfaces.

## Key Concepts
- `useState()` Hook for managing state
- Event handling and state updates
- Passing props from parent to child
- Default props and prop drilling
- Conditional rendering
- Rendering dynamic lists with `map()`
- Best practices for managing state and props

## Included Files

| Path                                       | Description                                                  |
|--------------------------------------------|--------------------------------------------------------------|
| `src/main.jsx`                             | Entry point for rendering the root App component             |
| `src/App.jsx`                              | Parent component demonstrating state and props usage         |
| `src/components/Counter.jsx`               | Component that manages and displays a counter with buttons   |
| `src/components/MessageDisplay.jsx`        | Child component that receives and displays a message prop    |
| `src/components/MessageList.jsx`           | Renders a list of usernames passed via props                 |
| `src/App.css`                              | Basic styling for layout and components                      |

## Learning Outcomes
By completing this lesson, you will be able to:

- Create and update state using the `useState` hook
- Trigger state changes with events (like button clicks)
- Pass props between parent and child components
- Handle conditional rendering using state and props
- Apply best practices for clean and maintainable component structure

## Run Locally

```bash
# Navigate into the app folder
cd react-state-props-app

# Install dependencies
npm install

# Run the dev server
npm run dev

# Visit the app in your browser
http://localhost:5173
