async function fetchWithErrorHandling() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/invalid-endpoint");

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log("Data:", data);
  } catch (error) {
    console.error("There was an error with the request:", error.message);
  }
}

fetchWithErrorHandling();
