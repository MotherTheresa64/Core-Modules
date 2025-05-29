// Lesson 6 Practice: Variables, Output, Operators

// Declare variables
const myName = "Noah";
let myAge = 23;
let likesCoding = true;

// Output values
console.log(`Name: ${myName}`);
console.log(`Age: ${myAge}`);
console.log(`Likes coding: ${likesCoding}`);

// Increment age and log again
myAge++;
console.log(`New Age: ${myAge}`);

// Modulus
let remainder = myAge % 5;
console.log(`Remainder when age is divided by 5: ${remainder}`);

// Type conversion
let ageStr = String(myAge);
console.log(`Age as a string: ${ageStr}`);

// Comparison
let isOlderThan20 = myAge > 20;
console.log(`Is age greater than 20? ${isOlderThan20}`);

// Button click alert (inline behavior trigger)
document.getElementById("btn").onclick = function () {
  alert("Button clicked!");
};
