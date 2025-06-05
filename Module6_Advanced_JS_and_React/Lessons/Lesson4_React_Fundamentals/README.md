# Lesson 4: React Fundamentals

## Overview
In this lesson, you built your first React application using Vite. You learned how to structure a React project with reusable components, how to write JSX to define UI structure, and how React uses a virtual DOM to update the interface efficiently. You also practiced applying basic styles and organizing component logic into a maintainable hierarchy.

## Key Concepts
- Declarative, component-based design
- Functional components in React
- JSX (JavaScript XML) for defining UI
- Virtual DOM for efficient rendering
- Project setup with Vite and npm
- Component composition and hierarchy
- Styling with CSS and modular files

## Included Files

| Path                               | Description                                                |
|------------------------------------|------------------------------------------------------------|
| `src/main.jsx`                     | Entry point: renders `<App />` into `#root`                |
| `src/App.jsx`                      | Root component; renders the `Dashboard` component          |
| `src/components/Profile.jsx`       | A functional component returning a heading with a name     |
| `src/components/Dashboard.jsx`     | Contains `Profile`, a paragraph, and a clickable button    |
| `src/App.css`                      | Optional component-level styling                           |
| `src/index.css`                    | Global styles applied across the app                       |

## Learning Outcomes
By completing this lesson, you are now able to:

- Set up a modern React project using Vite
- Build and render functional React components
- Use JSX to describe UI structure clearly
- Pass React components into each other (composition)
- Apply global and component-level styling
- Start the development server and view live updates

## Run Locally

```bash
# Navigate to your project folder
cd vite-react-app

# Install dependencies
npm install

# Start the local dev server
npm run dev

# Visit in browser
http://localhost:5173
