// Executes once after 3 seconds
setTimeout(() => {
  console.log("Timeout executed!");
}, 3000);

// Executes every 2 seconds
const intervalId = setInterval(() => {
  console.log("Interval executed every 2 seconds!");
}, 2000);

// Optional: Stop the interval after 7 seconds
setTimeout(() => {
  clearInterval(intervalId);
  console.log("Interval stopped.");
}, 7000);
