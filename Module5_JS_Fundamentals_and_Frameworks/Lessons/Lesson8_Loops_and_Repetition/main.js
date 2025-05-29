// Increment / Decrement Example
let a = 5;
console.log(++a); // 6
let b = 5;
console.log(b++); // 5
console.log(b);   // 6

// for Loop: 1 to 10, log even numbers
for (let i = 1; i <= 10; i++) {
  if (i % 2 === 0) {
    console.log(i + " is an even number.");
  }
}

// for...of Loop: Iterate over array
let colors = ['red', 'green', 'blue'];
for (let color of colors) {
  console.log("Color:", color);
}

// for...in Loop: Indexes of array
let numbers = [10, 20, 30];
for (let index in numbers) {
  console.log(`Index: ${index}, Value: ${numbers[index]}`);
}

// while Loop: 1 to 3
let i = 1;
while (i <= 3) {
  console.log("While iteration:", i);
  i++;
}

// do...while Loop: 1 to 3
let j = 1;
do {
  console.log("Do-while iteration:", j);
  j++;
} while (j <= 3);

// Nested Loops: Multiplication Table (1 to 3)
for (let x = 1; x <= 3; x++) {
  for (let y = 1; y <= 3; y++) {
    console.log(`${x} x ${y} = ${x * y}`);
  }
}

// break example: stop at 3
for (let k = 1; k <= 5; k++) {
  if (k === 3) break;
  console.log("Break test:", k);
}

// continue example: skip 3
for (let m = 1; m <= 5; m++) {
  if (m === 3) continue;
  console.log("Continue test:", m);
}

// Final Challenge: Multiplication Table 1-5
console.log("Multiplication Table 1–5:");
for (let row = 1; row <= 5; row++) {
  let output = "";
  for (let col = 1; col <= 5; col++) {
    output += (row * col) + "\t";
  }
  console.log(output);
}
