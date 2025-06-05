const promise = new Promise((resolve, reject) => {
  let success = true;

  if (success) {
    resolve("Operation succeeded");
  } else {
    reject("Operation failed");
  }
});

promise
  .then((message) => {
    console.log(message);
  })
  .catch((error) => {
    console.error(error);
  });
