// Engage & Apply: Simple if...else if...else Practice
let temperature = 72;
if (temperature > 75) {
  console.log("It's a hot day!");
} else if (temperature > 70) {
  console.log("It's a beautiful day!");
} else {
  console.log("It's a cool day.");
}

// Engage & Apply: Ticket Checker Program
let age = 30;
let hasVIPPass = true;

if (age < 5) {
  console.log("Free entry!");
} else if (age >= 5 && age <= 12) {
  console.log("Child ticket: $10");
} else if (age >= 13 && age <= 64) {
  console.log("Adult ticket: $20");
} else {
  console.log("Senior ticket: $15");
}

if (hasVIPPass) {
  console.log("VIP Access Granted");
}

// Engage & Apply: Weather Outfit Selector (Switch Statement)
let weather = "snowy";
switch (weather) {
  case "sunny":
    console.log("Wear sunglasses and a t-shirt!");
    break;
  case "rainy":
    console.log("Don't forget your umbrella and raincoat.");
    break;
  case "snowy":
    console.log("Bundle up! It's time for a heavy coat and gloves.");
    break;
  case "cloudy":
    console.log("A light jacket should be enough.");
    break;
  case "windy":
    console.log("Hold onto your hat and wear a windbreaker.");
    break;
  default:
    console.log("I'm not sure what to wear in this weather!");
}

// Final Challenge: Build a Simple Calculator
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

function multiply(a, b) {
  return a * b;
}

function divide(a, b) {
  if (b === 0) {
    return "Error: Division by zero";
  }
  return a / b;
}

function calculator(num1, num2, operation) {
  switch (operation) {
    case "add":
      return add(num1, num2);
    case "subtract":
      return subtract(num1, num2);
    case "multiply":
      return multiply(num1, num2);
    case "divide":
      return divide(num1, num2);
    default:
      return "Invalid operation";
  }
}

// Example calculator usage:
console.log(calculator(10, 5, "add"));      // Output: 15
console.log(calculator(10, 5, "divide"));   // Output: 2
console.log(calculator(10, 0, "divide"));   // Output: Error: Division by zero

// Bonus: Arrow function version of add
const arrowAdd = (a, b) => a + b;
console.log(arrowAdd(7, 8)); // Output: 15
