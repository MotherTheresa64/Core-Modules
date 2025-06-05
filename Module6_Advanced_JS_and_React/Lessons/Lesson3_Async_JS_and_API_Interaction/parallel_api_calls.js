async function fetchParallelData() {
  try {
    const [userResponse, postsResponse] = await Promise.all([
      fetch("https://jsonplaceholder.typicode.com/users/1"),
      fetch("https://jsonplaceholder.typicode.com/posts")
    ]);

    const user = await userResponse.json();
    const posts = await postsResponse.json();

    console.log("User:", user);
    console.log("Posts:", posts);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

fetchParallelData();
