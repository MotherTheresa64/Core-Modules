let student = {
  name: "Alice",
  age: 21,
  address: {
    street: "123 Main St",
    city: "Springfield",
    zipCode: "62704"
  },
  courses: ["JavaScript", "HTML", "CSS"]
};

// Accessing nested properties
console.log(student.address.city);          // Output: Springfield

// Modifying nested properties
student.address.city = "Chicago";
student.address.zipCode = "60601";

// Adding new nested property
student.address.country = "USA";

// Looping through nested object
for (let key in student.address) {
  console.log(`${key}: ${student.address[key]}`);
}
