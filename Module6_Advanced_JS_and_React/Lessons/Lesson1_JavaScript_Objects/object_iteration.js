let person = {
  firstName: "John",
  lastName: "Doe",
  age: 31,
  occupation: "Developer"
};

// Using Object methods
console.log(Object.keys(person));    // ['firstName', 'lastName', 'age', 'occupation']
console.log(Object.values(person));  // ['John', 'Doe', 31, 'Developer']
console.log(Object.entries(person)); // [['firstName', 'John'], ['lastName', 'Doe'], ['age', 31], ['occupation', 'Developer']]
