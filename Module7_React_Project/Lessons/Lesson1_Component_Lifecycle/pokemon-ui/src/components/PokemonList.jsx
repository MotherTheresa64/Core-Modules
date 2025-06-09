import { useState, useEffect } from 'react';

function PokemonList() {
  const [pokemon, setPokemon] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPokemonData = async () => {
      const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=5');

      if (!response.ok) {
        throw new Error('Pokemon fetch did not work');
      }

      const pokemonData = await response.json();
      setPokemon(pokemonData.results);
      setLoading(false);
    };

    fetchPokemonData();
  }, []);

  if (loading) {
    return <div>Loading Pokemon...</div>;
  }

  return (
    <div>
      <h1>List of Pokemon</h1>
      <ul>
        {pokemon.map(poke => (
          <li key={poke.name}>
            <p>{poke.name}</p>
            <img src={`https://img.pokemondb.net/artwork/${poke.name}.jpg`} alt={poke.name} />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PokemonList;
