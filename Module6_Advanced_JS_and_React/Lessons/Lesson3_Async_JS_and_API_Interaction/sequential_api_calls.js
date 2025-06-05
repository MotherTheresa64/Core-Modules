async function fetchMultipleData() {
  try {
    const userResponse = await fetch("https://jsonplaceholder.typicode.com/users/1");
    const user = await userResponse.json();

    const postsResponse = await fetch(`https://jsonplaceholder.typicode.com/users/${user.id}/posts`);
    const posts = await postsResponse.json();

    console.log("User:", user);
    console.log("User Posts:", posts);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

fetchMultipleData();
