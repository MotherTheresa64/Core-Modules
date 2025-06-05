function fetchData(callback) {
  setTimeout(() => {
    callback("Data received");
  }, 2000);
}

fetchData((message) => {
  console.log(message); // Output after 2 seconds: "Data received"
});
