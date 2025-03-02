import requests
from decouple import config

# Mapping of character names to their corresponding names in the API
CHARACTER_NAME_MAPPING = {
    "Aragorn": "Aragorn II Elessar",
    "Frodo": "Frodo Baggins",
    # Add other mappings as needed
}

def fetch_character_id(character_name):
    """
    Fetch the character ID from an external service.

    params: character_name (str): The name of the character to fetch the ID for.
    returns: Character ID or error message
    """
    # Use the mapped name if it exists, otherwise use the original name
    api_character_name = CHARACTER_NAME_MAPPING.get(character_name, character_name)
    
    url = "https://the-one-api.dev/v2/character"
    headers = {
        "Authorization": f"Bearer {config('API_BEARER_TOKEN')}"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for character in data['docs']:
                if character['name'].lower() == api_character_name.lower():
                    return character['_id']
            return f"Error: Character '{character_name}' not found."
        else:
            return f"Error: Failed to fetch character ID. Status code: {response.status_code}"
    except requests.RequestException as e:
        return f"Error: {str(e)}"

def fetch_quotes(character_id):
    """
    Fetch quotes from an external service.

    params: character_id (str): The ID of the character to fetch quotes for.
    returns: List of quotes or error message
    """
    url = f"https://the-one-api.dev/v2/character/{character_id}/quote"
    headers = {
        "Authorization": f"Bearer {config('API_BEARER_TOKEN')}"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return [quote['dialog'] for quote in data['docs']]
        else:
            return [f"Error: Failed to fetch quotes. Status code: {response.status_code}"]
    except requests.RequestException as e:
        return [f"Error: {str(e)}"]

# Add a function to fetch and print all character names for debugging
def fetch_all_characters():
    url = "https://the-one-api.dev/v2/character"
    headers = {
        "Authorization": f"Bearer {config('API_BEARER_TOKEN')}"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for character in data['docs']:
                print(character['name'])
        else:
            print(f"Error: Failed to fetch characters. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {str(e)}")

