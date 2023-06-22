'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function

    poke_info = get_pokemon_info("Rockruff")
    return
    

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter
    pokemon_name = str(pokemon_name).strip().lower()

    # Build a clean URL and use it to send a GET request
    url = f"{POKE_API_URL}/{pokemon_name}"
    print(f"Sending a GET request to {url}")
    response = requests.get(url)

    # If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if response.status_code == requests.codes.ok:
        pokemon_data = response.json()
        return pokemon_data
    else:
    # If the GET request failed, print the error reason and return None
        print(f"Request failed: {response.text}")
        print(f"Status code: {response.status_code} ({response.reason})")
        return None


if __name__ == '__main__':
    main()