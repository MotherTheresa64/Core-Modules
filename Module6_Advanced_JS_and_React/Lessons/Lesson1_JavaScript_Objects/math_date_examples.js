// Math object usage
let num = 4.56;
console.log(Math.round(num));         // 5
console.log(Math.floor(num));         // 4
console.log(Math.ceil(num));          // 5
console.log(Math.max(3, 7, 1, 9));    // 9
console.log(Math.min(3, 7, 1, 9));    // 1
console.log(Math.pow(2, 3));          // 8
console.log(Math.sqrt(25));           // 5

// Random number between 1 and 10
let randomBetween1And10 = Math.floor(Math.random() * 10) + 1;
console.log(randomBetween1And10);

// Date object usage
let now = new Date();
console.log(now.toLocaleDateString());   // e.g. "10/21/2024"

let specificDate = new Date(2024, 9, 21, 12, 0, 0);  // October = 9
console.log(specificDate);

// Countdown to New Year
function getTimeUntilNewYear() {
  let now = new Date();
  let newYear = new Date(now.getFullYear() + 1, 0, 1);
  let diff = newYear - now;
  let days = Math.floor(diff / (1000 * 60 * 60 * 24));
  let hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
  let minutes = Math.floor((diff / (1000 * 60)) % 60);
  let seconds = Math.floor((diff / 1000) % 60);

  return `Time until New Year: ${days} days, ${hours} hours, ${minutes} minutes, and ${seconds} seconds`;
}

console.log(getTimeUntilNewYear());
