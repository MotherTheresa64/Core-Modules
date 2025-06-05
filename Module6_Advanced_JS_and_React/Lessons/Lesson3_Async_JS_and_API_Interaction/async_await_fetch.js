async function fetchData() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/todos/1");

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log("Fetched Data:", data);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

fetchData();
