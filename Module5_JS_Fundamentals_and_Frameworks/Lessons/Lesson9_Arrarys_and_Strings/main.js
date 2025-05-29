// 📌 Basic Array Creation and Access
let fruits = ["apple", "banana", "cherry"];
console.log(fruits[0]);  // "apple"
console.log(fruits[2]);  // "cherry"

// 🛠 Updating and Modifying Arrays
fruits[1] = "grape";
fruits.push("orange");
fruits.unshift("mango");
fruits.pop();
fruits.shift();
fruits.splice(1, 0, "pear");   // Insert at index 1
fruits.splice(2, 1);           // Remove 1 at index 2
console.log(fruits);           // Final state

// 🔄 Task List Manager
let tasks = ["Do laundry", "Study JavaScript"];
tasks.push("Walk the dog");
tasks[1] = "Master JavaScript";
tasks.shift();
console.log(tasks);  // ["Master JavaScript", "Walk the dog"]

// ➕ Looping Through Arrays
let numbers = [1, 2, 3, 4, 5];

// for loop
for (let i = 0; i < numbers.length; i++) {
  console.log("for loop:", numbers[i]);
}

// for...of loop
for (let num of numbers) {
  console.log("for...of:", num);
}

// for...in loop
for (let index in numbers) {
  console.log(`for...in - Index: ${index}, Value: ${numbers[index]}`);
}

// 🔠 String Basics
let sentence = "JavaScript is awesome!";
console.log(sentence.toUpperCase());
let words = sentence.split(" ");
console.log(words);
let newSentence = sentence.replace("awesome", "powerful");
console.log(newSentence);
console.log(sentence.includes("JavaScript"));

// 🔁 Looping Through Strings
let word = "hello";

// for loop
for (let i = 0; i < word.length; i++) {
  console.log(`Char: ${word[i]}, Index: ${i}`);
}

// for...of
for (let char of word) {
  console.log("Char:", char);
}

// for...in
for (let index in word) {
  console.log(`Index: ${index}, Char: ${word[index]}`);
}

// 🔄 Conversion Between Arrays & Strings
let csv = "apple,banana,grape";
let fruitArray = csv.split(",");
console.log(fruitArray);

let joined = fruitArray.join(", ");
console.log(joined);

// 🧪 String Methods
let greeting = " Hello! ";
console.log(greeting.trim());
console.log(greeting.toLowerCase());
console.log(greeting.toUpperCase());

// 🧠 Final Challenge - forEach and map
let nums = [2, 4, 6, 8, 10];

nums.forEach((num) => {
  console.log("Doubled (forEach):", num * 2);
});

let doubledNums = nums.map((num) => num * 2);
console.log("Doubled (map):", doubledNums);

let string = "JavaScript is fun";
let splitWords = string.split(" ");

splitWords.forEach((word) => {
  console.log("Uppercase word:", word.toUpperCase());
});

let reversedWords = splitWords.map((word) =>
  word.split("").reverse().join("")
);
console.log("Reversed words:", reversedWords);
