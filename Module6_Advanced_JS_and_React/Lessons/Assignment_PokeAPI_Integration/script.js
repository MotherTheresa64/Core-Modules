const searchBtn = document.getElementById("searchBtn");
const pokemonInput = document.getElementById("pokemonInput");
const pokemonDisplay = document.getElementById("pokemonDisplay");
const pokemonName = document.getElementById("pokemonName");
const pokemonImage = document.getElementById("pokemonImage");
const pokemonType = document.getElementById("pokemonType");
const errorMessage = document.getElementById("errorMessage");

searchBtn.addEventListener("click", async () => {
  const query = pokemonInput.value.trim().toLowerCase();
  if (!query) return;

  try {
    errorMessage.textContent = "";
    pokemonDisplay.classList.add("hidden");

    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${query}`);

    if (!response.ok) {
      throw new Error("Pokémon not found.");
    }

    const data = await response.json();

    // Populate DOM
    pokemonName.textContent = data.name.toUpperCase();
    pokemonImage.src = data.sprites.front_default;
    pokemonImage.alt = data.name;

    // Bonus: Display Pokémon type
    const typeList = data.types.map(t => t.type.name).join(", ");
    pokemonType.textContent = `Type: ${typeList}`;

    pokemonDisplay.classList.remove("hidden");
  } catch (error) {
    errorMessage.textContent = error.message;
  }
});
