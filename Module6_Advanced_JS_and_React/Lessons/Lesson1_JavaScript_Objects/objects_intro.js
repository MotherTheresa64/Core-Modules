// Creating an object using object literal notation
let student = {
  name: "Alex",
  age: 21,
  enrolled: true,
  courses: ["JavaScript", "HTML", "CSS"],
  greet: function () {
    console.log(`Hello, I am ${this.name}`);
  }
};

// Accessing properties
console.log(student.name);        // Output: Alex
console.log(student["age"]);      // Output: 21

// Adding a new property
student.city = "New York";

// Modifying an existing property
student.age = 31;

// Calling a method
student.greet();                  // Output: Hello, I am Alex
